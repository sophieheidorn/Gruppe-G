# SETUP
import streamlit as st

import numpy as np
import pandas as pd
import altair as alt

from pathlib import Path
# import datetime as dt
# from datetime import datetime

#-------------------
# DATA

# Data import
df = pd.read_csv("https://github.com/sophieheidorn/homework-1/blob/main/data/external/data.csv", on_bad_lines='skip')

# Chart 1

# Data structure 
## Exploratory data analysis

df['party'] = df['party'].astype("category")
df['sample_size'] = df['sample_size'].astype("category")

#-------------------
# START OF APP

#-------------------
# SIDEBAR

# Make a sidebar  
chart_party = st.sidebar.multiselect('Select party', df['party'].unique().tolist())

# Create a subset out of chart_party 
# if len(chart_party) > 0:
   # df_subset = df[df['party'].isin(chart_party)]
    #evtl.raus

#-------------------
# HEADER

# Title of our app
st.title("Count of party members questioned ")
# Add header
st.header("This is the interactive app from team G")
# Add picture
st.image('hdm-logo.jpg')

#-------------------
# BODY

#-------------------
# Show static DataFrame
st.subheader("Show Data")
st.write("Here's my data:")


chart = alt.Chart(df).mark_bar(size = 40).encode(
    x=alt.X('party',
            sort='-y',
            axis=alt.Axis(title="Party", 
                          titleAnchor="middle", 
                          labelAngle=0)),
    y=alt.Y('count(party)', 
            axis=alt.Axis(title = "Count", 
                          titleAnchor="middle")),
    color=alt.Color('party', scale=alt.Scale(scheme='pastel2'))
).properties(
    title='Count of party members questioned ',
    width=350,
    height=250
).configure_title(
    fontSize=15,
    font='Arial',
    anchor='middle',
    color='black'
)

chart

c = chart

# Show plot
st.altair_chart(c, use_container_width=True)

###-------------------###

chart = alt.Chart(source).mark_arc(innerRadius=30).encode(
    theta=alt.Theta("count:Q", stack=True), 
    color=alt.Color("Population:N"),
    tooltip=["count", "Population"]
).properties(
    height=300, width=300,
    title="Questioned Population"
)


pie = chart.mark_arc(outerRadius=120)
legend = chart.mark_text(radius=140, size=20).encode(text="Population:N")



pie + legend

c = pie + chart

# Show plot
st.altair_chart(c, use_container_width=True)

###-------------------###
