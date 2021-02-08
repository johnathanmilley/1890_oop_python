# Filename: hello.py

"""Simple Hello World example with PyQt5."""

import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# 2. Create an instance of QApplication 
app = QApplication(sys.argv)

# 3. Create an instance of your application's GUI
### NOTE: camelCase
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(500, 500, 800, 600)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(300,100)

#4. Show your applicaton's GUI
window.show()

#5. Run your application's event loop (or main loop)
sys.exit(app.exec_())


