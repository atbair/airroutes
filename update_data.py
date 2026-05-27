import requests
import pandas as pd

airports_df = pd.read_csv(
    "https://github.com/davidmegginson/ourairports-data/raw/refs/heads/main/airports.csv"
)

airports = airports_df[
    ["name", "iata_code", "latitude_deg", "longitude_deg", "iso_country", "continent"]
].copy()

airports["continent"] = airports["continent"].fillna("NA")

url = "https://github.com/Jonty/airline-route-data/raw/refs/heads/main/airline_routes.json"
response = requests.get(url)
response.raise_for_status()
routes_json = response.json()

rows = []

for airport_code, airport_data in routes_json.items():
    for route in airport_data["routes"]:
        destination = route["iata"]

        if len(route["carriers"]) == 0:
            rows.append({
                "origin": airport_code,
                "destination": destination,
                "carrier_iata": None,
                "carrier_name": None,
            })

        for carrier in route["carriers"]:
            rows.append({
                "origin": airport_code,
                "destination": destination,
                "carrier_iata": carrier.get("iata"),
                "carrier_name": carrier.get("name"),
            })

routes = pd.DataFrame(rows)

source_airports = airports.rename(columns={
    "name": "source_name",
    "iata_code": "source_iata_code",
    "latitude_deg": "source_latitude_deg",
    "longitude_deg": "source_longitude_deg",
    "iso_country": "source_country_name",
    "continent": "source_continent"
})

destination_airports = airports.rename(columns={
    "name": "destination_name",
    "iata_code": "destination_iata_code",
    "latitude_deg": "destination_latitude_deg",
    "longitude_deg": "destination_longitude_deg",
    "iso_country": "destination_country_name",
    "continent": "destination_continent"
})

routes = routes.merge(
    source_airports,
    left_on="origin",
    right_on="source_iata_code",
    how="left"
)

routes = routes.merge(
    destination_airports,
    left_on="destination",
    right_on="destination_iata_code",
    how="left"
)
routes["path"] = routes["origin"] + "-" + routes["destination"]

routes = routes.drop_duplicates(
    subset=["path", "carrier_iata"]
)

routes.to_csv("data/routes_master.csv", index=False)