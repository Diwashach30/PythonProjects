## creta a weather app using GUI 

import tkinter as tk
from tkinter import messagebox
from tkinter import *
import requests

# Initialize the window
window = tk.Tk()
window.title("Weather App")
window.config(padx=50, pady=50)

# Function to get the weather data
def get_weather():
    # Get the city name from the user input
    city = entry.get()
    api_key = "YOUR_API_KEY"  # Replace this with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        # Send GET request to the OpenWeatherMap API
        response = requests.get(url)
        
        # Check if the response status code is 200 (successful)
        if response.status_code == 200:
            data = response.json()
            
            # Extract relevant weather information from the JSON response
            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            description = data["weather"][0]["description"]
            pressure = data["main"]["pressure"]
            visibility = data["visibility"]
            
            # Format the information to display in the result_label
            result = (
                f"City: {city_name}, {country}\n"
                f"Temperature: {temperature:.2f}°C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s\n"
                f"Description: {description}\n"
                f"Pressure: {pressure} hPa\n"
                f"Visibility: {visibility} meters"
            )
            
            # Update the result_label with the weather data
            result_label.config(text=result)
        
        else:
            # Handle errors like city not found or invalid API key
            error_message = response.json().get("message", "An unknown error occurred.")
            messagebox.showerror("Error", f"Failed to retrieve data: {error_message}")
    
    except requests.exceptions.RequestException as e:
        # Handle network or other request-related errors
        messagebox.showerror("Error", f"An error occurred while fetching data: {e}")

# Create the UI components
label = Label(window, text="Enter the city name:")
label.pack()

entry = Entry(window)
entry.pack()

button = Button(window, text="Get Weather", command=get_weather)
button.pack()

result_label = Label(window, text="")
result_label.pack()

# Run the Tkinter main loop
window.mainloop()

