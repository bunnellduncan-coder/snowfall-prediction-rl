import random
import pandas as pd

def generate_synthetic_weather_data(num_samples=1000):
    dates = pd.date_range(start='2026-01-01', periods=num_samples, freq='H')
    temperatures = [random.uniform(-10, 35) for _ in range(num_samples)]  # Random temperature between -10 and 35 °C
    humidity = [random.uniform(0, 100) for _ in range(num_samples)]        # Random humidity between 0 and 100%
    precipitation = [random.uniform(0, 20) for _ in range(num_samples)]    # Random precipitation in mm

    weather_data = pd.DataFrame({
        'Date': dates,
        'Temperature (°C)': temperatures,
        'Humidity (%)': humidity,
        'Precipitation (mm)': precipitation
    })
    return weather_data

if __name__ == '__main__':
    data = generate_synthetic_weather_data()
    print(data)