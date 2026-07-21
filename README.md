# 🌦️ Weather App

This is a simple weather application I built using **Python** and **PyQt5**. The app lets users search for the current weather in any city by using the **OpenWeatherMap API**. It displays the temperature, weather condition, humidity, wind speed, and even shows an emoji that matches the current weather.

I created this project to practice building desktop applications with Python, working with APIs, and designing graphical user interfaces using PyQt5.

---

## Features

* Search for the current weather by entering a city name
* Switch between **Celsius (°C)** and **Fahrenheit (°F)**
* Display the current weather condition
* Show a weather emoji based on the weather type
* Display humidity and wind speed
* Handle invalid city names and network errors gracefully
* Clean and easy-to-use interface

---

## Built With

* Python 3
* PyQt5
* Requests
* OpenWeatherMap API

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

### Install the required packages

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install PyQt5 requests
```

---

## Setting Up the API Key

This project uses the OpenWeatherMap API.

1. Create a free account on OpenWeatherMap.
2. Generate an API key.
3. Open the Python file and replace:

```python
api_key = "Replace with your API key"
```

with your own API key:

```python
api_key = "YOUR_API_KEY"
```

---

## Running the Project

After installing the required packages and adding your API key, run the program with:

```bash
python weather.py
```

---

## How It Works

1. Enter the name of a city.
2. Click **Get Weather**.
3. The app sends a request to the OpenWeatherMap API.
4. The weather information is displayed on the screen.
5. You can switch between Celsius and Fahrenheit without making another API request.

---

## What I Learned

Working on this project helped me improve my understanding of:

* Building desktop applications with PyQt5
* Working with REST APIs
* Sending HTTP requests using the Requests library
* Reading and processing JSON data
* Using object-oriented programming in Python
* Handling exceptions and user input
* Creating a simple and responsive user interface

---

## Future Improvements

There are a few features I would like to add in the future:

* Display weather icons instead of emojis
* Show the "feels like" temperature
* Display sunrise and sunset times
* Add a 5-day weather forecast
* Save recent searches
* Add dark mode
* Automatically detect the user's location

---

## Author

Created by **Duy Nhat Le**.

This project is part of my journey to improve my Python programming skills and learn more about desktop application development. If you have any suggestions or ideas for improvement, feel free to open an issue or submit a pull request.

If you found this project helpful, I'd really appreciate a ⭐ on the repository!
