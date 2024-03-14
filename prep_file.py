import pandas as pd

data = pd.read_csv("gdp.csv")

data["date"] = pd.to_datetime(
    data["quarter"].str.replace(" ", "")
) + pd.offsets.QuarterEnd(0)

data.to_csv("clean_gdp.csv")
