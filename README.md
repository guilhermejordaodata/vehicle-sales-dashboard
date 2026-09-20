# Vehicle Sales Dashboard

An interactive data dashboard built with Python, Pandas, Plotly and Streamlit to explore vehicle sales advertisement data through exploratory analysis and interactive visualizations.

**Live Demo:** https://web-app-compra-veiculos.onrender.com

## Project Overview

This project was originally developed as part of a practical software engineering project focused on strengthening Python development workflows and complementing data-related skills.

The project was later expanded to include exploratory data analysis (EDA), data quality investigation, descriptive statistics, interactive filtering and additional data visualizations.

The application allows users to explore more than 51,000 vehicle advertisements and investigate relationships between vehicle characteristics, mileage and listing prices.

## Objectives

* Practice Python software development workflows
* Load, inspect and manipulate structured data with Pandas
* Perform exploratory data analysis
* Identify missing values, potential outliers and data quality issues
* Apply descriptive statistics and correlation analysis
* Create interactive visualizations with Plotly
* Build an interactive dashboard with Streamlit
* Implement dynamic filtering of the dataset
* Manage project dependencies and version control
* Deploy a Python web application to a cloud service

## Dataset

The dataset contains **51,525 vehicle advertisements** and 13 variables describing characteristics such as:

* Price
* Model and model year
* Vehicle condition
* Cylinders
* Fuel type
* Mileage
* Transmission
* Vehicle type
* Paint color
* Four-wheel drive status
* Posting date
* Days listed

The exploratory analysis identified missing values in several variables as well as potential extreme values in price and mileage.

## Exploratory Data Analysis

The Jupyter notebook includes:

* Dataset structure inspection
* Missing-value analysis
* Descriptive statistics
* Duplicate-record verification
* Investigation of potential data quality issues
* Quantile analysis
* Investigation of extreme values
* Percentile-based filtering for visualization
* Mileage distribution analysis
* Price vs. mileage analysis
* Pearson correlation analysis
* Grouping and aggregation by vehicle type

The original dataset is preserved during the analysis. Percentile-based filtering is used for selected visualizations to reduce the influence of extreme observations without removing them from the source data.

## Key Findings

* No fully duplicated records were identified.
* Several variables contain missing values, particularly `is_4wd`, `paint_color`, `odometer`, `cylinders` and `model_year`.
* Potential data quality inconsistencies were identified in some model-year values.
* Price and mileage contain extreme observations that can affect visualization and descriptive statistics.
* Vehicle mileage is concentrated primarily within the lower and middle mileage ranges, with a long right tail.
* Price and mileage show a moderate negative linear association, with a Pearson correlation of approximately **-0.42** for the complete dataset.
* After limiting price and mileage to their 99th percentiles, the correlation is approximately **-0.45**.
* Median listing prices vary across vehicle types, indicating that mileage alone does not explain differences in vehicle prices.

These findings describe associations within this dataset and should not be interpreted as causal relationships.

## Interactive Dashboard

The Streamlit application provides:

* Dynamic filtering by vehicle type
* Dynamic filtering by vehicle condition
* Total listing count
* Median vehicle price
* Median vehicle mileage
* Interactive mileage distribution
* Optional 99th-percentile filtering for mileage visualization
* Interactive price vs. mileage scatter plot
* Optional 99th-percentile filtering for price and mileage
* Vehicle details through Plotly hover interactions
* Median price comparison by vehicle type

Dashboard metrics and visualizations automatically respond to the filters selected by the user.

## Technologies

* **Python**
* **Pandas**
* **Plotly**
* **Streamlit**
* **JupyterLab**
* **Git**
* **GitHub**
* **Render**

## Project Structure

```text
vehicle-sales-dashboard/
│
├── app.py
├── vehicles.csv
├── requirements.txt
├── config.toml
├── .gitignore
│
└── notebooks/
    └── EDA.ipynb
```

## Skills Demonstrated

**Programming:** Python

**Data Analysis:** Pandas · Data Manipulation · Exploratory Data Analysis · Descriptive Statistics · Missing-Value Analysis · Quantile Analysis · Correlation · GroupBy & Aggregation

**Data Visualization:** Plotly · Histograms · Scatter Plots · Bar Charts · Interactive Visualizations

**Dashboard Development:** Streamlit · Interactive Filters · Dynamic Metrics

**Development Workflow:** Virtual Environments · Dependency Management · Git · GitHub

**Deployment:** Cloud Application Deployment with Render

## Learning Outcomes

This project provided practical experience across the complete workflow of a small data application: inspecting and exploring a dataset, identifying data quality considerations, interpreting statistical relationships, creating interactive visualizations, building a web interface and deploying the final application.

The project demonstrates the integration of foundational data analysis skills with Python software development and interactive dashboard creation.

## Future Improvements

Potential future developments include:

* Additional filters for model year and price range
* Analysis of price differences by vehicle condition and model year
* Improved handling and documentation of missing values
* Additional statistical analysis of factors associated with vehicle prices
* Further dashboard interface and usability improvements
