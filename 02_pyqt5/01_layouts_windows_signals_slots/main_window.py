# Filename: main_window.py

"""Main Window-Style application."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar

class Window(QMainWindow):
    """Main Window"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle('QMainWindow')
        self.setCentralWidget(QLabel('I am the Central Widget'))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    # Note that the following methods are prefixed by a
    # single underscore. This is a Python convention that 
    # indicates that the method should only be call∏ed inside
    # of the class. It has no other effect.
    # For more info: https://dbader.org/blog/meaning-of-underscores-in-python

    def _createMenu(self):
        self.menu = self.menuBar().addMenu('&Menu')
        # setNativeMenuBar(False) necessary for macOS
        # self.menuBar().setNativeMenuBar(False) 
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage('I am the Status Bar')
        self.setStatusBar(status)


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
    win = Window()
    win.show()
    sys.exit(app.exec()) # start application event loop
