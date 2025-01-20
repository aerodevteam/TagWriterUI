from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox

class LandingScreen(QWidget):
    def __init__(self, switch_to_main, change_language):
        super().__init__()
        self.change_language_callback = change_language

        layout = QVBoxLayout()

        self.label = QLabel("Aerofoyl Technologies")
        self.label.setStyleSheet("font-size: 24px; color: purple;")
        layout.addWidget(self.label)

        self.insert_tag_button = QPushButton("Insert TAG")
        self.insert_tag_button.clicked.connect(switch_to_main)
        layout.addWidget(self.insert_tag_button)

        self.language_selector = QComboBox()
        self.language_selector.addItems(["English", "Hindi"])
        self.language_selector.currentIndexChanged.connect(self.language_changed)
        layout.addWidget(self.language_selector)

        self.setLayout(layout)

    def language_changed(self):
        selected_language = self.language_selector.currentText()
        self.change_language_callback(selected_language)

    def retranslate_ui(self, translator, target_language):
        self.label.setText(translator.translate("Aerofoyl Technologies", dest=target_language).text)
        self.insert_tag_button.setText(translator.translate("Insert TAG", dest=target_language).text)
        self.language_selector.setItemText(0, translator.translate("English", dest=target_language).text)
        self.language_selector.setItemText(1, translator.translate("Hindi", dest=target_language).text)
