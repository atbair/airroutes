#AirRouteApp ✈️
A while ago I wondered how I can find all the passenger airline routes between US and Europe. There was no where I could visualize it. So I decided to make one myself.

This project can display routes between airports/countries/continents. Additionally, it can show the airlines flying them.

It is a work in progress to make it more user friendly. 

The app can be run live on Strimlit:

##Data Sources:
The two sets of data are airport and route data:
### Airline Route Data

Route and carrier information comes from:

Jonty / airline-route-data (GitHub: https://github.com/Jonty/airline-route-data)

This dataset provides passenger airport routes and airline carrier information.

### Airport Metadata

Airport coordinates, country codes, and continent information come from:

OurAirports Open Data (Github: https://github.com/davidmegginson/ourairports-data)

Used for:

- airport metadata

- geolocation

- continent and country filtering

---

## Tech Stack

- Python

- Pandas

- Streamlit

- Plotly

- Requests

- Git / GitHub

---

## Project Structure

```text

airrouteapp/

├── airroute.py

├── update_data.py

├── requirements.txt

├── README.md

└── data/

    └── routes_master.csv
