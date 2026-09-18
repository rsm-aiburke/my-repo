import polars as pl

data = pl.read_csv("/Users/aidanburke/rsm-msba/my-repo/rogers.csv")
# print(data)
data = data.with_columns(pl.col("purchase_datetime").str.to_datetime("%Y-%m-%d %H:%M"))
