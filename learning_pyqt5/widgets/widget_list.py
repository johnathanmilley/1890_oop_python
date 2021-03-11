""" Purpose: To provide a simple example of various widgets 
    John Milley
"""

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)


class ListOfWidgets(QDialog):
    def __init__(self):
        super().__init__()

        # Create the main layout for ListOfWidgets class, which inherits from the QDialog class
        main_layout = QVBoxLayout()

        # Title Label
        title = QLabel("<h1 style='color: orange;'>More Widgets!</h1>")

        # QComboBox is called a drop-down menu on most platforms
        quantity = QComboBox()
        choices = {'1': 1, '2': 2, '3': 3}
        quantity.addItems(choices.keys()) # The items added to a dropdown list need to be Strings

        quantity_label = QLabel('&Quantity:')
        quantity_label.setBuddy(quantity)

        # Moving the creation of groups of widgets to a class method
        # This is a style choice. It keeps the __init__() more readable.
        self.create_radio_group()
        self.create_checkbox_group()
        self.create_tab_group()

        # Add widgets and widget groups to the main_layout
        main_layout.addWidget(title)
        main_layout.addWidget(quantity_label)
        main_layout.addWidget(quantity)
        main_layout.addWidget(self.radio_group)
        main_layout.addWidget(self.checkbox_group)
        main_layout.addWidget(self.tab_group)
        self.setLayout(main_layout) # Finally, set main_layout as the layout for the ListOfWidgets instance

    def create_radio_group(self):
        """Create a group of radio buttons"""
        # A QGroupBox provides a frame and a title to group widgets together
        # https://pythonbasics.org/pyqt-groupbox/
        self.radio_group = QGroupBox("Radio Button Group")
        radio_layout = QVBoxLayout()

        radio1 = QRadioButton("Apple")
        radio2 = QRadioButton("Orange")
        radio3 = QRadioButton("Banana")
        radio4 = QRadioButton("Grapes")
        radio_layout.addWidget(radio1)
        radio_layout.addWidget(radio2)
        radio_layout.addWidget(radio3)
        radio_layout.addWidget(radio4)

        # Set radio button layout as the layout for the QGroupBox
        self.radio_group.setLayout(radio_layout)
    
    def create_checkbox_group(self):
        """Create a group of checkbox widgets"""
        self.checkbox_group = QGroupBox("Checkbox Button Group")
        checkbox_layout = QHBoxLayout()

        checkbox1 = QCheckBox("Music")
        checkbox2 = QCheckBox("Movies")
        checkbox3 = QCheckBox("Gaming")
        checkbox4 = QCheckBox("Reading")
        checkbox_layout.addWidget(checkbox1)
        checkbox_layout.addWidget(checkbox2)
        checkbox_layout.addWidget(checkbox3)
        checkbox_layout.addWidget(checkbox4)

        self.checkbox_group.setLayout(checkbox_layout)

    def create_tab_group(self):
        self.tab_group = QTabWidget()

        # FIRST TAB
        first_tab = QWidget()
        first_tab_layout = QHBoxLayout()

        feedback = QTextEdit()
        feedback.setPlaceholderText("Please provide feedback...")

        first_tab_layout.addWidget(feedback)
        first_tab.setLayout(first_tab_layout)

        # SECOND TAB
        second_tab = QWidget()
        second_tab_layout = QVBoxLayout()

        # Creating a slider that updates a label with the current value
        self.slider = QSlider(Qt.Horizontal, self.tab_group)
        self.slider.setValue(10)
        self.slider.valueChanged.connect(self.slider_moved)
        
        # Remeber that we can use some HTML + CSS in our labels
        self.slider_label = QLabel(f'<h1 style="color: red;">{str(self.slider.value())}</h1>')
        self.slider_label.setAlignment(Qt.AlignCenter)

        second_tab_layout.addWidget(self.slider)
        second_tab_layout.addWidget(self.slider_label)
        second_tab.setLayout(second_tab_layout)

        # Instead of setLayout(), for tabs we need to you use addTab() for each tab
        self.tab_group.addTab(first_tab, '&First')
        self.tab_group.addTab(second_tab, '&Second')

    def slider_moved(self):
        self.slider_label.setText(f'<h1 style="color: red;">{str(self.slider.value())}</h1>')

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    widgets = ListOfWidgets()
    widgets.show()
    sys.exit(app.exec_()) 