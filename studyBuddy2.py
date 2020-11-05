# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studyBuddy.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import json
import datetime
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 626)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName("drop_shadow_layout")
        self.drop_shadow_frame = QtWidgets.QFrame(self.centralwidget)
        self.drop_shadow_frame.setMinimumSize(QtCore.QSize(828, 606))
        self.drop_shadow_frame.setMaximumSize(QtCore.QSize(16777215, 606))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drop_shadow_frame.setFont(font)
        self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_title = QtWidgets.QFrame(self.drop_shadow_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy)
        self.frame_title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_title.setStyleSheet("background-color: none;")
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_titleInside = QtWidgets.QFrame(self.frame_title)
        self.frame_titleInside.setStyleSheet("background-color: none;")
        self.frame_titleInside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_titleInside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_titleInside.setObjectName("frame_titleInside")
        self.label_title = QtWidgets.QLabel(self.frame_titleInside)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 241, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("background-color: none; color: rgb(60, 231, 195);")
        self.label_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title.setIndent(20)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.frame_titleInside)
        self.frame_btns = QtWidgets.QFrame(self.frame_title)
        self.frame_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_maximize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;    \n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(85, 255, 127, 150);\n"
"}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_4.addWidget(self.btn_maximize)
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(255, 170, 0, 150);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_4.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {        \n"
"    background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_4.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frame_btns)
        self.verticalLayout.addWidget(self.frame_title)
        self.frame_body = QtWidgets.QFrame(self.drop_shadow_frame)
        self.frame_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_body.setObjectName("frame_body")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_body)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_testDate = QtWidgets.QFrame(self.frame_body)
        self.frame_testDate.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_testDate.setStyleSheet("background-color: none;")
        self.frame_testDate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_testDate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_testDate.setObjectName("frame_testDate")
        self.lineEdit_testDate = QtWidgets.QLineEdit(self.frame_testDate)
        self.lineEdit_testDate.setGeometry(QtCore.QRect(10, 50, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_testDate.setFont(font)
        self.lineEdit_testDate.setAutoFillBackground(False)
        self.lineEdit_testDate.setStyleSheet("border: none;\n"
"color: rgb(220,220,220);\n"
"background-color: rgba(28, 29, 50, 255);")
        self.lineEdit_testDate.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_testDate.setObjectName("lineEdit_testDate")
        self.label_testDateTitle = QtWidgets.QLabel(self.frame_testDate)
        self.label_testDateTitle.setGeometry(QtCore.QRect(0, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_testDateTitle.setFont(font)
        self.label_testDateTitle.setStyleSheet("border: none;\n"
"color: rgb(60, 231, 195); background-color: none;")
        self.label_testDateTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_testDateTitle.setObjectName("label_testDateTitle")
        self.gridLayout.addWidget(self.frame_testDate, 0, 1, 1, 1)
        self.frame_daysUntilTest = QtWidgets.QFrame(self.frame_body)
        self.frame_daysUntilTest.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_daysUntilTest.setStyleSheet("background-color: none;")
        self.frame_daysUntilTest.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_daysUntilTest.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_daysUntilTest.setObjectName("frame_daysUntilTest")
        self.label_daysUntilTestTitle = QtWidgets.QLabel(self.frame_daysUntilTest)
        self.label_daysUntilTestTitle.setGeometry(QtCore.QRect(0, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_daysUntilTestTitle.setFont(font)
        self.label_daysUntilTestTitle.setStyleSheet("border: none;\n"
"color: rgb(60, 231, 195); background-color: none;")
        self.label_daysUntilTestTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_daysUntilTestTitle.setObjectName("label_daysUntilTestTitle")
        self.label_daysUntilTestEdit = QtWidgets.QLabel(self.frame_daysUntilTest)
        self.label_daysUntilTestEdit.setGeometry(QtCore.QRect(0, 0, 261, 141))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        self.label_daysUntilTestEdit.setFont(font)
        self.label_daysUntilTestEdit.setStyleSheet("border: none;\n"
"color: rgb(220,220,220);background-color: none;")
        self.label_daysUntilTestEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_daysUntilTestEdit.setObjectName("label_daysUntilTestEdit")
        self.gridLayout.addWidget(self.frame_daysUntilTest, 0, 2, 1, 1)
        self.frame_totalQuestions = QtWidgets.QFrame(self.frame_body)
        self.frame_totalQuestions.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_totalQuestions.setStyleSheet("background-color: none;")
        self.frame_totalQuestions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_totalQuestions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_totalQuestions.setObjectName("frame_totalQuestions")
        self.lineEdit_totalQuestions = QtWidgets.QLineEdit(self.frame_totalQuestions)
        self.lineEdit_totalQuestions.setGeometry(QtCore.QRect(10, 50, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_totalQuestions.setFont(font)
        self.lineEdit_totalQuestions.setAutoFillBackground(False)
        self.lineEdit_totalQuestions.setStyleSheet("border: none;\n"
"color: rgb(220,220,220);\n"
"background-color: rgba(28, 29, 50, 255);")
        self.lineEdit_totalQuestions.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_totalQuestions.setObjectName("lineEdit_totalQuestions")
        self.label_totalQuestionsTitle = QtWidgets.QLabel(self.frame_totalQuestions)
        self.label_totalQuestionsTitle.setGeometry(QtCore.QRect(0, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_totalQuestionsTitle.setFont(font)
        self.label_totalQuestionsTitle.setStyleSheet("border: none;\n"
"color: rgb(60, 231, 195); background-color: none;")
        self.label_totalQuestionsTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_totalQuestionsTitle.setObjectName("label_totalQuestionsTitle")
        self.gridLayout.addWidget(self.frame_totalQuestions, 1, 1, 1, 1)
        self.frame_questionsRemaining = QtWidgets.QFrame(self.frame_body)
        self.frame_questionsRemaining.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_questionsRemaining.setStyleSheet("background-color: none;")
        self.frame_questionsRemaining.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_questionsRemaining.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_questionsRemaining.setObjectName("frame_questionsRemaining")
        self.label_questionsRemaining = QtWidgets.QLabel(self.frame_questionsRemaining)
        self.label_questionsRemaining.setGeometry(QtCore.QRect(0, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_questionsRemaining.setFont(font)
        self.label_questionsRemaining.setStyleSheet("border: none;\n"
"color: rgb(60, 231, 195); background-color: none;")
        self.label_questionsRemaining.setAlignment(QtCore.Qt.AlignCenter)
        self.label_questionsRemaining.setObjectName("label_questionsRemaining")
        self.label_questionsRemainingEdit = QtWidgets.QLabel(self.frame_questionsRemaining)
        self.label_questionsRemainingEdit.setGeometry(QtCore.QRect(0, 0, 261, 141))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        self.label_questionsRemainingEdit.setFont(font)
        self.label_questionsRemainingEdit.setStyleSheet("border: none;\n"
"color: rgb(220,220,220);background-color: none;")
        self.label_questionsRemainingEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_questionsRemainingEdit.setObjectName("label_questionsRemainingEdit")
        self.gridLayout.addWidget(self.frame_questionsRemaining, 1, 2, 1, 1)
        self.frame_todaysDate = QtWidgets.QFrame(self.frame_body)
        self.frame_todaysDate.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_todaysDate.setStyleSheet("background-color: none;")
        self.frame_todaysDate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_todaysDate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_todaysDate.setObjectName("frame_todaysDate")
        self.label_todaysDateTitle = QtWidgets.QLabel(self.frame_todaysDate)
        self.label_todaysDateTitle.setGeometry(QtCore.QRect(0, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_todaysDateTitle.setFont(font)
        self.label_todaysDateTitle.setStyleSheet("border: none;\n"
"color: rgb(60, 231, 195); background-color: none;")
        self.label_todaysDateTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_todaysDateTitle.setObjectName("label_todaysDateTitle")
        self.label_todaysDateEdit = QtWidgets.QLabel(self.frame_todaysDate)
        self.label_todaysDateEdit.setGeometry(QtCore.QRect(0, 0, 261, 141))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        self.label_todaysDateEdit.setFont(font)
        self.label_todaysDateEdit.setStyleSheet("border: none;\n"
"color: rgb(220,220,220);background-color: none;")
        self.label_todaysDateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_todaysDateEdit.setObjectName("label_todaysDateEdit")
        self.gridLayout.addWidget(self.frame_todaysDate, 0, 0, 1, 1)
        self.frame_questionsComplete = QtWidgets.QFrame(self.frame_body)
        self.frame_questionsComplete.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_questionsComplete.setStyleSheet("background-color: none;")
        self.frame_questionsComplete.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_questionsComplete.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_questionsComplete.setObjectName("frame_questionsComplete")
        self.lineEdit_questionsComplete = QtWidgets.QLineEdit(self.frame_questionsComplete)
        self.lineEdit_questionsComplete.setGeometry(QtCore.QRect(10, 50, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_questionsComplete.setFont(font)
        self.lineEdit_questionsComplete.setAutoFillBackground(False)
        self.lineEdit_questionsComplete.setStyleSheet("border: none;\n"
"color: rgb(220,220,220);\n"
"background-color: rgba(28, 29, 50, 255);")
        self.lineEdit_questionsComplete.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_questionsComplete.setObjectName("lineEdit_questionsComplete")
        self.label_questionsCompleteTitle = QtWidgets.QLabel(self.frame_questionsComplete)
        self.label_questionsCompleteTitle.setGeometry(QtCore.QRect(0, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_questionsCompleteTitle.setFont(font)
        self.label_questionsCompleteTitle.setStyleSheet("border: none;\n"
"color: rgb(60, 231, 195); background-color: none;")
        self.label_questionsCompleteTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_questionsCompleteTitle.setObjectName("label_questionsCompleteTitle")
        self.gridLayout.addWidget(self.frame_questionsComplete, 1, 0, 1, 1)
        self.frame_percentCompleteOutside = QtWidgets.QFrame(self.frame_body)
        self.frame_percentCompleteOutside.setStyleSheet("background-color: none;")
        self.frame_percentCompleteOutside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_percentCompleteOutside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_percentCompleteOutside.setObjectName("frame_percentCompleteOutside")
        self.frame_percentCompleteInside = QtWidgets.QFrame(self.frame_percentCompleteOutside)
        self.frame_percentCompleteInside.setGeometry(QtCore.QRect(0, 0, 261, 241))
        self.frame_percentCompleteInside.setStyleSheet("background-color: none;")
        self.frame_percentCompleteInside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_percentCompleteInside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_percentCompleteInside.setObjectName("frame_percentCompleteInside")
        self.frame_questionsPerDayInsideInside = QtWidgets.QFrame(self.frame_percentCompleteInside)
        self.frame_questionsPerDayInsideInside.setGeometry(QtCore.QRect(30, 10, 221, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_questionsPerDayInsideInside.sizePolicy().hasHeightForWidth())
        self.frame_questionsPerDayInsideInside.setSizePolicy(sizePolicy)
        self.frame_questionsPerDayInsideInside.setStyleSheet("QFrame{\n"
"    border: 5px solid rgb(60, 231, 195);\n"
"    border-radius: 110px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_questionsPerDayInsideInside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_questionsPerDayInsideInside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_questionsPerDayInsideInside.setObjectName("frame_questionsPerDayInsideInside")
        self.label_questionsPerDayTitle = QtWidgets.QLabel(self.frame_questionsPerDayInsideInside)
        self.label_questionsPerDayTitle.setGeometry(QtCore.QRect(-20, 70, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_questionsPerDayTitle.setFont(font)
        self.label_questionsPerDayTitle.setStyleSheet("border: none;\n"
"color: rgb(60, 231, 195); background-color: none;")
        self.label_questionsPerDayTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_questionsPerDayTitle.setObjectName("label_questionsPerDayTitle")
        self.label_questionsPerDayEdit = QtWidgets.QLabel(self.frame_questionsPerDayInsideInside)
        self.label_questionsPerDayEdit.setGeometry(QtCore.QRect(10, 80, 211, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        self.label_questionsPerDayEdit.setFont(font)
        self.label_questionsPerDayEdit.setStyleSheet("border: none;\n"
"color: rgb(220,220,220);background-color: none;")
        self.label_questionsPerDayEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_questionsPerDayEdit.setObjectName("label_questionsPerDayEdit")
        self.gridLayout.addWidget(self.frame_percentCompleteOutside, 2, 1, 1, 1)
        self.frame_questionsPerDayOutside = QtWidgets.QFrame(self.frame_body)
        self.frame_questionsPerDayOutside.setStyleSheet("background-color: none;")
        self.frame_questionsPerDayOutside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_questionsPerDayOutside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_questionsPerDayOutside.setObjectName("frame_questionsPerDayOutside")
        self.frame_questionsPerDayInside = QtWidgets.QFrame(self.frame_questionsPerDayOutside)
        self.frame_questionsPerDayInside.setGeometry(QtCore.QRect(20, 10, 221, 221))
        self.frame_questionsPerDayInside.setStyleSheet("QFrame{\n"
"    border: 5px solid rgb(60, 231, 195);\n"
"    border-radius: 110px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_questionsPerDayInside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_questionsPerDayInside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_questionsPerDayInside.setObjectName("frame_questionsPerDayInside")
        self.label_questionsPerDayTitle_2 = QtWidgets.QLabel(self.frame_questionsPerDayInside)
        self.label_questionsPerDayTitle_2.setGeometry(QtCore.QRect(-20, 70, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_questionsPerDayTitle_2.setFont(font)
        self.label_questionsPerDayTitle_2.setStyleSheet("border: none;\n"
"color: rgb(60, 231, 195); background-color: none;")
        self.label_questionsPerDayTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_questionsPerDayTitle_2.setObjectName("label_questionsPerDayTitle_2")
        self.label_questionsPerDayEdit_2 = QtWidgets.QLabel(self.frame_questionsPerDayInside)
        self.label_questionsPerDayEdit_2.setGeometry(QtCore.QRect(0, 80, 221, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        self.label_questionsPerDayEdit_2.setFont(font)
        self.label_questionsPerDayEdit_2.setStyleSheet("border: none;\n"
"color: rgb(220,220,220);background-color: none;")
        self.label_questionsPerDayEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_questionsPerDayEdit_2.setObjectName("label_questionsPerDayEdit_2")
        self.gridLayout.addWidget(self.frame_questionsPerDayOutside, 2, 2, 1, 1)
        self.frame_blank = QtWidgets.QFrame(self.frame_body)
        self.frame_blank.setStyleSheet("background-color: none;")
        self.frame_blank.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_blank.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_blank.setObjectName("frame_blank")
        self.catPicture = QtWidgets.QLabel(self.frame_blank)
        self.catPicture.setGeometry(QtCore.QRect(180, 140, 91, 111))
        self.catPicture.setText("")
        self.catPicture.setPixmap(QtGui.QPixmap("cat.PNG"))
        self.catPicture.setScaledContents(True)
        self.catPicture.setObjectName("catPicture")
        self.gridLayout.addWidget(self.frame_blank, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_body)
        self.frame_credit = QtWidgets.QFrame(self.drop_shadow_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_credit.sizePolicy().hasHeightForWidth())
        self.frame_credit.setSizePolicy(sizePolicy)
        self.frame_credit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_credit.setStyleSheet("background-color: none;")
        self.frame_credit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_credit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_credit.setObjectName("frame_credit")
        self.label_credit = QtWidgets.QLabel(self.frame_credit)
        self.label_credit.setGeometry(QtCore.QRect(0, 0, 131, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_credit.sizePolicy().hasHeightForWidth())
        self.label_credit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_credit.setFont(font)
        self.label_credit.setStyleSheet("background-color: none; color: rgb(128, 102, 168);")
        self.label_credit.setScaledContents(True)
        self.label_credit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_credit.setIndent(20)
        self.label_credit.setObjectName("label_credit")
        self.verticalLayout.addWidget(self.frame_credit)
        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Study Buddy"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.lineEdit_testDate.setText(_translate("MainWindow", "12/10/2020"))
        self.label_testDateTitle.setText(_translate("MainWindow", "TEST DATE"))
        self.label_daysUntilTestTitle.setText(_translate("MainWindow", "DAYS UNTIL TEST"))
        self.label_daysUntilTestEdit.setText(_translate("MainWindow", "39"))
        self.lineEdit_totalQuestions.setText(_translate("MainWindow", "1600"))
        self.label_totalQuestionsTitle.setText(_translate("MainWindow", "TOTAL QUESTIONS"))
        self.label_questionsRemaining.setText(_translate("MainWindow", "QUESTIONS REMAINING"))
        self.label_questionsRemainingEdit.setText(_translate("MainWindow", "1200"))
        self.label_todaysDateTitle.setText(_translate("MainWindow", "TODAY\'S DATE"))
        self.label_todaysDateEdit.setText(_translate("MainWindow", self.getTodaysDate()))
        self.lineEdit_questionsComplete.setText(_translate("MainWindow", "400"))
        self.label_questionsCompleteTitle.setText(_translate("MainWindow", "QUESTIONS COMPLETE"))
        self.label_questionsPerDayTitle.setText(_translate("MainWindow", "PERCENT COMPLETE"))
        self.label_questionsPerDayEdit.setText(_translate("MainWindow", "25%"))
        self.label_questionsPerDayTitle_2.setText(_translate("MainWindow", "QUESTIONS PER DAY"))
        self.label_questionsPerDayEdit_2.setText(_translate("MainWindow", "25"))
        self.label_credit.setText(_translate("MainWindow", "By: Hung Doan"))
        
        # Actions to be completed
        self.lineEdit_testDate.textChanged.connect(self.testDateEdited)
        self.lineEdit_questionsComplete.textChanged.connect(self.questionsCompleteEdited)
        self.lineEdit_totalQuestions.textChanged.connect(self.totalQuestionsEdited)

    # Get Today's Date
    def getTodaysDate(self):
        today = date.today()
        return today.strftime("%m/%d/%Y")
    
    # Test Date edited
    def testDateEdited(self, testDate):
        # Test Date
        # Use try/except statement to check for valid
        try:
            testDate = datetime.datetime.strptime(testDate, '%m/%d/%Y')
        except:
            return
        
        julianTestDate = testDate.timetuple()
        
        # Today's Date
        today = date.today()
        julianToday = today.timetuple()
        
        # Days until test
        DaysUntilTest = julianTestDate.tm_yday - julianToday.tm_yday
        self.label_daysUntilTestEdit.setText(str(DaysUntilTest))
        
        # Questions per Day
        questionsComplete = int(self.lineEdit_questionsComplete.text())
        totalQuestions = int(self.lineEdit_totalQuestions.text())
        self.label_questionsPerDayEdit_2.setText(str((totalQuestions - questionsComplete) // 
                                                 int(self.label_daysUntilTestEdit.text())))

    # Questions Complete Change
    def questionsCompleteEdited(self, questionsComplete):
        # Check if questions completed is an integer
        try:
            questionsComplete = int(questionsComplete)
        except:
            return
        
        totalQuestions = int(self.lineEdit_totalQuestions.text())
        
        # Set Questions remaining and Percent Complete labels
        self.label_questionsRemainingEdit.setText(str(totalQuestions - questionsComplete))
        self.label_questionsPerDayEdit.setText(str(round(questionsComplete/totalQuestions*100, 1)) + "%")
        self.label_questionsPerDayEdit_2.setText(str((totalQuestions - questionsComplete) // 
                                                 int(self.label_daysUntilTestEdit.text())))
        
    # Questions Complete Change
    def totalQuestionsEdited(self, totalQuestions):
        # Check if questions completed is an integer
        try:
            totalQuestions = int(totalQuestions)
        except:
            return
        
        questionsComplete = int(self.lineEdit_questionsComplete.text())
        
        # Set Questions remaining and Percent Complete labels
        self.label_questionsRemainingEdit.setText(str(totalQuestions - questionsComplete))
        self.label_questionsPerDayEdit.setText(str(round(questionsComplete/totalQuestions*100, 1)) + "%")
        self.label_questionsPerDayEdit_2.setText(str((totalQuestions - questionsComplete) // 
                                                 int(self.label_daysUntilTestEdit.text())))
        

def loadFromRegistry(key):
    pass

def saveToRegistry(key, value):
    pass
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

