'''
    QDialog template with connected button methods
'''

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (
                                QApplication, QCheckBox, QComboBox, QDialog,
                                QFormLayout, QGridLayout, QGroupBox, 
                                QHBoxLayout, QLabel, QLineEdit, QPushButton,
                                QStyleFactory,  QTextEdit, QVBoxLayout, QWidget
                            )


class HotDogSurvey(QDialog):
    """Dialog"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle('Hot Dog Survey')
        self.main_layout = QVBoxLayout()

        self.title = QLabel('<h1 style="color: red">Hot Dog Survey</h1>')
        self.title.setAlignment(Qt.AlignCenter)
        self.form = QFormLayout()

        # Form Widgets
        self.name = QLineEdit()
        self.age = QLineEdit()
        self.age.setValidator(QIntValidator())

        # Add Widgets to Form
        self.form.addRow('Name:', self.name)
        self.form.addRow('Age:', self.age)

        self.question_1 = QLabel((
                                    'How many hot dogs would you consume'
                                    ' for a single meal?'
                                ))
        self.how_many_hotdogs = QComboBox()
        choices = ['1', '2', '3', '4', '5+']
        self.how_many_hotdogs.addItems(choices)

        self.condiment_group = QGroupBox("Select preferred condiments:")
        self.condiment_layout = QGridLayout()

        self.cond_ketchup = QCheckBox("Ketchup")
        self.cond_mustard = QCheckBox("Mustard")
        self.cond_relish = QCheckBox("Relish")
        self.cond_cheese = QCheckBox("Cheese")
        self.cond_onions = QCheckBox("Onions")
        self.cond_bacon = QCheckBox("Bacon")

        self.condiment_layout.addWidget(self.cond_ketchup, 0, 0)
        self.condiment_layout.addWidget(self.cond_mustard, 0, 1)
        self.condiment_layout.addWidget(self.cond_relish, 0, 2)
        self.condiment_layout.addWidget(self.cond_cheese, 1, 0)
        self.condiment_layout.addWidget(self.cond_onions, 1, 1)
        self.condiment_layout.addWidget(self.cond_bacon, 1, 2)

        self.condiment_group.setLayout(self.condiment_layout)

        self.btn_layout = QHBoxLayout()
        self.submit_btn = QPushButton('Submit')
        self.submit_btn.clicked.connect(self.confirm)
        self.cancel_btn = QPushButton('Cancel')
        self.cancel_btn.clicked.connect(self.close)
        self.btn_layout.addWidget(self.submit_btn)
        self.btn_layout.addWidget(self.cancel_btn)

        self.main_layout.addWidget(self.title)
        self.main_layout.addLayout(self.form)
        self.main_layout.addWidget(self.question_1)
        self.main_layout.addWidget(self.how_many_hotdogs)
        self.main_layout.addWidget(self.condiment_group)
        self.main_layout.addLayout(self.btn_layout)
        self.setLayout(self.main_layout)

    def confirm(self):
        confirm_win = QDialog(self)
        confirm_win.setWindowTitle('Confirm')
        confirm_layout = QVBoxLayout()
        lbl = QLabel('Is this information correct?')
        name = QLabel(self.name.text())
        age = QLabel(self.age.text())
        num = QLabel(self.how_many_hotdogs.currentText())

        checked = []
        for c in self.condiment_group.findChildren(QCheckBox):
            if c.isChecked():
                checked.append(c.text())
        condiments = QLabel(str(checked))

        confirm_layout.addWidget(lbl)
        confirm_layout.addWidget(name)
        confirm_layout.addWidget(age)
        confirm_layout.addWidget(num)
        confirm_layout.addWidget(condiments)

        confirm_win.setLayout(confirm_layout)

        confirm_win.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = HotDogSurvey()
    dlg.show()
    sys.exit(app.exec_())
