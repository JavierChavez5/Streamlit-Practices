import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World")
st.write("## This is a H2 Title!")
x = st.text_input("Movie", "Star Wars")

if st.button("Click Me"):
    st.write(f"Your favorite movie is `{x}`")


data = pd.read_csv("movies.csv")
st.write(data)


st.write("# My Cool Chart")

chart_data=pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B','C']
)

st.bar_chart(chart_data)
st.line_chart(chart_data)


