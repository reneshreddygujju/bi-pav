import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("Human_Resources.csv")

st.set_page_config(layout="wide")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Employees", len(df))
col2.metric("Average Age", round(df["Age"].mean(), 2))
col3.metric("Average Tenure", round(df["Tenure"].mean(), 2))

# Charts
c1, c2 = st.columns(2)

with c1:
    dept = df["Department"].value_counts()
    fig = px.bar(
        dept,
        x=dept.values,
        y=dept.index,
        orientation="h",
        title="Employees by Department"
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    gender = df["Gender"].value_counts()
    fig = px.pie(
        values=gender.values,
        names=gender.index,
        hole=0.5,
        title="Gender Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

c3, c4 = st.columns(2)

with c3:
    race = df["Race"].value_counts()
    fig = px.bar(
        race,
        x=race.values,
        y=race.index,
        orientation="h",
        title="Count of Race"
    )
    st.plotly_chart(fig, use_container_width=True)

with c4:
    df["Hire Date"] = pd.to_datetime(df["Hire Date"], dayfirst=True)
    hiring = df.groupby(df["Hire Date"].dt.year).size()

    fig = px.line(
        x=hiring.index,
        y=hiring.values,
        title="Hiring Trend by Year"
    )
    st.plotly_chart(fig, use_container_width=True)
