from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton

class MainScreen(QWidget):
    def __init__(self, switch_to_complete, switch_to_home):
        super().__init__()
        self.switch_to_home = switch_to_home

        layout = QVBoxLayout()

        self.label = QLabel("Passenger Information")
        self.label.setStyleSheet("font-size: 24px; color: purple;")
        layout.addWidget(self.label)

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText(
            "Name:\nFrom:\nTo:\nFlight No.:\nPNR:\nDeparture Time:\nBoarding Gate:\nAirline:"
        )
        layout.addWidget(self.text_edit)

        self.write_tag_button = QPushButton("Write tag")
        self.write_tag_button.clicked.connect(switch_to_complete)
        layout.addWidget(self.write_tag_button)

        self.clear_button = QPushButton("Clear tag")
        self.clear_button.clicked.connect(self.clear_fields)
        layout.addWidget(self.clear_button)

        self.exit_button = QPushButton("EXIT")
        self.exit_button.clicked.connect(self.close_application)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

    def clear_fields(self):
        self.text_edit.clear()

    def close_application(self):
        self.switch_to_home()

    def retranslate_ui(self, translator, target_language):
        self.label.setText(translator.translate("Passenger Information", dest=target_language).text)
        self.text_edit.setPlaceholderText(
            translator.translate("Name:\nFrom:\nTo:\nFlight No.:\nPNR:\nDeparture Time:\nBoarding Gate:\nAirline:", dest=target_language).text
        )
        self.write_tag_button.setText(translator.translate("Write tag", dest=target_language).text)
        self.clear_button.setText(translator.translate("Clear tag", dest=target_language).text)
        self.exit_button.setText(translator.translate("EXIT", dest=target_language).text)
