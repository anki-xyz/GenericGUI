from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, \
    QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
import pyqtgraph as pg
import numpy as np

class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.l = QGridLayout(self)

        # Create a plot outside the central widget
        x = np.linspace(0, 10*np.pi)
        y = np.sin(x)/x**2
        self.plot = pg.plot(x, y)

        # Create an ImageView inside the central widget
        self.imv = pg.ImageView()
        self.l.addWidget(self.imv)

        # random, grayscale image
        random_im = np.random.randint(0, 255, (10, 10)).astype(np.uint8)
        self.imv.setImage(random_im)

    def keyPressEvent(self, e):
        modifiers = QApplication.keyboardModifiers()

        # Checks for a specific key ("I") and if Ctrl is pressed
        if e.key() == Qt.Key_I and modifiers == Qt.ControlModifier:
            QMessageBox.information(self, "Shortcut", "Shortcut recognized!")

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.status = self.statusBar()
        self.menu = self.menuBar()

        # Main top menu
        self.file = self.menu.addMenu("&File")
        self.file.addAction("Open", self.open)
        self.file.addAction("Save", self.save)
        self.file.addAction("Close", self.close)

        # Central widget
        self.w = None

        # Title
        self.setWindowTitle("Generic GUI")
        self.setGeometry(100, 100, 800, 600)

    def open(self):
        self.fn = QFileDialog.getOpenFileName()[0]

        if self.fn:
            self.status.showMessage(self.fn)
            self.w = Interface()
            self.setCentralWidget(self.w)

    def save(self):
        QMessageBox.critical(self, 
            "Meaningful error", 
            "Something went wrong!")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    m = Main()
    m.show()

    sys.exit(app.exec_())