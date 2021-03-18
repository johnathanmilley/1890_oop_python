""" Purpose: To provide an example of adding images using a compiled qresource file.

    Images shamelessly stolen to quickly develop an educational tool (...sorry)

    Files needed to run:
        adding_images.py
        resources.qrc
        icons/
            windows.png
            linux.png
        images/
            linux_win.jpg
            ms_loves_linux.png
            windows_v_linux.jpg
            windows_win.jpg

    Compile instructions:
        pyrcc5 resources.qrc -o resources.py

        Note: to run pyrcc5, the python Scripts folder must be a part of the PATH environment variable

    John Milley
"""

import resources
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap, QFont, QIcon)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

class WindowsVersusLinux(QDialog):
    def __init__(self):
        super().__init__()

        # Creating and setting the main layout for this Dialog window
        self.main_layout = QVBoxLayout()
        self.setWindowTitle('OS Battle: Windows vs. Linux')
        self.setLayout(self.main_layout)

        # Header Picture
        self.header = QLabel()
        self.win_v_linux = QPixmap(':/images/windows_v_linux.jpg') # :/ indicates a resource path
        self.header.setPixmap(self.win_v_linux)

        # Adding Icons to Radio Buttons
        self.radio_group = QGroupBox("Who will win?")
        self.radio_layout = QVBoxLayout()

        self.win_radio = QRadioButton("Windows")
        self.win_icon = QIcon(':/icons/windows.png')
        self.win_radio.setIcon(self.win_icon)

        self.linux_radio = QRadioButton("Linux")
        self.linux_icon = QIcon(':/icons/linux.png')
        self.linux_radio.setIcon(self.linux_icon)

        self.both_radio = QRadioButton("Why not both?")

        self.win_radio.toggled.connect(self.windows_wins)
        self.linux_radio.toggled.connect(self.linux_wins)
        self.both_radio.toggled.connect(self.both_win)

        self.radio_layout.addWidget(self.win_radio)
        self.radio_layout.addWidget(self.linux_radio)
        self.radio_layout.addWidget(self.both_radio)

        self.radio_group.setLayout(self.radio_layout)

        # Winner Label
        self.winner_label = QLabel()

        self.main_layout.addWidget(self.header)
        self.main_layout.addWidget(self.radio_group)
        self.main_layout.addWidget(self.winner_label)

    def windows_wins(self):
        self.winner_img = QPixmap(':/images/windows_win.jpg')
        self.winner_label.setPixmap(self.winner_img)
    
    def linux_wins(self):
        self.winner_img = QPixmap(':/images/linux_win.jpg')
        self.winner_label.setPixmap(self.winner_img)

    def both_win(self):
        self.winner_img = QPixmap(':/images/ms_loves_linux.png')
        self.winner_label.setPixmap(self.winner_img)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widgets = WindowsVersusLinux()
    widgets.show()
    sys.exit(app.exec_()) 