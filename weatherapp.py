import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.humidity_label = QLabel(self)
        self.wind_speed_label = QLabel(self)
        self.unit_toggle_button = QPushButton("Switch to Fahrenheit", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addWidget(self.city_input)
        hbox.addWidget(self.get_weather_button)

        vbox.addWidget(self.city_label)
        vbox.addLayout(hbox)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        vbox.addWidget(self.humidity_label)
        vbox.addWidget(self.wind_speed_label)
        vbox.addWidget(self.unit_toggle_button)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.humidity_label.setAlignment(Qt.AlignCenter)
        self.wind_speed_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.humidity_label.setObjectName("humidity_label")
        self.wind_speed_label.setObjectName("wind_speed_label")
        self.unit_toggle_button.setObjectName("unit_toggle_button")

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: calibri;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
            }
            QPushButton#get_weather_button, QPushButton#unit_toggle_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label, QLabel#humidity_label, QLabel#wind_speed_label {
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)
        self.unit_toggle_button.clicked.connect(self.toggle_unit)

        self.is_celsius = True

    def toggle_unit(self):
        self.is_celsius = not self.is_celsius
        self.unit_toggle_button.setText("Switch to Fahrenheit" if self.is_celsius else "Switch to Celsius")
        if hasattr(self, "last_weather_data"):
            self.display_weather(self.last_weather_data)

    def get_weather(self):
        api_key = "Replace with your API key"   
        city = self.city_input.text().strip()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.last_weather_data = data
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            self.display_error(f"HTTP error occurred: {http_error}")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error: {req_error}")

    def display_error(self, message):
        QMessageBox.critical(self, "Error", message)

    def display_weather(self, data):
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = temperature_c * 9/5 + 32
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        temperature = temperature_c if self.is_celsius else temperature_f
        unit = "°C" if self.is_celsius else "°F"

        self.temperature_label.setText(f"{temperature:.0f}{unit}")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description.capitalize())
        self.humidity_label.setText(f"Humidity: {humidity}%")
        self.wind_speed_label.setText(f"Wind Speed: {wind_speed} m/s")

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())