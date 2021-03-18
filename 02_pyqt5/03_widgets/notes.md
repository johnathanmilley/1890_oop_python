# Week 8: More Widgets

## Code Files

- `widget_gallery.py` — This code was obtained from the [official pyqt repo](https://github.com/pyqt/examples). I have added some comments for teaching purposes. 
- `widget_list.py` — Some additional code that I wrote that contains a number of widgets.


## Adding layouts and widgets to the window

The general format that I follow when adding widgets to a page is this:

1. Create a layout (QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout)
2. Create interactive widgets (QLabel, QLineEdit, QPushButton, QCheckBox, QRadioButton, QComboBox, etc.)
3. Add interactive widgets to the layout using `layout.addWidget()`
4. Use the `setLayout()` method to add the layout to the window (QDialog, QWidget, QMainWindow)
    - Example: `self.setLayout(main_layout)`, where `self` is a QDialog.
    - Exmaple 2: `self._centralLayout(main_layout)`, where `self` is a QMainWindow. (QMainWindow requires a central widget)
    - https://doc.qt.io/qt-5/application-windows.html