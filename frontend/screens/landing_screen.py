from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor

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

    def paintEvent(self, event):
        """
        Draw a semi-transparent rounded-corner box in the background,
        behind all other widgets.
        """
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        # Choose any color and alpha (transparency)
        box_color = QColor(159, 178, 252, 73)  # (R, G, B, Alpha=120)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(box_color))

        # For example: a box at 50% of current width/height, centered
         # Define exact position and size as needed
        box_x = 30
        box_y = 20
        box_width = int(self.width() * 0.9)   # 50% of widget width
        box_height = int(self.height() * 0.9) # 50% of widget height

        corner_radius = 20
        painter.drawRoundedRect(box_x, box_y, box_width, box_height,corner_radius, corner_radius)


        # Rounded corners
        corner_radius = 20
        painter.drawRoundedRect(box_x, box_y, box_width, box_height, corner_radius, corner_radius)
