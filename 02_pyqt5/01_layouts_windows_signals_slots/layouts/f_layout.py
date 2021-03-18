# Filename: g_layout.py

"""Form layout example.

A form layout is a 2-column format that typically contains label elements in the first column, and form widgets in the second (QLineEdit, QComboBox, QSpinBox).
"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QFormLayout')
layout = QFormLayout()
layout.addRow('Name:', QLineEdit())
layout.addRow('Age:', QLineEdit())
layout.addRow('Job:', QLineEdit())
layout.addRow('Hobbies:', QLineEdit())
layout.addRow('', QPushButton('Submit'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
