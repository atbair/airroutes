# AirRouteApp ✈️

AirRouteApp is an interactive aviation route visualization tool built with Python, Streamlit, and Plotly.

A while ago, I wanted to explore all passenger airline routes between regions such as North America and Europe, but I could not find a simple way to visualize them. This project was built to solve that problem.

The app allows users to explore direct passenger airline routes between:

- Airports
- Countries
- Continents

It also identifies which airlines operate each route and visualizes connections on an interactive world map.

This project is currently a work in progress, with additional features and usability improvements planned.

## Live App

Try the app here:

https://airroutes-6kpgnbfwxdc5gbfpqqeqpz.streamlit.app/

---

## Features

- Explore airline routes by:
  - Airport
  - Country
  - Continent
- Interactive route visualization on a global map
- View airlines operating each route
- Route deduplication for cleaner visualization
- Dynamic filtering and route exploration

---

## Data Sources

This project combines two open datasets:

### Airline Route Data

Route and carrier information comes from:

**Jonty / airline-route-data**  
https://github.com/Jonty/airline-route-data

This dataset provides passenger airport routes and airline carrier information.

### Airport Metadata

Airport coordinates, country codes, continent information, and airport identifiers come from:

**OurAirports Open Data**  
https://github.com/davidmegginson/ourairports-data

Used for:

- Airport metadata
- Geolocation
- Country and continent filtering
- Route mapping

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
```

---

## Running Locally

Clone the repository:

```bash
git clone https://github.com/atbair/airroutes.git
cd airroutes
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run airroute.py
```

Update route data:

```bash
python update_data.py
```

---

## Future Improvements

Planned features include:

- Airline alliance filters (Star Alliance, SkyTeam, Oneworld)
- Airline-specific filtering
- Enhanced map styling
- Automated monthly route updates
- Improved mobile usability

---

## Author

Amir Bajehkian
