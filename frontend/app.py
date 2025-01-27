import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget, QMessageBox
from screens.landing_screen import LandingScreen
from screens.main_screen import MainScreen
from screens.complete_screen import CompleteScreen

class AppWindow(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Create screens
        self.landing_screen = LandingScreen(self.show_main_screen)
        self.main_screen = None  # Initialize later with data
        self.complete_screen = CompleteScreen(self.show_home_screen)

        # Add screens
        self.addWidget(self.landing_screen)
        self.addWidget(self.complete_screen)

        # Set the initial screen
        self.setCurrentWidget(self.landing_screen)

    def show_main_screen(self, data):
        """Switch to the main screen with the fetched data."""
        # Dynamically initialize MainScreen with data
        self.main_screen = MainScreen(switch_to_complete=self.show_complete_screen, switch_to_home=self.show_home_screen, data=data)
        self.addWidget(self.main_screen)
        self.setCurrentWidget(self.main_screen)

    def show_complete_screen(self):
        """Switch to the complete screen."""
        self.setCurrentWidget(self.complete_screen)
        self.complete_screen.start_timer()

    def show_home_screen(self):
        """Switch back to the landing screen."""
        self.setCurrentWidget(self.landing_screen)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = AppWindow()
    window.setWindowTitle("Tag Writer Application")
    window.resize(500, 800)
    window.show()

    sys.exit(app.exec_())