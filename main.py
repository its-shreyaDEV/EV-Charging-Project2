# EV Charging Station Geospatial Scatter & Future Demand Forecast
# Author: [Your Name]
# Description:
# Visualizes EV charging stations, usage trends, and predicts future demand.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np
from datetime import datetime

# ---------------------------
# 1. Load Dataset
# ---------------------------
df = pd.read_csv("global_ev_charging_stations.csv")

print("✅ Dataset Loaded Successfully!")
print(df.head())

# ---------------------------
# 2. Clean Data
# ---------------------------
df = df.dropna(subset=['Latitude', 'Longitude'])

usage_columns = [col for col in df.columns if 'usage' in col.lower() or 'kwh' in col.lower() or 'power' in col.lower()]
color_col = usage_columns[0] if usage_columns else None

# ---------------------------
# 3. Geospatial Scatter Plot — Station Distribution
# ---------------------------
plt.figure(figsize=(10, 7))
if color_col:
    sns.scatterplot(
        data=df,
        x='Longitude',
        y='Latitude',
        hue=color_col,
        palette='coolwarm',
        alpha=0.8,
        edgecolor='k'
    )
    plt.title(f"Geospatial Distribution of EV Charging Stations by {color_col}")
    plt.legend(title=color_col)
else:
    sns.scatterplot(
        data=df,
        x='Longitude',
        y='Latitude',
        color='dodgerblue',
        alpha=0.7,
        edgecolor='k'
    )
    plt.title("Geospatial Distribution of EV Charging Stations")

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ---------------------------
# 4. Histogram — Battery Capacity (Optional)
# ---------------------------
battery_columns = [col for col in df.columns if 'battery' in col.lower() or 'capacity' in col.lower()]
if battery_columns:
    battery_col = battery_columns[0]
    plt.figure(figsize=(8, 5))
    sns.histplot(df[battery_col].dropna(), bins=20, kde=True, color='skyblue')
    plt.title(f"Battery Capacity Distribution ({battery_col})")
    plt.xlabel("Battery Capacity (kWh)")
    plt.ylabel("Frequency")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
else:
    print("⚠️ No battery capacity column found. Skipping histogram.")

# ---------------------------
# 5. Future Demand Pattern (Always Visible)
# ---------------------------

# Check if a date or time column exists
time_cols = [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()]

if time_cols and color_col:
    # Use actual dataset trends if possible
    time_col = time_cols[0]
    df[time_col] = pd.to_datetime(df[time_col], errors='coerce')
    df = df.dropna(subset=[time_col, color_col])
    df['Month'] = df[time_col].dt.to_period('M')
    demand_trend = df.groupby('Month')[color_col].mean().reset_index()
    demand_trend['Month'] = demand_trend['Month'].dt.to_timestamp()
else:
    # Generate synthetic trend if missing
    print("⚠️ No date/usage column found. Creating synthetic demand trend for visualization.")
    months = pd.date_range(start='2023-01-01', periods=24, freq='MS')
    np.random.seed(42)
    demand = np.linspace(100, 300, 24) + np.random.randn(24) * 20  # simulated demand growth
    demand_trend = pd.DataFrame({'Month': months, 'Usage_kWh': demand})
    color_col = 'Usage_kWh'

# ---------------------------
# 6. Predict Future Demand
# ---------------------------
demand_trend['TimeIndex'] = np.arange(len(demand_trend))
X = demand_trend[['TimeIndex']]
y = demand_trend[color_col]

model = LinearRegression()
model.fit(X, y)

# Predict next 12 months
future_time_index = np.arange(len(demand_trend), len(demand_trend) + 12)
future_predictions = model.predict(future_time_index.reshape(-1, 1))
future_dates = pd.date_range(demand_trend['Month'].iloc[-1] + pd.offsets.MonthBegin(),
                             periods=12, freq='MS')

forecast_df = pd.DataFrame({
    'Month': future_dates,
    'Predicted_Demand': future_predictions
})

# ---------------------------
# 7. Plot Historical vs Predicted Demand
# ---------------------------
plt.figure(figsize=(10, 6))
plt.plot(demand_trend['Month'], demand_trend[color_col], label='Historical Demand', marker='o')
plt.plot(forecast_df['Month'], forecast_df['Predicted_Demand'], label='Forecasted Demand (Next 12 Months)', linestyle='--', marker='x')
plt.title("Future Demand Pattern for EV Charging Stations")
plt.xlabel("Month")
plt.ylabel("Average Charging Usage (kWh)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()