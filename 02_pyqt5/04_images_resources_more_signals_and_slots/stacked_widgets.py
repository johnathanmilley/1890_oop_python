""" Purpose: To demonstrate the QStackedWiget (and introduce external style sheets)    

    John Milley
"""

from functools import partial
import resources
import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QSlider,
                                QStackedWidget, QStatusBar, QToolBar, QVBoxLayout, QWidget)


class StackedWidgets(QMainWindow):
    """Main Window"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle('QMainWindow')
        self.setFixedSize(250, 250)
        
        # This method of getting the system path will be compatible on all OS
        current_dir = os.path.dirname(os.path.abspath(__file__))
        styles = os.path.join(current_dir, 'styles.css')
        with open(styles, 'r') as f:
            # Use external stylesheet
            self.setStyleSheet(f.read())

        # Create the stack (think of a stack of cards, each card is a view or a difference screen)
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        self.screen_1 = QWidget()
        self.screen_1.setObjectName("screen_1") # refer as QWidget#screen_1 in stylesheet
        self.screen_1_layout = QVBoxLayout()
        self.screen_1.setLayout(self.screen_1_layout)
        self.screen_1_label = QLabel('SCREEN 1')
        self.screen_1_layout.addWidget(self.screen_1_label)

        self.screen_2 = QWidget()
        self.screen_2.setObjectName("screen_2") # QWidget#screen_2
        self.screen_2_layout = QVBoxLayout()
        self.screen_2.setLayout(self.screen_2_layout)
        self.screen_2_label = QLabel("SCREEN 2")
        self.screen_2_layout.addWidget(self.screen_2_label)

        # QStackWidgets can be accessed using an index
        self.stack.addWidget(self.screen_1) # i = 0
        self.stack.addWidget(self.screen_2) # i = 1

        self._create_menu()
        self._create_tool_bar()

    # Note that the following methods are prefixed by a
    # single underscore. This is a Python convention that 
    # indicates that the method should only be call∏ed inside
    # of the class. It has no other effect.
    # For more info: https://dbader.org/blog/meaning-of-underscores-in-python

    def _create_menu(self):
        self.menu = self.menuBar().addMenu('&Menu')
        self.screen = self.menuBar().addMenu('&Screen')
        # setNativeMenuBar(False) necessary for macOS
        # self.menuBar().setNativeMenuBar(False) 
        self.menu.addAction('&Exit', self.close)
        self.screen.addAction('1', partial(self.show_screen, 0))
        self.screen.addAction('2', partial(self.show_screen, 1))
    
    def _create_tool_bar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('1', partial(self.show_screen, 0))
        tools.addAction('2', partial(self.show_screen, 1))

    def show_screen(self, i):
        self.stack.setCurrentIndex(i)

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
    win = StackedWidgets()
    win.show()
    sys.exit(app.exec()) # start application event loop
