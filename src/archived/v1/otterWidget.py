# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/robinshindelman/repos/school/361.SE/SpotRater/src/uiFiles/otterRockWidg.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(882, 567)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 0, 0, 1, 1)
        self.Close = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Close.sizePolicy().hasHeightForWidth())
        self.Close.setSizePolicy(sizePolicy)
        self.Close.setObjectName("Close")
        self.gridLayout.addWidget(self.Close, 0, 1, 1, 1)
        self.GoodnessRating = QtWidgets.QLabel(Form)
        self.GoodnessRating.setObjectName("GoodnessRating")
        self.gridLayout.addWidget(self.GoodnessRating, 1, 0, 1, 1)
        self.BoardRec = QtWidgets.QLabel(Form)
        self.BoardRec.setObjectName("BoardRec")
        self.gridLayout.addWidget(self.BoardRec, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Buoy Data"))
        self.label.setText(_translate("Form", "Significant Wave Height:"))
        self.label_2.setText(_translate("Form", "Swell Period:"))
        self.label_3.setText(_translate("Form", "Swell Direction: "))
        self.label_10.setText(_translate("Form", "Swell Steepness:"))
        self.label_7.setText(_translate("Form", "Water Temperature:"))
        self.label_4.setText(_translate("Form", "Wind Direction:"))
        self.label_5.setText(_translate("Form", "Wind Speed:"))
        self.label_6.setText(_translate("Form", "Air Temperature:"))
        self.groupBox_2.setTitle(_translate("Form", "Tide Chart"))
        self.Title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:700; text-decoration: underline;\">Otter Rock</span></p></body></html>"))
        self.Close.setText(_translate("Form", "x"))
        self.GoodnessRating.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Goodness Rating: </span></p></body></html>"))
        self.BoardRec.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Board Recommended: </span></p></body></html>"))