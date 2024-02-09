# Author: Robin Shindelman
# Last Mod: 2024-02-08, 1pm, Robin


from PyQt5.QtWidgets import QWidget, QStackedWidget, QMainWindow, QApplication
from PyQt5.QtGui import QColor, QPalette
from buoyDataWidg import Ui_Form as sbInfo
from homeWidget import Ui_Form as HomeScreen
from agBeachWidg import Ui_Form as agInfo
from otterWidget import Ui_Form as orInfo


class MainWindow(QMainWindow):
    def __init__(self, *args, obj=None, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        # Nav stack initialization:
        self.widg_stack = QStackedWidget()
        self.sb_widg = SBPage()
        self.home_page = HomePage()
        self.ag_widg = AgPage()
        self.or_widg = ORPage()

        self.setupUi()


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
        self.widg_stack.addWidget(self.sb_widg)
        self.widg_stack.addWidget(self.ag_widg)
        self.widg_stack.addWidget(self.or_widg)
        self.widg_stack.addWidget(self.home_page)


    def nav_logic(self):
        """Route all navigation button signals to correct places."""
        # SB button handling
        self.home_page.sbNavButton.clicked.connect(self.navigate_to_sb)
        self.sb_widg.Close.clicked.connect(self.close_aux_widg)

        # Ag button handling
        self.home_page.AgNavButton.clicked.connect(self.navigate_to_ag)
        self.ag_widg.Close.clicked.connect(self.close_aux_widg)
    
        # Otter button handling
        self.home_page.ORNavButton.clicked.connect(self.navigate_to_or)
        self.or_widg.Close.clicked.connect(self.close_aux_widg)
    

    def navigate_to_sb(self):
        """Set widget stack to show south beach info page."""
        self.widg_stack.setCurrentWidget(self.sb_widg)
        self.setCentralWidget(self.widg_stack) 
    

    def navigate_to_or(self):
        """Set widget stack to show agate info page."""
        self.widg_stack.setCurrentWidget(self.or_widg)
        self.setCentralWidget(self.widg_stack)
        
    
    def navigate_to_ag(self):
        """Set widget stack to show agate info page."""
        self.widg_stack.setCurrentWidget(self.ag_widg)
        self.setCentralWidget(self.widg_stack)


    def close_aux_widg(self):
        """Return to home from any auxillary widget page."""
        self.widg_stack.setCurrentWidget(self.home_page)
        self.setCentralWidget(self.widg_stack)


class HomePage(QWidget, HomeScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Background Color:
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(232, 243, 247))
        self.setPalette(palette)


class SBPage(QWidget, sbInfo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Background Color:
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(232, 243, 247))
        self.setPalette(palette)


class AgPage(QWidget, agInfo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Background Color:
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(232, 243, 247))
        self.setPalette(palette)


class ORPage(QWidget, orInfo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Background Color:
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(232, 243, 247))
        self.setPalette(palette)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
