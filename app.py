import streamlit as st
from multiapp import MultiApp
from dashboard import data_dash
app = MultiApp()

st.sidebar.markdown('# **Pharmaceutical Sales forcasting**')
st.sidebar.markdown("""
The aim of this project is to predict the sales six weeks ahead across all the stores of the Rossman Pharmaceutical company using Machine and Deep Learning. The different factors affecting the sales are: promotions, competitions, school-state holiday, seasonality, and locality.
""")

# Add all your application here

app.add_app("Data sets", data_dash.app)

# The main app
app.run()