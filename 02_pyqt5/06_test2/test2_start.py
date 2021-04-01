'''
    CP1890: Test 2 Template File
'''

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator # (optional)
from PyQt5.QtWidgets import (
                                QApplication, QCheckBox, QComboBox, QDialog,
                                QFormLayout, QGridLayout, QGroupBox, 
                                QHBoxLayout, QLabel, QLineEdit, QPushButton,
                                QStyleFactory,  QTextEdit, QVBoxLayout, QWidget
                            )


class HotDogSurvey(QDialog):
    """A very serious survey of user's hot dog eating habits"""
    def __init__(self, parent=None):
        """This init builds the survey window"""
        super().__init__(parent)
        self.setWindowTitle('Hot Dog Survey')
        self.main_layout = QVBoxLayout()


       

        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = HotDogSurvey()
    dlg.show()
    sys.exit(app.exec_())
