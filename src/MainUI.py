# Author: Robin Shindelman
# Last Mod: 2024-02-06

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QStackedWidget
from PyQt5.QtGui import QColor, QPalette
from InfoPage import Ui_Form
from homeWidget import Ui_Form as HomeScreen


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, obj=None, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        # Nav stack initialization:
        self.widg_stack = QStackedWidget()
        self.sb_widg = SBPage()
        self.home_page = HomePage()

        self.setWindowTitle('The Spot Rater')
        self.setupUi()

    def setupUi(self):
        """TODO:"""

        # Widget stack initialization
        self.widg_stack.addWidget(self.sb_widg)
        self.widg_stack.addWidget(self.home_page)
        # Immediately display homepage
        self.widg_stack.setCurrentWidget(self.home_page)
        self.setCentralWidget(self.widg_stack)
        self.resize(900, 500)

        # Navigation logic
        self.nav_logic()


    def nav_logic(self):
        """TODO:"""
        self.home_page.sbNavButton.clicked.connect(self.navigate_to_sb)
        self.sb_widg.Close.clicked.connect(self.close_sb)

    
    def navigate_to_sb(self):
        """Set widget stack to show south beach info page."""
        self.widg_stack.setCurrentWidget(self.sb_widg)
        self.setCentralWidget(self.widg_stack) 
    

    def close_sb(self):
        """Return to home from south beach info page"""
        self.widg_stack.setCurrentWidget(self.home_page)
        self.setCentralWidget(self.widg_stack)
        

class HomePage(QtWidgets.QWidget, HomeScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Background Color:
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(232, 243, 247))
        self.setPalette(palette)


class SBPage(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Background Color:
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(232, 243, 247))
        self.setPalette(palette)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()
    app.exec()
