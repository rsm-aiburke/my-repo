import polars as pl
import matplotlib.pyplot as plt

data = pl.read_csv("/Users/aidanburke/rsm-msba/my-repo/rogers.csv")
data = data.with_columns(pl.col("purchase_datetime").str.to_datetime("%m/%d/%Y %H:%M"))
data = data.with_columns(
    (
        pl.col("purchase_datetime") - pl.duration(minutes=pl.col("trip_duration_mins"))
    ).alias("est_entry")
)
# print(data.with_columns(pl.col("est_entry")))
time_session = data.group_by("session_id").agg(
    pl.col("est_entry").min().alias("session_start"),
    pl.col("group_size").max().alias("group_size"),
)

time_session = time_session.with_columns(
    (pl.col("session_start").dt.truncate("15m")).alias("interval_start")
)
interval_totals = (
    time_session.group_by("interval_start")
    .agg(pl.col("group_size").sum().alias("total_group_size"))
    .sort("interval_start")
).with_columns(pl.col("interval_start").dt.strftime("%I:%M %p").alias("interval_start"))

# Line plot of Customers per 15 minute interval
plt.plot(interval_totals["interval_start"], interval_totals["total_group_size"])
plt.xlabel("Entry Time")
plt.ylabel("Number of Customers")
plt.title("Customers Entering the Store Every 15 Minutes")
plt.xticks(interval_totals["interval_start"][::4], rotation=45)
plt.tight_layout()
plt.show()
