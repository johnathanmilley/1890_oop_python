""" Purpose: Another example using signals+slots

    John Milley
"""

import resources
import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QVBoxLayout)

class RandomRoll(QDialog):
    def __init__(self):
        super().__init__()

        # Creating and setting the main layout for this Dialog window
        self.setWindowTitle('Random Roll')
        self.setStyleSheet('background-color: black;')
        
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.roll_label = QLabel("-")
        self.roll_label.setFont(QFont('Monospace', 40))
        self.roll_label.setAlignment(Qt.AlignCenter)
        self.roll_label.setStyleSheet('color: white;')

        self.roll_btn = QPushButton("Roll")
        self.roll_btn.clicked.connect(self.roll_dice)
        self.roll_btn.setStyleSheet('background-color: white;')

        self.main_layout.addWidget(self.roll_label)
        self.main_layout.addWidget(self.roll_btn)

    def roll_dice(self):
        self.roll_label.setText(str(random.randrange(1, 7)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widgets = RandomRoll()
    widgets.show()
    sys.exit(app.exec_()) 