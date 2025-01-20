import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from screens.landing_screen import LandingScreen
from screens.main_screen import MainScreen
from screens.complete_screen import CompleteScreen
from googletrans import Translator

class AppWindow(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Initialize translator
        self.translator = Translator()
        self.current_language = "en"  # Default language is English

        # Create screens
        self.landing_screen = LandingScreen(self.show_main_screen, self.change_language)
        self.main_screen = MainScreen(self.show_complete_screen, self.show_home_screen)
        self.complete_screen = CompleteScreen(self.show_home_screen)

        # Add screens
        self.addWidget(self.landing_screen)
        self.addWidget(self.main_screen)
        self.addWidget(self.complete_screen)

        # Set the initial screen
        self.setCurrentWidget(self.landing_screen)

    def show_main_screen(self):
        self.setCurrentWidget(self.main_screen)

    def show_complete_screen(self):
        self.setCurrentWidget(self.complete_screen)
        self.complete_screen.start_timer()

    def show_home_screen(self):
        self.setCurrentWidget(self.landing_screen)

    def change_language(self, language):
        # Map language dropdown selection to language codes
        lang_code = {"English": "en", "Hindi": "hi"}.get(language, "en")
        self.current_language = lang_code
        self.retranslate_ui()

    def retranslate_ui(self):
        # Dynamically translate all screens
        for screen in [self.landing_screen, self.main_screen, self.complete_screen]:
            screen.retranslate_ui(self.translator, self.current_language)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = AppWindow()
    window.setWindowTitle("Tag Writer Application")
    window.resize(500, 800)
    window.show()

    sys.exit(app.exec_())
