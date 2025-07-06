# StockSense: AI Demand Forecasting Tool

## Overview
StockSense is an AI-powered demand forecasting tool designed for small retailers. Using Facebook's Prophet model, it predicts future product demand based on historical sales data. The goal is to help shopkeepers make smarter inventory decisions without requiring deep technical skills.

## Features
- Upload your sales CSV file  
- Automatically detects products and forecasts each one  
- Uses AI (Prophet) to predict the next 30 days of demand  
- Interactive line charts comparing actual and predicted sales  
- Downloadable forecast as CSV  
- Supports multiple products (e.g., Milk, Eggs, Curd, etc.)  
- Runs locally with no internet or cloud dependency  

## Inspiration
Many small vendors rely on gut instinct for restocking, leading to overstocking or understocking. We wanted to bring the power of AI demand forecasting—usually available only to big companies—to every local shop in a simple and affordable way.

## How We Built It
- Used Python and Streamlit for the app interface  
- Integrated Facebook Prophet for time-series forecasting  
- Created a custom CSV dataset with 7 products over 30 days  
- Built interactive visualizations using Plotly  

## BuiltWith
- Python3.11  
- FacebookProphet fortimeseriesforecasting  
- Streamlit forwebappinterface  
- Pandas fordatahandling  
- Plotly forvisualizations  
- LocalCSVdataset with7productsand30daysofsales  
- Runslocally viaStreamlitinbrowser  

## Challenges
- Cleaning and reshaping time-series data  
- Supporting multiple products in a single dataset  
- Making AI accessible and usable through a no-code interface  

## What's Next
- Add Firebase integration for cloud storage  
- Send forecast summaries via email  
- Add OCR to extract product sales from printed bills  
- Build a simple mobile app interface  

## How to Run
1. Install Python 3.11  
2. Install the required libraries by running:
3. Place your CSV file (e.g., `milk_sales.csv`) in the same folder as `app.py`.  
4. Run the app using Streamlit:
5. A browser window will open. Select the product and view its AI-powered forecast.

## License
This project is open-source and free to use for educational and demo purposes.


  
