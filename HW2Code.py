import polars as pl
import matplotlib.pyplot as plt

data = pl.read_csv("/Users/aidanburke/rsm-msba/my-repo/rogers.csv")
data = data.with_columns(pl.col("purchase_datetime").str.to_datetime("%m/%d/%Y %H:%M"))
data = data.with_columns(
    (
        pl.col("purchase_datetime") - pl.duration(minutes=pl.col("trip_duration_mins"))
    ).alias("est_entry")
)

time_session = data.group_by("session_id").agg(
    pl.col("est_entry").min().alias("session_start"),
    pl.col("purchase_datetime").max().alias("session_end"),
    pl.col("group_size").max().alias("group_size"),
    pl.col("trip_duration_mins").max().alias("trip_duration_mins"),
)

# time_session = time_session.with_columns(
# (pl.col("session_start").dt.truncate("15m")).alias("interval_start")
# )
# Inventory build up and average inventory calculation
entries = time_session.select(
    pl.col("session_start").alias("time"), pl.col("group_size").alias("change")
)

exits = time_session.select(
    pl.col("session_end").alias("time"), (-pl.col("group_size")).alias("change")
)
events = pl.concat([entries, exits]).sort("time")
inventory = events.with_columns(pl.col("change").cum_sum().alias("customers_inside"))
inventory = inventory.with_columns(pl.col("time").shift(-1).alias("next_time"))
inventory = inventory.with_columns(
    ((pl.col("next_time") - pl.col("time")).dt.total_minutes()).alias("minutes")
)
lunch_sessions = time_session.filter(
    (pl.col("session_start").dt.time() >= pl.time(11, 30, 0))
    & (pl.col("session_start").dt.time() < pl.time(13, 30, 0))
)

lunch_customers = lunch_sessions["group_size"].sum()

lunch_arrival_rate_per_hour = lunch_customers / 2
# Time flow for system
T = time_session.with_columns(
    (
        pl.col("trip_duration_mins") * pl.col("group_size") / pl.col("group_size").sum()
    ).alias("weighted_flow")
).sum()
T_hours = T["weighted_flow"] / 60
avg_inventory = lunch_arrival_rate_per_hour * 2 * T_hours
print(avg_inventory)


# customer_minutes = (inventory["customers_inside"] * inventory["minutes"]).sum()
# avg_inventory = customer_minutes / (16 * 60)
# inventory = events.with_columns(pl.col("change").cum_sum().alias("customers_inside"))
# inventory = inventory.with_columns(pl.col("time").dt.truncate("15m").alias("interval"))
# interval_inventory = (
#     inventory.group_by("interval")
#     .agg(pl.col("customers_inside").max().alias("max_customers"))
#     .sort("interval")
# )
# risk_intervals = interval_inventory.filter(pl.col("max_customers") > 12)

# risk_intervals = risk_intervals.with_columns(
#     pl.col("interval").dt.strftime("%I:%M %p").alias("time")
# )


# Plot of Customers Inside Rogers Market Over Time
# plt.step(inventory["time"], inventory["customers_inside"], where="post")
# plt.xlabel("Time")
# plt.ylabel("Customers Inside")
# plt.title("Number of Customers Inside Rogers Market")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# interval_totals = (
#     time_session.group_by("interval_start")
#     .agg(pl.col("group_size").sum().alias("total_group_size"))
#     .sort("interval_start")
# ).with_columns(pl.col("interval_start").dt.strftime("%I:%M %p").alias("interval_start"))

# Line plot of Customers per 15 minute interval
# plt.plot(interval_totals["interval_start"], interval_totals["total_group_size"])
# plt.xlabel("Entry Time")
# plt.ylabel("Number of Customers")
# plt.title("Customers Entering the Store Every 15 Minutes")
# plt.xticks(interval_totals["interval_start"][::4], rotation=45)
# plt.tight_layout()
# plt.show()
#
