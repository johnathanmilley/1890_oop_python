# Filename: dialog.py

"""Dialog-style application."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

class Dialog(QDialog):
    """Dialog"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        
        formLayout.addRow('Name:', QLineEdit())
        formLayout.addRow('Age:', QLineEdit())
        formLayout.addRow('Job:', QLineEdit())
        formLayout.addRow('Hobbies:', QLineEdit())
        
        dlgLayout.addLayout(formLayout)
        
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

""" From the docs:

A module’s __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt. (https://docs.python.org/3/library/__main__.html)
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
