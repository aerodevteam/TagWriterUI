from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MainScreen(QWidget):
    def __init__(self, switch_to_complete, switch_to_home):
        super().__init__()
        self.switch_to_home = switch_to_home

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Card Layout (Main Container)
        card_layout = QVBoxLayout()
        card_widget = QWidget()
        card_widget.setStyleSheet("""
            QWidget {
                background: #ffffff; /* White background */
                border-radius: 25px;
                padding: 20px;
                border: 2px solid #cccccc;
            }
        """)
        card_widget.setLayout(card_layout)

        # Airline Logo and Title
        header_layout = QVBoxLayout()
        airline_logo = QLabel()
        airline_logo_pixmap = QPixmap("resources/icons/airplanelogo.png").scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        if airline_logo_pixmap.isNull():
            print("Airline logo image not loaded")
        airline_logo.setPixmap(airline_logo_pixmap)
        airline_logo.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(airline_logo)

        title = QLabel("Passenger Information")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #333333; margin: 10px 0;")
        header_layout.addWidget(title)
        card_layout.addLayout(header_layout)

        # Separator Line
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: #cccccc; margin: 10px 0;")
        card_layout.addWidget(separator)

        # Flight Info (GUJ -> MUM)
        flight_info_layout = QHBoxLayout()
        flight_info_layout.setSpacing(40)

        from_label = QLabel("<b>GUJ</b><br><span style='color:#888888;'>Gujarat</span>")
        from_label.setAlignment(Qt.AlignCenter)
        from_label.setStyleSheet("font-size: 16px;")
        flight_info_layout.addWidget(from_label)

        airplane_icon = QLabel()
        airplane_icon_pixmap = QPixmap("resources/icons/airplane.png").scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        if airplane_icon_pixmap.isNull():
            print("Airplane icon image not loaded")
        airplane_icon.setPixmap(airplane_icon_pixmap)
        airplane_icon.setAlignment(Qt.AlignCenter)
        flight_info_layout.addWidget(airplane_icon)

        to_label = QLabel("<b>MUM</b><br><span style='color:#888888;'>Mumbai</span>")
        to_label.setAlignment(Qt.AlignCenter)
        to_label.setStyleSheet("font-size: 16px;")
        flight_info_layout.addWidget(to_label)

        card_layout.addLayout(flight_info_layout)

        # Passenger Details
        passenger_details_layout = QHBoxLayout()

        left_details = QLabel("""
        <b>Passenger Name:</b> Anna Berlin<br>
        <b>Flight No.:</b> MI0987<br>
        <b>PNR:</b> 3645732476
        """)
        left_details.setStyleSheet("font-size: 14px; color: #444444;")
        left_details.setAlignment(Qt.AlignLeft)

        right_details = QLabel("""
        <b>Departure Time:</b> 9:00 pm<br>
        <b>Boarding Gate:</b> Gate - 3
        """)
        right_details.setStyleSheet("font-size: 14px; color: #444444;")
        right_details.setAlignment(Qt.AlignLeft)

        passenger_details_layout.addWidget(left_details)
        passenger_details_layout.addWidget(right_details)
        card_layout.addLayout(passenger_details_layout)

        # Activate Button
        activate_button = QPushButton("Activate Tag")
        activate_button.setStyleSheet("""
            QPushButton {
                background-color: #FFD700; /* Yellow background */
                color: #000000; /* Black text */
                font-size: 18px;
                font-weight: bold;
                padding: 15px;
                border-radius: 20px;
                margin: 20px 0;
            }
            QPushButton:hover {
                background-color: #FFCC00; /* Darker yellow */
            }
        """)
        activate_button.clicked.connect(switch_to_complete)
        card_layout.addWidget(activate_button)

        # Add card to main layout
        main_layout.addWidget(card_widget)

        self.setLayout(main_layout)



    def retranslate_ui(self, translator, target_language):
        self.label.setText(translator.translate("Passenger Information", dest=target_language).text)
        self.text_edit.setPlaceholderText(
            translator.translate("Name:\nFrom:\nTo:\nFlight No.:\nPNR:\nDeparture Time:\nBoarding Gate:\nAirline:", dest=target_language).text
        )
        self.activate_button.setText(translator.translate("Activate Tag", dest=target_language).text)

