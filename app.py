import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from prophet import Prophet

def forecast_sales(data, periods=30):
    df = data.rename(columns={'Date': 'ds', 'Units_Sold': 'y'})
    model = Prophet(daily_seasonality=True)
    model.fit(df)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']], model

st.set_page_config(page_title="StockSense", layout="centered")
st.title("📈 StockSense - AI Demand Forecasting")
st.markdown("This app uses AI (Facebook Prophet) to forecast product demand for the next 30 days from your dataset.")

file_path = r"C:\Users\tusha\OneDrive\Desktop\MY WORKING PROJECTS\Stocksense\milk_sales.csv"

try:
    data = pd.read_csv(file_path)
    st.success("✅ Dataset loaded successfully from local path.")
    st.subheader("📄 Loaded Data Preview")
    st.write(data.head())


    if 'Date' not in data.columns or 'Units_Sold' not in data.columns or 'Product' not in data.columns:
        st.error("❌ Your CSV must contain 'Date', 'Product', and 'Units_Sold' columns.")
        st.stop()


    products = data['Product'].unique()
    selected_product = st.selectbox("🔍 Select Product", products)

    product_data = data[data['Product'] == selected_product][['Date', 'Units_Sold']]
    product_data['Date'] = pd.to_datetime(product_data['Date'])

    st.subheader("📊 Forecasted Demand (Next 30 Days)")
    forecast, model = forecast_sales(product_data)

    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=product_data['Date'], y=product_data['Units_Sold'],
                             mode='lines+markers', name='Actual Sales'))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'],
                             mode='lines', name='Forecast'))
    fig.update_layout(title=f"Forecast for: {selected_product}",
                      xaxis_title='Date', yaxis_title='Units Sold')
    st.plotly_chart(fig)

    
    csv = forecast.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Forecast CSV", data=csv,
                       file_name=f'forecast_{selected_product}.csv',
                       mime='text/csv')

except Exception as e:
    st.error(f"⚠️ Error loading dataset: {e}")
    st.info("💡 Make sure the file exists and is not open in Excel.")
