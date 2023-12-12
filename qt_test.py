import sys
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton

sunrise = "7:45 AM"
sunset = "4:19 PM"
    
class MorningRoutineApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Morning Routine App")
        self.setGeometry(100, 100, 800, 400)

        central_widget = QWidget(self)
        layout = QHBoxLayout(central_widget)

        # Set margin around the main layout
        layout.setContentsMargins(100, 100, 100, 100)  # Adjust the values as needed

        # Apply a sunset-themed gradient background
        central_widget.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FF6F61, stop:1 #1A2B50); color: white;")

        # Left side with greeting, weather, and sunrise/sunset
        left_layout = QVBoxLayout()

        greeting_label = QLabel("Good morning, \nCharlotte", self)
        greeting_label.setStyleSheet("font-size: 36px; font-weight: bold; background: None;")
        left_layout.addWidget(greeting_label, alignment=Qt.AlignmentFlag.AlignTop)

        weather_label = QLabel("Weather: Sunny", self)
        weather_label.setStyleSheet("font-size: 18px; background: None;")
        left_layout.addWidget(weather_label)


        sunrise_sunset_label = QLabel(f"\u2600 {sunrise} / {sunset}", self)
        sunrise_sunset_label.setStyleSheet("font-size: 18px; background: None")
        left_layout.addWidget(sunrise_sunset_label)

        # Add left layout to main layout
        layout.addLayout(left_layout)

        # Right side with options
        right_layout = QVBoxLayout()

        options_label = QLabel("Options for the day:", self)
        options_label.setStyleSheet("font-size: 18px; background: None; font-weight: bold; ")
        right_layout.addWidget(options_label)

        # Style for option buttons
        button_style = (
            "QPushButton {"
            "   background-color: rgba(0, 0, 0, 0);"
            "   border: 2px solid white;"
            "   color: white;"
            "   padding: 10px 20px;"
            "   border-radius: 5px;"
            "   font-size: 16px;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgba(255, 255, 255, 0.2);"
            "}"
        )

        brown_noise_button = QPushButton("Play Brown Noise on Spotify", self)
        brown_noise_button.setStyleSheet(button_style)
        right_layout.addWidget(brown_noise_button)

        recipes_button = QPushButton("Get Breakfast Recipe Ideas", self)
        recipes_button.setStyleSheet(button_style)
        right_layout.addWidget(recipes_button)

        walk_button = QPushButton("Plan a Morning Walk", self)
        walk_button.setStyleSheet(button_style)
        right_layout.addWidget(walk_button)

        # Add right layout to main layout
        layout.addLayout(right_layout)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MorningRoutineApp()
    window.show()
    sys.exit(app.exec_())
