import requests
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QMessageBox


class LandingScreen(QWidget):
    def __init__(self, switch_to_main, change_language):
        super().__init__()
        self.switch_to_main = switch_to_main
        self.change_language_callback = change_language

        layout = QVBoxLayout()

        # Title Label
        self.label = QLabel("Aerofoyl Technologies")
        self.label.setStyleSheet("font-size: 24px; color: purple;")
        layout.addWidget(self.label)

        # Insert Tag Button
        self.insert_tag_button = QPushButton("Insert TAG")
        self.insert_tag_button.clicked.connect(self.fetch_data_and_switch)
        layout.addWidget(self.insert_tag_button)

        # Language Selector
        self.language_selector = QComboBox()
        self.language_selector.addItems(["English", "Hindi"])
        self.language_selector.currentIndexChanged.connect(self.language_changed)
        layout.addWidget(self.language_selector)

        self.setLayout(layout)

    def language_changed(self):
        """Handle language change."""
        selected_language = self.language_selector.currentText()
        self.change_language_callback(selected_language)

    def fetch_data_and_switch(self):
        """Fetch data from API and pass it to the main screen."""
        # Example payload
        payload = {
            "pnr": "VYI9QO",
            "nameEmail": "piyush"
        }

        try:
            # Call the API
            response = requests.post("https://frontendservers.onrender.com/api/passenger/det/findpax", json=payload)

            if response.status_code == 200:
                data = response.json()
                QMessageBox.information(self, "Success", "Data fetched successfully!", QMessageBox.Ok)
                # Pass data to the main screen
                self.switch_to_main(data)
            else:
                QMessageBox.warning(self, "API Error", f"Error fetching data: {response.status_code}", QMessageBox.Ok)
        except requests.exceptions.RequestException as error:
            QMessageBox.critical(self, "Network Error", f"Error: {error}", QMessageBox.Ok)


    def retranslate_ui(self, translator, target_language):
        self.label.setText(translator.translate("Aerofoyl Technologies", dest=target_language).text)
        self.insert_tag_button.setText(translator.translate("Insert TAG", dest=target_language).text)
        self.language_selector.setItemText(0, translator.translate("English", dest=target_language).text)
        self.language_selector.setItemText(1, translator.translate("Hindi", dest=target_language).text)
