# SETUP
import streamlit as st

import numpy as np
import pandas as pd
import altair as alt

from pathlib import Path
import datetime as dt
from datetime import datetime

#-------------------
# DATA

# Data import
df = pd.read_csv("../data/external/data.csv", on_bad_lines='skip')



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
# st.image('hdm-logo.jpg')

#-------------------
# BODY

#-------------------
# Show static DataFrame
st.subheader("Show Data")
st.write("Here's my data:")

###-------------------###

# Chart 1

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

c = chart

# Show plot
st.altair_chart(c, use_container_width=True)

###-------------------###

# Chart 2

### Data structure

df['population'] = df['population'].astype("category")

## Exploratory data analysis

source = pd.DataFrame(df.population.value_counts())

source = source.reset_index()

source.rename(columns={"index": "Population", "population": "count"}, inplace=True)

source



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

c = pie + legend

# Show plot
st.altair_chart(c, use_container_width=True)

###-------------------###

# Chart 3

### Data structure

df.subject = df.subject.astype("category")
df.party = df.party.astype("category")

## Exploratory data analysis

chart = alt.Chart(df).mark_bar(size = 60).encode(
    x=alt.X('subject',
            sort='-y',
            axis=alt.Axis(title="Subject", 
                          titleAnchor="middle", 
                          labelAngle=0)),
    y=alt.Y('count(subject)', 
            axis=alt.Axis(title = "Count", 
                          titleAnchor="middle")),
    color= alt.Color('party', 
                     legend=alt.Legend(title="Party"), scale=alt.Scale(scheme='tableau20')),
    tooltip=["subject", "party", "count(subject)"]
).interactive(
).properties(
    title='How many people of which party were questioned for each Trump and Biden?',
    width=350,
    height=250
).configure_title(
    fontSize=15,
    font='Arial',
    anchor='middle',
    color='orange'
)

c = chart

# Show plot
st.altair_chart(c, use_container_width=True)

###-------------------###

# Chart 4

### Data structure

df.pollster = df.pollster.astype("category")
df.subject = df.subject.astype("category")

## Exploratory data analysis

chart = alt.Chart(df).mark_bar(
    cornerRadiusTopLeft=3,
    cornerRadiusTopRight=3,
    size=10
).encode(
    x=alt.X('pollster:O',
            sort='-y',
            axis=alt.Axis(title="Pollster", 
                          titleAnchor="middle")),
    y=alt.Y('count(subject):Q', 
            axis=alt.Axis(title = "Count(Subject)", 
                          titleAnchor="middle")),
    color=alt.Color('subject:N', 
                     legend=alt.Legend(title="Subject"), scale=alt.Scale(scheme='dark2')),
    tooltip=[ "pollster", "subject", "count(subject)"]
).interactive(
).properties(
    title='How many polls did the pollsters carry out for each Trump and Biden?',
    width=900,
    height=550
).configure_title(
    fontSize=25,
    font='New Times Roman',
    anchor='middle',
    color='orange'
)

c = chart

# Show plot
st.altair_chart(c, use_container_width=True)

###-------------------###
