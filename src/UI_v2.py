# Author: Robin Shindelman
# Last Mod: 2024-02-09, 2pm, Robin


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


    def setupUi(self):
        """Set up initial main window on start up."""
        # Widget stack initialization
        self.stack_the_widgets()
        # Immediately display homepage
        self.display_home_page()
        # Navigation logic
        self.nav_logic()
        # Create tool tips
        self.tool_tips()

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


    def tool_tips(self):
        """Display little tutorials for the user when they hover over features"""
        rating_tip = """
            \n   The Goodness Rating\n
        -Green means waves are epic!\n
        -Yellow means waves are okay.\n
        -Red means waves are bad.\n\n
        This rating is derived from an algorithm learning off of historical \n
        buoy data sourced from NOAA. The criteria for judging the quality of \n
        surf is based on local knowledge of how each specific spot reacts to \n
        a variety of conditions. \n
        """
        tide_tip = """
                \n    The Tide Chart \n
        This chart depicts the high and low tides in an 18 hour period in the \n
        local area. The vertical axis describes the water level in feet, the \n
        horizontal axis describes the time of day. Find the low and high tides \n
        by examining the peaks and troughs of the curve. \n\n
        Some interesting surf lingo: \n
        - When the tide is incoming (going from low to high), this is called \n
        the push, and the waves are rumored to be more powerful. \n
        - When the tide is outgoing (going from high to low), the waves are \n
        typically weaker, but some surfers say it's easier to find a hollow and \n
        barreling wave. Interestingly, no one has a fun word for the outgoing tide.
        """
        atmos_tip = """
            \n      Atmospheric Data \n
        This box contains two simple measurements, water temperature and air \n
        temperature. Both measurements are taken in Farenheit.
        """
        wind_tip = """
            \n      Wind Data \n
        This box contains information regarding wind data relevant to surfers. \n\n
        - Wind Direction: This measurement is reported in degrees, then \n
        translated into a more readable notation. W=West, N=North, E=East, S=South. \n
        Some spots do better with one wind direction or another. \n
        - Wind Speed: This is an 8 minute average of wind speed given in meters \n
        per second then converted to miles per hour. In this area, a wind speed \n
        below 15 mph is surfable without protection. \n
        - Wind Gust: Gusts represent the peak wind speed recorded in the same 8 \n
        minute measurement interval as above. \n
        """
        swell_tip = """
                 Swell Data \n
        This box contains information regarding swell data relevant to surfers. \n\n
        - Significant Wave Height: This measurement represents the height of \n
        the tallest waves recorded in a 20 minute interval. These waves are \n
        measured in meters, then converted to feet. The size of wave you see \n
        here will correspond to the size of the largest waves you're likely to \n
        encounter during your surf session. \n
        - Dominant Swell Period: This refers to the time recorded between peaks \n
        or troughs of the primary swell. A greater period corresponds to cleaner \n
        and more powerful surf. \n
        - Secondary Swell Period: This is the same as the dominant, but referring \n
        to the next most prominent swell present in the water. \n
        - Primary Swell Direction: This measurement records the direction of \n
        the dominant swell. Different spots react to various swell directions \n
        in interesting ways. Depending on the season, surfers may 'hide' from \n
        overwhelmingly large swell behind geographical features that block a \n
        particular direction. \n
        - Secondary Swell Direction: Same as above. If you notice this measurement \n
        is in a direction which will meet the dominant swell at a steep angle, \n
        it's possible conditions will be choppy and sloppy or peaky and fun \n
        depending on the swell periods. \n
        - Swell Steepness: A measurement of the ratio between wave length and \n
        wave height. \n
        """

        self.home_page.help_lbl.setToolTip(rating_tip)
        self.home_page.tide_chart.setToolTip(tide_tip)
        self.buoy_page.atmos_help.setToolTip(atmos_tip)
        self.buoy_page.wind_help.setToolTip(wind_tip)
        self.buoy_page.swell_help.setToolTip(swell_tip)


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
