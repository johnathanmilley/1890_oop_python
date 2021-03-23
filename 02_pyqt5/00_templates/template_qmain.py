'''
    QMainWindow template with Menu, Toolbar, Statusbar
'''

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap, QFont, QIcon)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy, QSlider, QSpinBox, QStatusBar, QStyleFactory, QToolBar, QTabWidget, QTextEdit, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    """Main Window"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle('QMainWindow')
        self._central_widget = QWidget() # QMainWindow requires a central widget
        self.main_layout = QVBoxLayout()
        self._central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self._central_widget)

        
        # remove these three lines and associated methods if not using
        self._create_menu()
        self._create_tool_bar()
        self._create_status_bar()

    # Note that the following methods are prefixed by a
    # single underscore. This is a Python convention that 
    # indicates that the method should only be call∏ed inside
    # of the class.
    # For more info: https://dbader.org/blog/meaning-of-underscores-in-python

    def _create_menu(self):
        self.menu = self.menuBar().addMenu('&Menu')
        # setNativeMenuBar(False) necessary for macOS
        # self.menuBar().setNativeMenuBar(False) 
        self.menu.addAction('&Exit', self.close)

    def _create_tool_bar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _create_status_bar(self):
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
    win = MainWindow()
    win.show()
    sys.exit(app.exec()) # start application event loop
