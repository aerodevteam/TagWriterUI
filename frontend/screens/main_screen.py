from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QHBoxLayout, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class MainScreen(QWidget):
    def __init__(self, switch_to_complete, switch_to_home, data=None):
        super().__init__()
        self.switch_to_home = switch_to_home
        self.switch_to_complete = switch_to_complete
        print("piyush",data)
        
        
        
                # Extract data from the JSON
        flight_details = data.get("flightDetails", {}) if data else {}
        first_name = data.get("firstName", "N/A")
        last_name = data.get("lastName", "N/A")
        full_name = f"{first_name} {last_name}"
        pnr = flight_details.get("pnrNo", "N/A")
        flight_number = flight_details.get("flightNumber", "N/A")
        departure_time = flight_details.get("departureTime", "N/A")
        terminal = flight_details.get("terminal", "N/A")
        from_location = flight_details.get("from", "N/A")
        to_location = flight_details.get("to", "N/A")
        date = flight_details.get("date", "N/A").split("T")[0]  
        
        
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)  # Adjusted margins
        main_layout.setSpacing(5)  # Reduced spacing between elements

        # Add Background Image
        self.bg_label = QLabel(self)
        self.bg_label.setPixmap(QPixmap("resources/Group2.png"))
        self.bg_label.setScaledContents(True)
        self.bg_label.setAlignment(Qt.AlignCenter)
        self.bg_label.setStyleSheet("border: none;")
        self.bg_label.setGeometry(0, 0, self.width(), self.height())  # Ensure full-screen background

        # Spacer for image space (slightly reduced height)
        top_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)
        main_layout.addSpacerItem(top_spacer)

        # Circle Widget
        circle_widget = QLabel()
        circle_widget.setFixedSize(100, 100)  # Fixed size for the circle
        circle_widget.setStyleSheet("""
            QLabel {
                background-color: #CCCCCC; 
                border-radius: 50px;        
            }
        """)
        circle_widget.setAlignment(Qt.AlignCenter)
        circle_widget.setPixmap(
            QPixmap("resources/icons/airplanelogo.png").scaled(60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        # Centered Box Layout
        box_widget = QWidget()
        box_widget.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF; 
                border-radius: 20px;        
                padding: 15px;  /* Reduced padding */
            }
        """)
        box_widget.setFixedSize(420, 600)  # Adjusted height of the box

        # Box Content
        box_layout = QVBoxLayout()
        box_layout.setSpacing(5)  # Reduced spacing between elements inside the box
        box_widget.setLayout(box_layout)

        # Add Plane Image
        plane_image = QLabel()
        plane_image.setPixmap(
            QPixmap("resources/icons/airplane.png").scaled(300, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )
        plane_image.setAlignment(Qt.AlignCenter)
        box_layout.addWidget(plane_image)

        # Title
        title_label = QLabel("Passenger Information")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #333333;")
        box_layout.addWidget(title_label)

        # Flight Info (Date + GUJ -> MUM)
        flight_info_layout = QVBoxLayout()
        flight_info_layout.setSpacing(3)  # Reduced spacing between rows
        flight_info_layout.setContentsMargins(0, 5, 0, 5)

        # GUJ -> MUM Layout
        guj_mum_layout = QHBoxLayout()
        guj_mum_layout.setSpacing(5)

        # From Date and Location
        from_layout = QVBoxLayout()
        from_date = QLabel("<span style='font-size:12px; color:#555555;'>Mon 15 Jul</span>")
        from_date.setAlignment(Qt.AlignCenter)
        from_location = QLabel(f"<b style='font-size:25px; letter-spacing:3px;'>GUJ</b><br><span style='font-size:12px; color:#888888;'>{from_location}</span>")
        from_location.setAlignment(Qt.AlignCenter)
        from_layout.addWidget(from_date)
        from_layout.addWidget(from_location)
        guj_mum_layout.addLayout(from_layout)

        # Airplane Icon
        airplane_layout = QVBoxLayout()
        airplane_icon = QLabel()
        airplane_icon.setPixmap(QPixmap("../resources/icons/airplane.png").scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        airplane_icon.setAlignment(Qt.AlignCenter)
        airplane_layout.addWidget(airplane_icon)
        guj_mum_layout.addLayout(airplane_layout)

        # To Date and Location
        to_layout = QVBoxLayout()
        to_date = QLabel("<span style='font-size:12px; color:#555555;'>Mon 15 Jul</span>")
        to_date.setAlignment(Qt.AlignCenter)
        to_location = QLabel(f"<b style='font-size:25px; letter-spacing:3px;'>MUM</b><br><span style='font-size:12px; color:#888888;'>{to_location}</span>")
        to_location.setAlignment(Qt.AlignCenter)
        to_layout.addWidget(to_date)
        to_layout.addWidget(to_location)
        guj_mum_layout.addLayout(to_layout)

        flight_info_layout.addLayout(guj_mum_layout)
        box_layout.addLayout(flight_info_layout)

        # Passenger Name
        name_label = QLabel(f"<b style='font-size:12px; font-weight:500; color:#555555;'>Passenger Name:</b><br><span style='font-size:16px;font-weight:700; letter-spacing:1px;'>{full_name}</span>")
        name_label.setStyleSheet("font-size:14px;")  # Add space below name
        name_label.setAlignment(Qt.AlignLeft)
        box_layout.addWidget(name_label)

       # Details Grid for Other Info
        details_grid = QGridLayout()
        details_grid.setHorizontalSpacing(10)  # Adjust column spacing
        details_grid.setVerticalSpacing(10)    # Add vertical spacing

        # Flight No. and Departure Time
        flight_no = QLabel(f"""
        <b style='font-size:12px; font-weight:500; color:#555555;'>Flight No.:</b><br>
        <span style='font-size:16px; font-weight:700;  margin-top:4px; letter-spacing:1px;'>{flight_number}</span>
        """)

        flight_no.setStyleSheet("font-size:14px;")
        flight_no.setAlignment(Qt.AlignLeft)
        details_grid.addWidget(flight_no, 0, 0)

        departure_time = QLabel(f"""
        <b style='font-size:12px; font-weight:500; color:#555555;'>Departure Time:</b><br>
        <span style='font-size:16px; font-weight:700; letter-spacing:1px;'>{departure_time}</span>
        """)
        departure_time.setStyleSheet("font-size:14px;")
        departure_time.setAlignment(Qt.AlignLeft)
        details_grid.addWidget(departure_time, 0, 1)

        # PNR and Boarding Gate
        pnr_label = QLabel(f"""
        <b style='font-size:12px; font-weight:500; color:#555555;'>PNR:</b><br>
        <span style='font-size:16px; font-weight:700; letter-spacing:1px;'>{pnr}</span>
        """)
        pnr_label.setStyleSheet("font-size:14px; ")
        pnr_label.setAlignment(Qt.AlignLeft)
        details_grid.addWidget(pnr_label, 1, 0)

        boarding_gate = QLabel(f"""
        <b style='font-size:12px; font-weight:500; color:#555555;'>Boarding Gate:</b><br>
        <span style='font-size:16px; font-weight:700; letter-spacing:1px;'>{terminal}</span>
        """)
        boarding_gate.setStyleSheet("font-size:14px;")
        boarding_gate.setAlignment(Qt.AlignLeft)
        details_grid.addWidget(boarding_gate, 1, 1)

        # Add details grid to box layout
        box_layout.addLayout(details_grid)


        # Add Circle and Box Layout
        main_layout.addWidget(circle_widget, alignment=Qt.AlignHCenter)
        main_layout.addWidget(box_widget, alignment=Qt.AlignHCenter)

        # Yellow Button
        button = QPushButton("Activate Tag")
        button.setStyleSheet("""
            QPushButton {
                background-color: #FFD700;
                color: #000000;
                font-size: 16px;
                font-weight: bold;
                padding: 12px;
                border-radius: 10px;
            }
        """)
        button.setFixedSize(300, 80)
        button.clicked.connect(switch_to_complete)
        main_layout.addWidget(button, alignment=Qt.AlignBottom | Qt.AlignHCenter)

        self.setLayout(main_layout)

    def resizeEvent(self, event):
        """Ensure the background image scales dynamically on resize."""
        self.bg_label.setGeometry(0, 0, self.width(), self.height())












    # def resizeEvent(self, event):
    #     """Ensure the background image scales dynamically on resize."""
    #     pixmap = QPixmap("../resources/Group2.png")
    #     if not pixmap.isNull():
    #         self.bg_label.setPixmap(pixmap.scaled(
    #             self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))




    def retranslate_ui(self, translator, target_language):
        self.label.setText(translator.translate("Passenger Information", dest=target_language).text)
        self.text_edit.setPlaceholderText(
            translator.translate("Name:\nFrom:\nTo:\nFlight No.:\nPNR:\nDeparture Time:\nBoarding Gate:\nAirline:", dest=target_language).text
        )
        self.write_tag_button.setText(translator.translate("Write tag", dest=target_language).text)
        self.clear_button.setText(translator.translate("Clear tag", dest=target_language).text)
        self.exit_button.setText(translator.translate("EXIT", dest=target_language).text)
