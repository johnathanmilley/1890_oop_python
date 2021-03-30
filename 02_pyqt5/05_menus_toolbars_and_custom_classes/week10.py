'''
    QMainWindow template with Menu, Toolbar, Statusbar
'''


import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap, QFont, QIcon)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy, QSlider, QSpinBox, QStatusBar, QStyleFactory, QToolBar, QTabWidget, QTextEdit, QVBoxLayout, QWidget)


class Dice:
    ''' Builds a dice layout with connected slot roll_dice '''
    def __init__(self):
        self.dice_layout = QVBoxLayout()
        
        self.roll_label = QLabel("-")
        self.roll_label.setFont(QFont('Times', 100))
        self.roll_label.setAlignment(Qt.AlignCenter)

        self.roll_btn = QPushButton("Roll")
        self.roll_btn.clicked.connect(self.roll_dice)

        self.dice_layout.addWidget(self.roll_label)
        self.dice_layout.addWidget(self.roll_btn)

    def roll_dice(self):
        roll = random.randrange(1, 7)
        self.roll_label.setText(str(roll))

class MainWindow(QMainWindow):
    """Main Window"""
    def __init__(self):
        """Initializer"""
        super().__init__()
        self.setWindowTitle('QMainWindow')

        # QMainWindow requires a central widget
        self._central_widget = QWidget() 
        self.main_layout = QHBoxLayout()
        self._central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self._central_widget)


        self.d1 = Dice()
        d2 = Dice() # note that this one will not work properly (as in class...)
        self.d3 = Dice()

        self.main_layout.addLayout(self.d1.dice_layout)
        self.main_layout.addLayout(d2.dice_layout)
        self.main_layout.addLayout(self.d3.dice_layout)

        # remove these three lines and associated methods if not using
        self._create_menu()
        self._create_tool_bar()

    # Note that the following methods are prefixed by a
    # single underscore. This is a Python convention that 
    # indicates that the method should only be call∏ed inside
    # of the class.
    # For more info: https://dbader.org/blog/meaning-of-underscores-in-python

    def _create_menu(self):
        self.menu = self.menuBar().addMenu('&Menu')
        self.help = self.menuBar().addMenu('&Help')
        
        self.menu.addAction('&Exit', self.close)
        self.help.addAction('&About', self.display_about)

    def _create_tool_bar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _create_status_bar(self):
        status = QStatusBar()
        status.showMessage('I am the Status Bar')
        self.setStatusBar(status)

    def display_about(self):
        """ Create a dialog window with information about the program."""
        about = QDialog(self) # set MainWindow (self) as the parent
        about.setWindowTitle('About')
        # create layout
        # create widgets
        about.exec()


if __name__ == '__main__':
    """Some of the responsibilities of QApplication:
    
    Handling initialization and finalization
    Providing the event loop and event handling
    Handling most of the system-wide and application-wide settings
    Providing access to global information, such as the application’s directory, screen size, and so on
    Parsing common command-line arguments
    Defining the application’s look and feel
    Providing localization capabilities
    """
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec()) # start application event loop
