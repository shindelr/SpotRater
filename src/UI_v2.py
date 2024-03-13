# Author: Robin Shindelman
# Last Mod: 2024-03-01, 8am, Robin


# Communication & data manipulation 
import zmq
from PIL import Image
from pandas import read_csv

# PyQt Dependencies
from PyQt5.QtWidgets import QWidget, QStackedWidget, QMainWindow, QApplication, QToolTip
from PyQt5.QtGui import QColor, QPalette, QPixmap
from PyQt5.QtCore import Qt
# UI forms
from homeWidg_v2 import Ui_Form as mainHomeWidget
from buoyDataWidg import Ui_Form as buoyDataWidg
from agCamWidg import Ui_Frame as agCamWidg



class MainWindow(QMainWindow):
    def __init__(self, *args, obj=None, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        # Nav stack initialization:
        self.widg_stack = QStackedWidget()
        self.home_page = HomePage()
        self.buoy_page = buoyDataPage()
        self.ag_cam_page = agCamWPage()

        self.setupUi()

        # set up PyZMQ socket for communication with image scraper.
        PORT = "5555"
        context = zmq.Context()
        print("connecting to server")
        self.socket = context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:" + PORT)



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
        self.widg_stack.addWidget(self.ag_cam_page)



    def nav_logic(self):
        """Route all navigation button signals to correct places."""
        # SB button handling
        self.home_page.toBuoyData.clicked.connect(self.navigate_to_buoy)
        self.home_page.toCamImage.clicked.connect(self.navigate_to_cam)
        self.buoy_page.back_button.clicked.connect(self.close_aux_widg)
        self.ag_cam_page.back_button.clicked.connect(self.close_aux_widg)


    def navigate_to_cam(self):
        """Set widget stack to show agate beach cam"""
        self.widg_stack.setCurrentWidget(self.ag_cam_page)
        self.setCentralWidget(self.widg_stack)
        self.image_scraper()
        self.ag_cam_page.camImage.setPixmap(QPixmap("src/uiFiles/../../image-scraper-master/images/agate_beach.jpg"))


    def navigate_to_buoy(self):
        """Set widget stack to show buoy info page."""
        self.widg_stack.setCurrentWidget(self.buoy_page)
        self.setCentralWidget(self.widg_stack)


    def close_aux_widg(self):
        """Return to home from any auxillary widget page."""
        self.widg_stack.setCurrentWidget(self.home_page)
        self.setCentralWidget(self.widg_stack)

    
    def image_scraper(self):
        """Communicate with image scraping service. Service must be running."""
        # Send request for image and then wait to receive it.
        self.socket.send(b'cam_image')
        print('Requesting image')
        image = self.socket.recv()
        print('Received image')
        path = '/Users/robinshindelman/repos/school/361.SE/SpotRater/image-scraper-master/images/agate_beach.jpg'
        with open(path, 'wb') as img:
            byte_array = bytearray(image)
            img.write(byte_array)
        with Image.open(path) as img:
            resize = img.resize((900,500))
            resize.save(path)


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
        buoy_button_tip = """Click me to go see the buoy data. There will be
        a back button to return you to this page."""
        cam_button_tip = """Click me to go see a picture of the surf at Agate Beach
        right now. The image is updated every 5 minutes. There will be
        a back button to return you to this page."""

        self.home_page.help_lbl.setToolTip(rating_tip)
        self.home_page.tide_chart.setToolTip(tide_tip)
        self.buoy_page.atmos_help.setToolTip(atmos_tip)
        self.buoy_page.wind_help.setToolTip(wind_tip)
        self.buoy_page.swell_help.setToolTip(swell_tip)
        self.home_page.toBuoyData.setToolTip(buoy_button_tip)
        self.home_page.toCamImage.setToolTip(cam_button_tip)


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

        self.labels = {
            'WDIR': None,
            'WSPD': None,
            'GST':  None,
            'WVHT': None,
            'DPD':  None,
            'APD':  None,
            'MWD':  None,
            'ATMP': None,
            'WTMP': None
        }

        # Fill current data
        self.current_data = self.get_NBDC_data()
        self.populate_fields()


    def get_NBDC_data(self):
        """
        Retrieve the most recent, complete row of data from buoy number 46050.
        :return:
            The cleanest, most recent row of a pandas data frame.
        """
        url = 'https://www.ndbc.noaa.gov/data/realtime2/46050.txt'
        data = read_csv(url, sep='\s+')

        sub_frame = data.iloc[:, :-4]  # Cuts off 'DEWP' 'VIS' 'PTDY' 'TIDE'

        # Tricky boolean mask that returns a complete row of data
        complete_rows = sub_frame[~sub_frame.isin(['MM']).any(axis=1)]

        return complete_rows.iloc[[1]]


    def populate_fields(self):
        """
        Set all fields to their current values. At the moment, all values are
        reported in metric.
        """
        self.fill_labels(self.current_data)
        self.wind_dir_lbl.setText('Wind Direction: ' + self.labels['WDIR'] + ' degrees')
        self.wind_spd_lbl.setText('Wind Speed: ' + self.labels['WSPD'] + ' m/s')
        self.wind_gust_lbl.setText(f'Wind Gust: ' + self.labels['GST'] + ' m/s')
        self.sigWaveHT_lbl.setText(f'Significant Wave Height: ' + self.labels['WVHT'] + ' m')
        self.dom_swl_period_lb.setText(f'Dominant Period: ' + self.labels['DPD'] + ' sec')
        self.sec_swl_per_lbl.setText(f'Average Period: ' + self.labels['APD'] + ' sec')
        self.pr_swl_dir_lbl.setText(f'Primary Swell Direction: ' + self.labels['MWD'] + ' degrees')
        self.air_temp_lbl.setText(f'Air Temperature: ' + self.labels['ATMP'] + ' C')
        self.water_temp_lbl.setText(f'Water Temperature: ' + self.labels['WTMP'] + ' C')


    def fill_labels(self, data):
        """Populate the current data dictionary with data."""
        for key in self.labels:
            val = str(data[key].values)
            self.labels[key] = val[2:-2]


class agCamWPage(QWidget, agCamWidg):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Background Color:
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(232, 243, 247))
        self.setPalette(palette)


def run_app():
    """
    Generate an instance of QApplication and a MainWindow for it to run in.
    Starts the Surfing App.
    """    
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    run_app()
