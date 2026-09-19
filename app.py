import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title='Vehicle Sales Dashboard',
    page_icon='🚗',
    layout='wide'
)

st.title('Vehicle Sales Dashboard')

st.write(
    'Interactive exploration of vehicle sales advertisements, '
    'including pricing, mileage and vehicle characteristics.'
)

car_data = pd.read_csv('vehicles.csv')


hist_button = st.button('Create Histogram')

if hist_button:
    st.write(
        'Creating a histogram for the vehicle sales advertisement dataset.'
    )

    fig = px.histogram(
        car_data,
        x='odometer',
        title='Vehicle Mileage Distribution'
    )

    st.plotly_chart(fig, use_container_width=True)


build_scatter_plot = st.checkbox('Create Scatter Plot')

if build_scatter_plot:
    st.write(
        'Creating a scatter plot comparing vehicle mileage and price.'
    )

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Vehicle Price vs. Mileage'
    )

    st.plotly_chart(fig, use_container_width=True)
