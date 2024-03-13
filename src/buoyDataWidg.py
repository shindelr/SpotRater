# Buoy Data Widget

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(770, 493)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)

        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")

        # Back button widget
        self.back_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button.setText("")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/robinshindelman/repos/school/361.SE/SpotRater/src/uiFiles/back_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button.setIcon(icon)
        self.back_button.setObjectName("back_button")
        self.gridLayout.addWidget(self.back_button, 0, 0, 1, 1)

        # Atmospheric Frame Widget basics
        self.atmos_frame = QtWidgets.QFrame(Form)
        self.atmos_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.atmos_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.atmos_frame.setObjectName("atmos_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.atmos_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # Atmos tool tip
        self.atmos_help = QtWidgets.QLabel(self.atmos_frame)
        self.atmos_help.setText("")
        self.atmos_help.setPixmap(QtGui.QPixmap("/Users/robinshindelman/repos/school/361.SE/SpotRater/src/uiFiles/../../assets/icons/question.png"))
        self.atmos_help.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.atmos_help.setObjectName("atmos_help")
        self.gridLayout_2.addWidget(self.atmos_help, 0, 2, 1, 1)
        self.atmos_title = QtWidgets.QLabel(self.atmos_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.atmos_title.sizePolicy().hasHeightForWidth())
        self.atmos_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.atmos_title.setFont(font)
        self.atmos_title.setAlignment(QtCore.Qt.AlignCenter)
        self.atmos_title.setObjectName("atmos_title")

        # Water and Air temps
        self.gridLayout_2.addWidget(self.atmos_title, 0, 1, 1, 1)
        self.water_temp_lbl = QtWidgets.QLabel(self.atmos_frame)
        self.water_temp_lbl.setObjectName("water_temp_lbl")
        self.gridLayout_2.addWidget(self.water_temp_lbl, 2, 0, 1, 3)
        self.air_temp_lbl = QtWidgets.QLabel(self.atmos_frame)
        self.air_temp_lbl.setObjectName("air_temp_lbl")
        self.gridLayout_2.addWidget(self.air_temp_lbl, 3, 0, 1, 3)
        self.gridLayout.addWidget(self.atmos_frame, 1, 1, 1, 1)

        # Wind widget
        self.wind_frame = QtWidgets.QFrame(Form)
        self.wind_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.wind_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.wind_frame.setObjectName("wind_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.wind_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")

        # Wind Speed
        self.wind_spd_lbl = QtWidgets.QLabel(self.wind_frame)
        self.wind_spd_lbl.setObjectName("wind_spd_lbl")
        self.gridLayout_3.addWidget(self.wind_spd_lbl, 4, 0, 1, 1)

        # Wind Gust
        self.wind_gust_lbl = QtWidgets.QLabel(self.wind_frame)
        self.wind_gust_lbl.setObjectName("wind_gust_lbl")
        self.gridLayout_3.addWidget(self.wind_gust_lbl, 5, 0, 1, 1)

        # Wind Direction
        self.wind_dir_lbl = QtWidgets.QLabel(self.wind_frame)
        self.wind_dir_lbl.setObjectName("wind_dir_lbl")
        self.gridLayout_3.addWidget(self.wind_dir_lbl, 3, 0, 1, 1)

        # Wind Tooltip
        self.wind_help = QtWidgets.QLabel(self.wind_frame)
        self.wind_help.setText("")
        self.wind_help.setPixmap(QtGui.QPixmap("/Users/robinshindelman/repos/school/361.SE/SpotRater/src/uiFiles/../../assets/icons/question.png"))
        self.wind_help.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wind_help.setObjectName("wind_help")
        self.gridLayout_3.addWidget(self.wind_help, 1, 3, 1, 1)
        self.wind_title = QtWidgets.QLabel(self.wind_frame)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.wind_title.setFont(font)
        self.wind_title.setAlignment(QtCore.Qt.AlignCenter)
        self.wind_title.setObjectName("wind_title")
        self.gridLayout_3.addWidget(self.wind_title, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.wind_frame, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("/Users/robinshindelman/repos/school/361.SE/SpotRater/src/uiFiles/../../assets/icons/buoy64.png"))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 3, 1, 1)

        # Swell Widget
        self.swell_frame = QtWidgets.QFrame(Form)
        self.swell_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.swell_frame.setObjectName("swell_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.swell_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")

        # Period
        self.dom_swl_period_lb = QtWidgets.QLabel(self.swell_frame)
        self.dom_swl_period_lb.setObjectName("dom_swl_period_lb")
        self.gridLayout_4.addWidget(self.dom_swl_period_lb, 2, 0, 1, 3)

        # Significant Height
        self.sigWaveHT_lbl = QtWidgets.QLabel(self.swell_frame)
        self.sigWaveHT_lbl.setObjectName("sigWaveHT_lbl")
        self.gridLayout_4.addWidget(self.sigWaveHT_lbl, 1, 0, 1, 1)

        # Swell Direction
        self.pr_swl_dir_lbl = QtWidgets.QLabel(self.swell_frame)
        self.pr_swl_dir_lbl.setObjectName("pr_swl_dir_lbl")
        self.gridLayout_4.addWidget(self.pr_swl_dir_lbl, 4, 0, 1, 1)
        self.sec_swl_dir_lbl = QtWidgets.QLabel(self.swell_frame)
        self.sec_swl_dir_lbl.setObjectName("sec_swl_dir_lbl")
        self.gridLayout_4.addWidget(self.sec_swl_dir_lbl, 5, 0, 1, 1)

        # Swell tool tips
        self.swell_help = QtWidgets.QLabel(self.swell_frame)
        self.swell_help.setText("")
        self.swell_help.setPixmap(QtGui.QPixmap("/Users/robinshindelman/repos/school/361.SE/SpotRater/src/uiFiles/../../assets/icons/question.png"))
        self.swell_help.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.swell_help.setObjectName("swell_help")
        self.gridLayout_4.addWidget(self.swell_help, 0, 2, 1, 1)
        self.sec_swl_per_lbl = QtWidgets.QLabel(self.swell_frame)
        self.sec_swl_per_lbl.setObjectName("sec_swl_per_lbl")
        self.gridLayout_4.addWidget(self.sec_swl_per_lbl, 3, 0, 1, 3)

        # Steepness
        self.steepness_lbl = QtWidgets.QLabel(self.swell_frame)
        self.steepness_lbl.setObjectName("steepness_lbl")
        self.gridLayout_4.addWidget(self.steepness_lbl, 6, 0, 1, 1)
        self.swell_title = QtWidgets.QLabel(self.swell_frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.swell_title.setFont(font)
        self.swell_title.setAlignment(QtCore.Qt.AlignCenter)
        self.swell_title.setObjectName("swell_title")
        self.gridLayout_4.addWidget(self.swell_title, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.swell_frame, 1, 2, 2, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.atmos_title.setText(_translate("Form", "Atmospheric"))
        self.water_temp_lbl.setText(_translate("Form", "Water Temperature:    52°F"))
        self.air_temp_lbl.setText(_translate("Form", "Air Temperature:    55°F"))
        self.wind_spd_lbl.setText(_translate("Form", "Wind Speed:     12 mph"))
        self.wind_gust_lbl.setText(_translate("Form", "Wind Gust:     18 mph"))
        self.wind_dir_lbl.setText(_translate("Form", "Wind Direction: WNW"))
        self.wind_title.setText(_translate("Form", "Wind"))
        self.dom_swl_period_lb.setText(_translate("Form", "Dominant Swell Period: 11 seconds"))
        self.sigWaveHT_lbl.setText(_translate("Form", "Significant Wave Height: 7.4 ft"))
        self.pr_swl_dir_lbl.setText(_translate("Form", "Primary Swell Direction:  S"))
        self.sec_swl_dir_lbl.setText(_translate("Form", "Secondary Swell Direction:  N/A"))
        self.sec_swl_per_lbl.setText(_translate("Form", "Secondary Swell Period: 8 seconds"))
        self.steepness_lbl.setText(_translate("Form", "Swell Steepness:    N/A"))
        self.swell_title.setText(_translate("Form", "Swell"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Current Buoy Data</span></p></body></html>"))
