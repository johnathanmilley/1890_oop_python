# Filename: signal_slots.py

"""Signals and slots example."""

import sys

from functools import partial

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
        
# greeting that reads name from text field
def greeting():
    if name.text():
        greeting_msg.setText(f'Hello {name.text()}')
        name.setText('')
    else:
        greeting_msg.setText('')
        
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

# Name (LineEdit)
name = QLineEdit()
name.setPlaceholderText("Enter your name:")
name.returnPressed.connect(greeting)
layout.addWidget(name)

btn = QPushButton('Greet')
btn.clicked.connect(greeting)

layout.addWidget(btn)
greeting_msg = QLabel('')
layout.addWidget(greeting_msg)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
