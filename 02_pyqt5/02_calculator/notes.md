# Some Notes on Calc program

## Links:
- [PyQt5 Documentation](https://doc.qt.io/qtforpython/api.html)
- [Article on the use of underscores in python](https://dbader.org/blog/meaning-of-underscores-in-python)
- [More on eval()](https://realpython.com/python-eval-function/)

## QWidget

This is the base class for all UI objects. It contains many of the methods that we use to set up a general window, such as setFixedSize(), and setWindowTitle().

## QMainWindow

- You can’t create a main window without first setting a central widget. You must have a central widget, even if it’s just a placeholder. When this is the case, you can use a QWidget object as your central widget. You can set the main window’s central widget with .setCentralWidget(). The main window’s layout will allow you to have only one central widget, but it can be a single or a composite widget.