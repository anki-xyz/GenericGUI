# GenericGUI
A generic graphical user interface (GUI) in Python, based on PyQt, numpy and pyqtgraph.
I'm using this as starting point for a new GUI.

## Features

- Main window with central widget
- Status bar
- Menu bar with File -> Open, Save, Close commands
- Open command...
  - selects a file using ```QFileDialog```
  - shows an x,y plot in a separate window
  - shows a random 10x10 image in the central widget
  - shows the filename in the status bar
- Save command produces a generic notification window (critical)
- The central widget accepts shortcuts, Ctrl+I shows a notification window (information)

## Screenshots

![Screenshot Main Window](https://github.com/anki-xyz/GenericGUI/generic_gui_screenshot1.png "Screenshot Main Window")

![Screenshot Plot](https://github.com/anki-xyz/GenericGUI/generic_gui_screenshot2.png "Screenshot Plot")

