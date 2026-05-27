import pandas as pd

routes = pd.read_csv("data/routes_master.csv")

print(
    routes[routes["origin"] == "DXB"]["destination"]
    .dropna()
    .sort_values()
    .unique()
)