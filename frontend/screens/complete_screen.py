from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer

class CompleteScreen(QWidget):
    def __init__(self, switch_to_home):
        super().__init__()
        self.switch_to_home = switch_to_home

        layout = QVBoxLayout()

        self.label = QLabel("Tag written...")
        self.label.setStyleSheet("font-size: 24px; color: red;")
        layout.addWidget(self.label)

        self.success_icon = QLabel("✔")
        self.success_icon.setStyleSheet("font-size: 48px; color: green;")
        layout.addWidget(self.success_icon)

        self.exit_button = QPushButton("EXIT")
        self.exit_button.clicked.connect(self.close_application)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.switch_to_home)

    def start_timer(self):
        self.timer.start()

    def close_application(self):
        self.switch_to_home()

    def retranslate_ui(self, translator, target_language):
        """
        Update all translatable text in the screen dynamically.
        """
        self.label.setText(translator.translate("Tag written...", dest=target_language).text)
        self.exit_button.setText(translator.translate("EXIT", dest=target_language).text)
