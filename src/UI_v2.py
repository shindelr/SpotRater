# Author: Robin Shindelman
# Last Mod: 2024-02-08, 1pm, Robin


from PyQt5.QtWidgets import QWidget, QStackedWidget, QMainWindow, QApplication, QToolTip
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt

from homeWidg_v2 import Ui_Form as mainHomeWidget
from buoyDataWidg import Ui_Form as buoyDataWidg


class MainWindow(QMainWindow):
    def __init__(self, *args, obj=None, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        # Nav stack initialization:
        self.widg_stack = QStackedWidget()
        self.home_page = HomePage()
        self.buoy_page = buoyDataPage()

        self.setupUi()
        tip = """
            \n   The Goodness Rating\n
        -Green means waves are epic!\n
        -Yellow means waves are okay.\n
        -Red means waves are bad.\n\n
        This rating is derived from an algorithm learning off of historical \n
        buoy data sourced from NOAA. The criteria for judging the quality of \n
        surf is based on local knowledge of how each specific spot reacts to \n
        a variety of conditions. \n
        """
        self.home_page.help_lbl.setToolTip(tip)


    def setupUi(self):
        """Set up initial main window on start up."""
        # Widget stack initialization
        self.stack_the_widgets()
        # Immediately display homepage
        self.display_home_page()
        # Navigation logic
        self.nav_logic()

        self.setWindowTitle('The Spot Rater')


    def display_home_page(self):
        """
        Initializes home page on start up. Pretty much identical to close
        auxillary widget method but includes a resize() request.
        """
        self.widg_stack.setCurrentWidget(self.home_page)
        self.setCentralWidget(self.widg_stack)
        self.resize(900, 500)


    def stack_the_widgets(self):
        """Initializes all widgets into the stack."""
        self.widg_stack.addWidget(self.home_page)
        self.widg_stack.addWidget(self.buoy_page)


    def nav_logic(self):
        """Route all navigation button signals to correct places."""
        # SB button handling
        self.home_page.toBuoyData.clicked.connect(self.navigate_to_buoy)
        self.buoy_page.back_button.clicked.connect(self.close_aux_widg)


    def navigate_to_buoy(self):
        """Set widget stack to show south beach info page."""
        self.widg_stack.setCurrentWidget(self.buoy_page)
        self.setCentralWidget(self.widg_stack) 


    def close_aux_widg(self):
        """Return to home from any auxillary widget page."""
        self.widg_stack.setCurrentWidget(self.home_page)
        self.setCentralWidget(self.widg_stack)


class HomePage(QWidget, mainHomeWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Background Color:
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(232, 243, 247))
        self.setPalette(palette)

        # Fill the Spot Frame.
        # light_grey = 241, 242, 242
        self.spots_frame.setStyleSheet("background-color:rgb(241,242,242)")



class buoyDataPage(QWidget, buoyDataWidg):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Background Color:
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(232, 243, 247))
        self.setPalette(palette)

        # Fill text frames
        self.atmos_frame.setStyleSheet("background-color:rgb(241,242,242)")
        self.wind_frame.setStyleSheet("background-color:rgb(241,242,242)")
        self.swell_frame.setStyleSheet("background-color:rgb(241,242,242)")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
