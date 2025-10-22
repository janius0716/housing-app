import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style()

st.title('California Housing Data (1990) by Zhijia Zhou')
df = pd.read_csv('housing.csv')

median_house_value_filter = st.slider('Minimal Median House Price:', 0, 500001, 200000)

ocean_proximity_filter = st.sidebar.multiselect(
    'ocean_proximity Type Selector',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique()
)
df = df[df.ocean_proximity.isin(ocean_proximity_filter)]

median_income = st.sidebar.radio(
    'Income Level',
    ["Low", "Medium", "High"]
)

if median_income == "Low":
    df = df[df.median_income <= 2.5]
elif median_income == "Medium":
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif median_income == "High":
    df = df[df.median_income > 4.5]

st.map(df)
st.subheader("Histogram of Median House Value")
fig, ax = plt.subplots(figsize=(10, 7))
df.median_house_value.hist(bins = 30)
st.pyplot(fig)