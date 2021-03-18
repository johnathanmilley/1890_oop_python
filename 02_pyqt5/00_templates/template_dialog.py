'''
    QDialog template with connected button methods
'''

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap, QFont, QIcon)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy, QSlider, QSpinBox, QStatusBar, QStyleFactory, QToolBar, QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Dialog(QDialog):
    """Dialog"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        
        self.dlgLayout = QVBoxLayout()

        self.lbl = QLabel('Are you sure you want to do this '
                            'potentially disastrous thing that '
                            'you are about to do?')
        
        self.btns = QDialogButtonBox()
        self.btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.btns.accepted.connect(self.user_confirmed)
        self.btns.rejected.connect(self.user_cancelled)

        self.dlgLayout.addWidget(self.lbl)
        self.dlgLayout.addWidget(self.btns)
        self.setLayout(self.dlgLayout)

    def user_confirmed(self):
        self.close()

    def user_cancelled(self):
        self.close()

""" From the docs:

A module’s __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt. (https://docs.python.org/3/library/__main__.html)
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
