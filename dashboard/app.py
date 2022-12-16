# SETUP
import streamlit as st

import numpy as np
import pandas as pd
import altair as alt

from pathlib import Path
import datetime as dt
from datetime import datetime

#-------------------#
# DATA

# Data import
df = pd.read_csv("../data/external/data.csv", on_bad_lines='skip')

#-------------------#
# START OF APP

#-------------------#
# SIDEBAR

# Header
st.sidebar.header("Your opinion is requested:")

# Make a slider
handling = st.sidebar.slider('How do you assess the handling of corona in the usa at the moment on a scale from 1 to 10?', 0, 10, 1)

# Show output of slider selection
st.sidebar.write("my assessment is ", handling, 'from 10 points')

#-------------------#

# HEADER

# Title of our app
st.title("US POLITICS") 
# Add a gif
st.markdown("![Alt Text](https://media.giphy.com/media/onjwu5lrSCrvbUQVfR/fullscreen/giphy.gif)")
# Add header
st.header("The following visualizations are about the opinion of different groups in America concerning Trump and Bidens handling of the coronavirus outbreak")


#-------------------#
# BODY

###-------------------###

# Chart 1

st.subheader("Chart 1")
st.write("Bar plot:")

# Data structure 

df['party'] = df['party'].astype("category")
df['sample_size'] = df['sample_size'].astype("category")

## Exploratory data analysis

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
    color='orange'
)

c = chart

# Show plot
st.altair_chart(c, use_container_width=True)


###-------------------###

# Chart 2

st.subheader("Chart 2")
st.write("The data:")

### Data structure

df['population'] = df['population'].astype("category")

## Exploratory data analysis

source = pd.DataFrame(df.population.value_counts())

source = source.reset_index()

source.rename(columns={"index": "Population", "population": "count"}, inplace=True)

source 

#-------------------#

st.write("Pie chart of the data:")

chart = alt.Chart(source).mark_arc(innerRadius=30).encode(
    theta=alt.Theta("count:Q", stack=True), 
    color=alt.Color("Population:N"),
    tooltip=["count", "Population"]
).properties(
    height=500, width=500,
    title="Questioned Population"
)


pie = chart.mark_arc(outerRadius=110)
legend = chart.mark_text(radius=160, size=30).encode(text="Population:N")

c = pie + legend 

# Show plot
st.altair_chart(c, use_container_width=True)


###-------------------###

# Chart 3

st.subheader("Chart 3")
st.write("Stacked bar chart:")

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

st.subheader("Chart 4")
st.write("Stacked bar chart:")

### Data structure

df.pollster = df.pollster.astype("category")
df.subject = df.subject.astype("category")

## Exploratory data analysis

chart = alt.Chart(df).mark_bar(
    cornerRadiusTopLeft=50,
    cornerRadiusTopRight=50,
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
    fontSize=20,
    font='Arial',
    anchor='middle',
    color='orange'
)


c = chart

# Show plot
st.altair_chart(c, use_container_width=True)

###-------------------###

#End
st.write("Now you know more about US politics.")

