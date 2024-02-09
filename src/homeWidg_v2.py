# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/robinshindelman/repos/school/361.SE/SpotRater/src/uiFiles/homeWidgV2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(807, 490)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(Form)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.spots_frame = QtWidgets.QFrame(Form)
        self.spots_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spots_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spots_frame.setObjectName("spots_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.spots_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.Ag_rating = QtWidgets.QLabel(self.spots_frame)
        self.Ag_rating.setText("")
        self.Ag_rating.setPixmap(QtGui.QPixmap("/Users/robinshindelman/repos/school/361.SE/SpotRater/src/uiFiles/good_rating.png"))
        self.Ag_rating.setAlignment(QtCore.Qt.AlignCenter)
        self.Ag_rating.setObjectName("Ag_rating")
        self.gridLayout.addWidget(self.Ag_rating, 1, 0, 1, 1)
        self.SB_rating = QtWidgets.QLabel(self.spots_frame)
        self.SB_rating.setText("")
        self.SB_rating.setPixmap(QtGui.QPixmap("/Users/robinshindelman/repos/school/361.SE/SpotRater/src/uiFiles/bad_rating.png"))
        self.SB_rating.setAlignment(QtCore.Qt.AlignCenter)
        self.SB_rating.setObjectName("SB_rating")
        self.gridLayout.addWidget(self.SB_rating, 1, 1, 1, 1)
        self.SB_label = QtWidgets.QLabel(self.spots_frame)
        self.SB_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SB_label.setObjectName("SB_label")
        self.gridLayout.addWidget(self.SB_label, 0, 1, 1, 1)
        self.OR_rating = QtWidgets.QLabel(self.spots_frame)
        self.OR_rating.setText("")
        self.OR_rating.setPixmap(QtGui.QPixmap("/Users/robinshindelman/repos/school/361.SE/SpotRater/src/uiFiles/okay_rating.png"))
        self.OR_rating.setAlignment(QtCore.Qt.AlignCenter)
        self.OR_rating.setObjectName("OR_rating")
        self.gridLayout.addWidget(self.OR_rating, 1, 2, 1, 1)
        self.OR_label = QtWidgets.QLabel(self.spots_frame)
        self.OR_label.setAlignment(QtCore.Qt.AlignCenter)
        self.OR_label.setObjectName("OR_label")
        self.gridLayout.addWidget(self.OR_label, 0, 2, 1, 1)
        self.Ag_label = QtWidgets.QLabel(self.spots_frame)
        self.Ag_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Ag_label.setObjectName("Ag_label")
        self.gridLayout.addWidget(self.Ag_label, 0, 0, 1, 1)
        self.help_lbl = QtWidgets.QLabel(self.spots_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help_lbl.sizePolicy().hasHeightForWidth())
        self.help_lbl.setSizePolicy(sizePolicy)
        self.help_lbl.setText("")
        self.help_lbl.setPixmap(QtGui.QPixmap("/Users/robinshindelman/repos/school/361.SE/SpotRater/src/uiFiles/../../assets/icons/question.png"))
        self.help_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.help_lbl.setObjectName("help_lbl")
        self.gridLayout.addWidget(self.help_lbl, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.spots_frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tide_chart = QtWidgets.QLabel(Form)
        self.tide_chart.setText("")
        self.tide_chart.setPixmap(QtGui.QPixmap("/Users/robinshindelman/repos/school/361.SE/SpotRater/src/uiFiles/../../assets/images/Figure_1 copy.png"))
        self.tide_chart.setObjectName("tide_chart")
        self.horizontalLayout.addWidget(self.tide_chart)
        self.toBuoyData = QtWidgets.QPushButton(Form)
        self.toBuoyData.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toBuoyData.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/robinshindelman/repos/school/361.SE/SpotRater/src/uiFiles/../../assets/icons/buoy32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toBuoyData.setIcon(icon)
        self.toBuoyData.setIconSize(QtCore.QSize(32, 32))
        self.toBuoyData.setObjectName("toBuoyData")
        self.horizontalLayout.addWidget(self.toBuoyData)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Spots</span></p></body></html>"))
        self.SB_label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">South Beach</span></p></body></html>"))
        self.OR_label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Otter Rock</span></p></body></html>"))
        self.Ag_label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Agate Beach</span></p></body></html>"))
        self.toBuoyData.setText(_translate("Form", "Detailed Buoy Data"))
