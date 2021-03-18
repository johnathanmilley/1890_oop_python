# Week 9 - Multi-Window, Images, Resources, Slots

There are 3 examples this week to read through and understand.

- `adding_images.py` - Demonstrates how to add images and icons to your application
  - `adding_images_resources.qrc` - link to images in this file
  - `adding_images_resources.py` - compiled python file from .qrc
  - To compile the .qrc file, run the following command in PowerShell:
        
      ``` pyrcc5 resources.qrc -o resources.py ```

    - if you are unable to run pyrcc5 then the Python's Scripts folder may not be in your PATH. [See these instructions](add_python_scripts_to_PATH.md)

- `stacked_widgets.py` - Demonstrates how to create an application with multiple 'screens'
  - `stacked_widgets.css` - external stylesheet used for styling widgets

- `random_roll.py` - Small example demonstrating slots and styles.

## Resources

### QResource System
- [Tutorial](https://www.learnpyqt.com/tutorials/qresource-system/#the%20qrc%20file)
- [Official Docs](https://doc.qt.io/qtforpython/overviews/resources.html)
- The QResource System makes it easier to manage all of the external media files used in your final application
- Examine the `adding_images.py` and `resources.qrc` files to see how to set up the QResource system

### Images
- [Tutorial](https://www.learnpyqt.com/tips/adding-images-to-pyqt5-applications/)
  - Note: this tutorial does not use the QResource System (you should)
- You can add images to your applications by creating a QPixmap and applying it to a QLabel.
```
# example from adding_images.py
self.header = QLabel()
self.win_v_linux = QPixmap(':/images/windows_v_linux.jpg') # :/ indicates a resource path
self.header.setPixmap(self.win_v_linux)
```
- Setting up a QResource system is recommended before adding images to your application.

### Using Style Sheets in PyQt
- What can be styled? 
  - https://doc.qt.io/qt-5/stylesheet-reference.html
  - https://doc.qt.io/archives/qt-4.8/stylesheet-examples.html
