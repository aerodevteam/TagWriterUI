from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
import random
import math

class CompleteScreen(QWidget):
    def __init__(self, switch_to_home):
        super().__init__()
        self.switch_to_home = switch_to_home

        # Window size to ensure enough space for animation
        self.setMinimumSize(600, 400)

        # ------------------ EXIT Button (manual placement) ------------------
        self.exit_button = QPushButton("EXIT", self)
        # Make the button bigger
        self.exit_button.setFixedSize(250, 70)
        # Optional: Increase font size for the button text
        self.exit_button.setStyleSheet("""QPushButton {font-size: 23px;background-color: #F6D500;color: #3B3B3B;border-radius: 25px;}""")
        self.exit_button.clicked.connect(self.close_application)

        # ------------------ Labels (manually positioned in paintEvent) ------
        self.label_tag_written = QLabel("THANK YOU", self)
        self.label_tag_written.setAlignment(Qt.AlignCenter)
        self.label_tag_written.setStyleSheet("font-size: 34px; color: #3B3B3B; background-color: transparent;")

        self.label_thank_you = QLabel("Your Tag is Printed", self)
        self.label_thank_you.setAlignment(Qt.AlignCenter)
        self.label_thank_you.setStyleSheet("font-size: 20px; color: #3B3B3B; background-color: transparent;")

        # ------------------ Timers ------------------------------------------
        # 1) Timer to switch away from this screen after ~5 seconds
        self.timer = QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.switch_to_home)

        # 2) Animation timer (~25 FPS)
        self.animation_timer = QTimer(self)
        self.animation_timer.setInterval(20)
        self.animation_timer.timeout.connect(self.update_animation)

        # Animation parameters
        self.frame_count = 0
        self.crackers = []
        self.crackers_created = False

        # Start the animation here, or call start_timer() from outside
        self.animation_timer.start()

    def start_timer(self):
        """
        Reset animation variables each time we arrive on this page,
        and then start the timers.
        """
        self.frame_count = 0
        self.crackers = []
        self.crackers_created = False
        self.animation_timer.start()
        self.timer.start()

    def close_application(self):
        self.switch_to_home()

    def retranslate_ui(self, translator, target_language):
        """
        Example method to dynamically change text based on language.
        """
        self.label_tag_written.setText(translator.translate("THANK YOU", dest=target_language).text)
        self.label_thank_you.setText(translator.translate("Your Tag is Printed", dest=target_language).text)
        self.exit_button.setText(translator.translate("EXIT", dest=target_language).text)

    def update_animation(self):
        """
        Animation frames (runs ~25 times per second).
        """
        self.frame_count += 1

        # Once the circle is partially drawn, create crackers
        if self.frame_count >= 15 and not self.crackers_created:
            self.create_crackers()
            self.crackers_created = True

        if self.crackers_created:
            self.update_crackers()

        # Trigger a repaint
        self.update()

    def create_crackers(self):
        """
        Create small dots in random directions to simulate 'confetti' or 'crackers'.
        """
        num_crackers = 40
        center_x = self.width() // 2
        center_y = (self.height() // 2) - 200
        for _ in range(num_crackers):
            angle = random.random() * 2 * math.pi
            speed = random.uniform(2.0, 6.0)
            size = random.randint(3, 8)
            color = QColor(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            self.crackers.append({
                "x": center_x,
                "y": center_y,
                "vx": math.cos(angle) * speed,
                "vy": math.sin(angle) * speed,
                "size": size,
                "color": color,
                "life": 60
            })

    def update_crackers(self):
        """
        Move the crackers outward and decrease their life.
        """
        for c in self.crackers:
            c["x"] += c["vx"]
            c["y"] += c["vy"]
            c["life"] -= 1
        # Keep only crackers that are alive
        self.crackers = [c for c in self.crackers if c["life"] > 0]

    def paintEvent(self, event):
        """
        Paint the circle, check mark, crackers, and position labels & button accordingly.
        """
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        center_x = self.width() // 2
        center_y = (self.height() // 2) - 200
        
        
        box_color = QColor(159, 178, 252, 73)  # RGBA: red with alpha=120
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(box_color))

        # Define exact position and size as needed
        box_x = 30
        box_y = 20
        box_width = int(self.width() * 0.9)   # 50% of widget width
        box_height = int(self.height() * 0.9) # 50% of widget height

        corner_radius = 20
        painter.drawRoundedRect(box_x, box_y, box_width, box_height,corner_radius, corner_radius)


        # -------------------- Draw Cracker Dots --------------------
        if self.crackers_created:
            for c in self.crackers:
                alpha = max(0, int((c["life"] / 60) * 255))
                color = c["color"]
                color.setAlpha(alpha)
                painter.setBrush(QBrush(color))
                painter.setPen(Qt.NoPen)
                painter.drawEllipse(
                    int(c["x"]),
                    int(c["y"]),
                    int(c["size"]),
                    int(c["size"])
                )

        # -------------------- Draw Growing Circle -------------------
        circle_grow_frames = 10.0
        progress = min(self.frame_count / circle_grow_frames, 1.0)

        max_radius = min(self.width(), self.height()) // 8
        radius = int(max_radius * progress)

        circle_color = QColor(100, 200, 100)  # arbitrary greenish
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(circle_color))
        painter.drawEllipse(center_x - radius, center_y - radius, radius * 2, radius * 2)

        # -------------------- Draw Check Mark -----------------------
        check_start = 10
        check_end = 20
        if self.frame_count > check_start:
            check_progress = min((self.frame_count - check_start) / (check_end - check_start), 1.0)
            painter.setPen(QPen(Qt.white, 10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            p1 = (center_x - radius * 0.4, center_y + radius * 0.1)
            p2 = (center_x - radius * 0.1, center_y + radius * 0.3)
            p3 = (center_x + radius * 0.3, center_y - radius * 0.3)

            segment_progress = check_progress * 2.0

            # First segment
            if segment_progress <= 1.0:
                x_mid = p1[0] + (p2[0] - p1[0]) * segment_progress
                y_mid = p1[1] + (p2[1] - p1[1]) * segment_progress
                painter.drawLine(int(p1[0]), int(p1[1]), int(x_mid), int(y_mid))
            else:
                # full first segment
                painter.drawLine(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
                # partial second segment
                seg2_progress = segment_progress - 1.0
                seg2_progress = min(seg2_progress, 1.0)
                x_mid = p2[0] + (p3[0] - p2[0]) * seg2_progress
                y_mid = p2[1] + (p3[1] - p2[1]) * seg2_progress
                painter.drawLine(int(p2[0]), int(p2[1]), int(x_mid), int(y_mid))

        painter.end()

        # ------------------ Position Labels & Button Below Circle ------------------
        #
        # 1) "THANK YOU"
        self.label_tag_written.adjustSize()
        label_tag_w = self.label_tag_written.width()
        label_tag_h = self.label_tag_written.height()
        vertical_offset = 20

        label_tag_x = center_x - (label_tag_w // 2)
        label_tag_y = (center_y + radius) + vertical_offset
        self.label_tag_written.move(label_tag_x, label_tag_y)

        # 2) "Your Tag is Printed"
        self.label_thank_you.adjustSize()
        label_thank_w = self.label_thank_you.width()
        label_thank_h = self.label_thank_you.height()
        vertical_offset2 = 10

        label_thank_x = center_x - (label_thank_w // 2)
        label_thank_y = label_tag_y + label_tag_h + vertical_offset2
        self.label_thank_you.move(label_thank_x, label_thank_y)

        # 3) EXIT button (directly below “Thank you”)
        # Center it horizontally, offset below the "Thank you"
        button_width = self.exit_button.width()
        button_height = self.exit_button.height()
        vertical_offset_button = 55

        button_x = center_x - (button_width // 2)
        button_y = label_thank_y + label_thank_h + vertical_offset_button
        self.exit_button.move(button_x, button_y)
