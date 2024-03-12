    # NOAA stuff
token = 'WBtFHGISuLrFoPdVSVkEmLFzjhpWveRa'
buoy_id = '46050'
endpoint = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid=FIPS:41&token=" + token 

def get_data(endpoint):
    """TODO:"""
    # url = endpoint + token
    response = get(endpoint)
    data = response.json()
    return data
    # return url
    
print(get_data(endpoint))




# # Agate Cam Widget


# from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_Frame(object):
#     def setupUi(self, Frame):
#         Frame.setObjectName("Frame")
#         Frame.resize(924, 524)
#         self.gridLayout = QtWidgets.QGridLayout(Frame)
#         self.gridLayout.setObjectName("gridLayout")
#         self.camImage = QtWidgets.QLabel(Frame)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.camImage.sizePolicy().hasHeightForWidth())
#         self.camImage.setSizePolicy(sizePolicy)
#         self.camImage.setMinimumSize(QtCore.QSize(900, 500))
#         self.camImage.setMaximumSize(QtCore.QSize(900, 500))
#         self.camImage.setFrameShape(QtWidgets.QFrame.WinPanel)
#         self.camImage.setFrameShadow(QtWidgets.QFrame.Plain)
#         self.camImage.setLineWidth(38)
#         self.camImage.setText("")
#         self.camImage.setPixmap(QtGui.QPixmap("src/uiFiles/../../image-scraper-master/images/agate_beach.jpg"))
#         self.camImage.setObjectName("camImage")
#         self.gridLayout.addWidget(self.camImage, 0, 0, 1, 1)
#         self.back_button = QtWidgets.QPushButton(Frame)
#         self.back_button.setGeometry(QtCore.QRect(20, 20, 50, 32))
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
#         self.back_button.setSizePolicy(sizePolicy)
#         self.back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.back_button.setText("")
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap("src/uiFiles/back_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.back_button.setIcon(icon)
#         self.back_button.setObjectName("back_button")

#         self.retranslateUi(Frame)
#         QtCore.QMetaObject.connectSlotsByName(Frame)

#     def retranslateUi(self, Frame):
#         _translate = QtCore.QCoreApplication.translate
#         Frame.setWindowTitle(_translate("Frame", "Agate Beach Cam"))