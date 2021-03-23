'''
    QStackedWidget Template
'''

import sys
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap, QFont, QIcon)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy, QSlider, QSpinBox, QStackedWidget, QStatusBar, QStyleFactory, QToolBar, QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Dialog(QDialog):
    """Dialog"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle('QDialog')

        # main layout of the QDialog window
        self.main_layout = QVBoxLayout()
        
        # create the stack
        self.stack = QStackedWidget()

        # first widget to add to stack
        self.first = QWidget()
        self.first_layout = QVBoxLayout()
        
        self.first_label = QLabel('Screen 1')
        self.first_button = QPushButton('To Screen 2')
        self.first_button.pressed.connect(partial(self.show_screen, 1))

        self.first_layout.addWidget(self.first_label)
        self.first_layout.addWidget(self.first_button)
        self.first.setLayout(self.first_layout)
        
        # second widget to add to stack
        self.second = QWidget()
        self.second_layout = QVBoxLayout()
        self.second_label = QLabel('Screen 2')
        self.second_button = QPushButton('To Screen 1')
        self.second_button.pressed.connect(partial(self.show_screen, 0))

        self.second_layout.addWidget(self.second_label)
        self.second_layout.addWidget(self.second_button)
        self.second.setLayout(self.second_layout)

        # add first and second widget to the stack
        self.stack.addWidget(self.first)
        self.stack.addWidget(self.second)

        # add the stack to the main layout
        self.main_layout.addWidget(self.stack)

        # set layout of entire window (QDialog)
        self.setLayout(self.main_layout)

    def show_screen(self, screen):
        self.stack.setCurrentIndex(screen)

""" From the docs:

A module’s __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt. (https://docs.python.org/3/library/__main__.html)
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
