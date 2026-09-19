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

st.subheader('Mileage Distribution')

exclude_mileage_outliers = st.checkbox(
    'Limit mileage to the 99th percentile',
    value=True
)

mileage_data = filtered_data.copy()

if exclude_mileage_outliers:
    mileage_99 = mileage_data['odometer'].quantile(0.99)

    mileage_data = mileage_data[
        mileage_data['odometer'] <= mileage_99
    ]

fig_mileage = px.histogram(
    mileage_data,
    x='odometer',
    nbins=50,
    title='Distribution of Vehicle Mileage',
    labels={'odometer': 'Mileage'}
)

st.plotly_chart(
    fig_mileage,
    use_container_width=True
)

st.subheader('Price vs. Mileage')

limit_scatter_outliers = st.checkbox(
    'Limit price and mileage to the 99th percentile',
    value=True
)

scatter_data = filtered_data.copy()

if limit_scatter_outliers:
    price_99 = scatter_data['price'].quantile(0.99)
    odometer_99 = scatter_data['odometer'].quantile(0.99)

    scatter_data = scatter_data[
        (scatter_data['price'] <= price_99) &
        (scatter_data['odometer'] <= odometer_99)
    ]

fig_scatter = px.scatter(
    scatter_data,
    x='odometer',
    y='price',
    title='Vehicle Price vs. Mileage',
    labels={
        'odometer': 'Mileage',
        'price': 'Price'
    },
    hover_data=[
        'model',
        'model_year',
        'condition',
        'type'
    ],
    opacity=0.5
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

st.subheader('Median Price by Vehicle Type')

median_price_by_type = (
    filtered_data
    .groupby('type')['price']
    .median()
    .sort_values(ascending=False)
    .reset_index()
)

fig_type = px.bar(
    median_price_by_type,
    x='type',
    y='price',
    title='Median Vehicle Price by Type',
    labels={
        'type': 'Vehicle Type',
        'price': 'Median Price'
    }
)

st.plotly_chart(
    fig_type,
    use_container_width=True
)
