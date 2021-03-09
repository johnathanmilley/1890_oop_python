# Filename: pyqt_lab1_modulo_calc.py

"""Basic Modulo Calculator built using PyQt5"""

import sys

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
        
def calculate_modulo():
    if a.text() and n.text() :
        result.setText(f'{a.text()} mod {n.text()} = ' +
                       f'{int(a.text()) % int(n.text())}')
    else:
        result.setText('<p style="color: red">You must enter 2 integers</p>')
        
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Lab 1: Modulo Calculator')
layout = QVBoxLayout()

# Add 2 QLineEdit fields
a = QLineEdit()
a.setValidator(QIntValidator())
layout.addWidget(a)

n = QLineEdit()
n.setValidator(QIntValidator())
layout.addWidget(n)

calculate_btn = QPushButton('Calculate')
calculate_btn.clicked.connect(calculate_modulo)
layout.addWidget(calculate_btn)

result = QLabel('')
layout.addWidget(result)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
