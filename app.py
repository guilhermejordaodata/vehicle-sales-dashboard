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

st.sidebar.header('Filters')

vehicle_types = sorted(car_data['type'].dropna().unique())
conditions = sorted(car_data['condition'].dropna().unique())

selected_types = st.sidebar.multiselect(
    'Vehicle Type',
    options=vehicle_types,
    default=vehicle_types
)

selected_conditions = st.sidebar.multiselect(
    'Condition',
    options=conditions,
    default=conditions
)

filtered_data = car_data[
    (car_data['type'].isin(selected_types)) &
    (car_data['condition'].isin(selected_conditions))
]

st.subheader('Dataset Overview')

total_listings = len(filtered_data)
median_price = filtered_data['price'].median()
median_mileage = filtered_data['odometer'].median()

if filtered_data.empty:
    st.warning('No vehicles match the selected filters.')
    st.stop()

col1, col2, col3 = st.columns(3)

col1.metric(
    'Total Listings',
    f'{total_listings:,}'
)

col2.metric(
    'Median Price',
    f'${median_price:,.0f}'
)

col3.metric(
    'Median Mileage',
    f'{median_mileage:,.0f}'
)



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
