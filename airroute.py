import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# Load routes data
routes = pd.read_csv(
    "data/routes_master.csv",
    keep_default_na=False
)


def filter_routes(
    df,
    source_type=None,
    source_value=None,
    dest_type=None,
    dest_value=None,
    unique_paths=False
):
    filtered = df.copy()

    # Source filtering
    if source_type == "airport" and source_value is not None:
        filtered = filtered[
            filtered["origin"] == source_value
        ]

    elif source_type == "country" and source_value is not None:
        filtered = filtered[
            filtered["source_country_name"] == source_value
        ]

    elif source_type == "continent" and source_value is not None:
        filtered = filtered[
            filtered["source_continent"] == source_value
        ]

    # Destination filtering
    if dest_type == "airport" and dest_value is not None:
        filtered = filtered[
            filtered["destination"] == dest_value
        ]

    elif dest_type == "country" and dest_value is not None:
        filtered = filtered[
            filtered["destination_country_name"] == dest_value
        ]

    elif dest_type == "continent" and dest_value is not None:
        filtered = filtered[
            filtered["destination_continent"] == dest_value
        ]

    # Remove duplicate airline-route combos
    if unique_paths:
        filtered = filtered.drop_duplicates(
            subset=["path", "carrier_iata"]
        )

    return filtered


# Dropdown lists
countries = sorted(
    routes["source_country_name"]
    .dropna()
    .unique()
)

airportlist = sorted(
    routes["origin"]
    .dropna()
    .unique()
)

continents = sorted(
    routes["source_continent"]
    .dropna()
    .unique()
)

# -------------------------
# SOURCE FILTER
# -------------------------

source_type = st.selectbox(
    "Select region type for origin",
    ("continent", "country", "airport"),
)

if source_type == "continent":
    source_value = st.selectbox(
        "Select origin continent",
        continents
    )

elif source_type == "country":
    source_value = st.selectbox(
        "Select origin country",
        countries
    )

else:
    source_value = st.selectbox(
        "Select origin airport",
        airportlist
    )

# -------------------------
# DESTINATION FILTER
# -------------------------

dest_type = st.selectbox(
    "Select region type for destination",
    ("continent", "country", "airport"),
)

if dest_type == "continent":
    dest_value = st.selectbox(
        "Select destination continent",
        sorted(
            routes["destination_continent"]
            .dropna()
            .unique()
        )
    )

elif dest_type == "country":
    dest_value = st.selectbox(
        "Select destination country",
        sorted(
            routes["destination_country_name"]
            .dropna()
            .unique()
        )
    )

else:
    dest_value = st.selectbox(
        "Select destination airport",
        sorted(
            routes["destination"]
            .dropna()
            .unique()
        )
    )

# -------------------------
# FILTER ROUTES
# -------------------------

chosen_routes = filter_routes(
    routes,
    source_type,
    source_value,
    dest_type,
    dest_value,
    unique_paths=True
)

st.write(
    f"Routes found: {len(chosen_routes)}"
)

# -------------------------
# KEEP ONLY MAPPABLE ROUTES
# -------------------------

map_routes = chosen_routes.dropna(
    subset=[
        "source_latitude_deg",
        "source_longitude_deg",
        "destination_latitude_deg",
        "destination_longitude_deg"
    ]
)

# -------------------------
# GROUP AIRLINES BY ROUTE
# -------------------------

map_routes = (
    map_routes
    .groupby(
        ["path", "origin", "destination"],
        as_index=False
    )
    .agg({
        "carrier_name":
            lambda x: ", ".join(
                sorted(set(x.dropna()))
            ),
        "source_latitude_deg": "first",
        "source_longitude_deg": "first",
        "destination_latitude_deg": "first",
        "destination_longitude_deg": "first"
    })
)

# -------------------------
# CREATE MAP
# -------------------------

fig = go.Figure()

for i in range(len(map_routes)):
    fig.add_trace(
        go.Scattergeo(
            lon=[
                map_routes[
                    "source_longitude_deg"
                ].iloc[i],

                map_routes[
                    "destination_longitude_deg"
                ].iloc[i]
            ],

            lat=[
                map_routes[
                    "source_latitude_deg"
                ].iloc[i],

                map_routes[
                    "destination_latitude_deg"
                ].iloc[i]
            ],

            hovertext=(
                str(
                    map_routes["origin"]
                    .iloc[i]
                )
                + " → "
                + str(
                    map_routes["destination"]
                    .iloc[i]
                )
                + "<br>Airlines: "
                + str(
                    map_routes["carrier_name"]
                    .iloc[i]
                )
            ),

            hoverinfo="text",
            mode="lines+markers",
            line=dict(
                width=1,
                color="red"
            ),
            showlegend=False
        )
    )

fig.update_layout(
    height=700
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.caption(

    "Data sources: Jonty/airline-route-data for route/carrier data (https://github.com/Jonty/airline-route-data); "

    "OurAirports for airport metadata and coordinates (https://github.com/davidmegginson/ourairports-data)"

)