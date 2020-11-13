# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:31:36 2020

@author: hungd
"""

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QSizeGrip
from PyQt5.QtGui import QColor
from studyBuddy_ui import Ui_Form
import datetime
from datetime import date
import sys
import json

# Global Variable for resizing window
GLOBAL_STATE = 0

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.uiDefinitions()
        self.startUpValues(loadFromRegistry())
        self.buttonFunctions()
        self.show()

    
    ####################################
    # UI Design and Mouse Click Events #
    ####################################
    
        # Move Window
        def moveWindow(event):
            # Restore before move
            if GLOBAL_STATE == 1:
                self.maximize_restore()
    
            # If left click, move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
                
        # Set Title Bar (This is where you click to move window)
        self.ui.frame_top.mouseMoveEvent = moveWindow
                
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    def uiDefinitions(self):
        # Remove Title Bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Set Drop Shadow Window
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        
        # Apply Drop Shadow Frame
        self.ui.frame_background.setGraphicsEffect(self.shadow)
        
        # Maximize / Restore
        self.ui.btn_maximize.clicked.connect(lambda: self.maximize_restore())

        # Minimize
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # Close
        self.ui.btn_close.clicked.connect(lambda: self.close())

        # Create size grip to resize window
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        
    def maximize_restore(self):       
        global GLOBAL_STATE
        status = GLOBAL_STATE
        
        # IF NOT MAXIMIZED
        if status == 0:
            GLOBAL_STATE = 1
            self.showMaximized()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            
    
    ########################################
    # Start Up Values and Button Functions #
    ########################################
    
    # Start Up Values
    def startUpValues(self, registry):  
        
        # Initiate test date from registry
        self.ui.lineEdit_testDate.setText(registry['testDate'])
        
        # Initiate Questions Complete from registry
        self.ui.lineEdit_questionsComplete.setText(registry['questionsComplete'])
        
        # Initiate Questions Total from registry
        self.ui.lineEdit_totalQuestions.setText(registry['totalQuestions'])
        
        # Set Days Until Test
        self.testDateEdited(self.ui.lineEdit_testDate.text())
        
         # Set Questions Remaining, Questions Complete, and Questions per Day
        self.questionsCompleteEdited(self.ui.lineEdit_questionsComplete.text())

        # Set the Date
        self.ui.label_todaysDateEdit.setText(self.getTodaysDate())
    
    # Button Actions
    def buttonFunctions(self):
        
        # Change test Date
        self.ui.lineEdit_testDate.textChanged.connect(self.testDateEdited)
        
        # Change questions completed
        self.ui.lineEdit_questionsComplete.textChanged.connect(self.questionsCompleteEdited)
        
        # Change Total Questions
        self.ui.lineEdit_totalQuestions.textChanged.connect(self.totalQuestionsEdited)
    
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
        
        # Check if test crosses the 1-Year mark (Not going to account for leap-years)
        julianTestDate = (julianTestDate.tm_year - julianToday.tm_year) * 365 + julianTestDate.tm_yday
        julianToday = julianToday.tm_yday
        
        # Days until test
        DaysUntilTest = julianTestDate - julianToday
        self.ui.label_daysUntilTestEdit.setText(str(DaysUntilTest))
        
        # Questions per Day
        questionsComplete = int(self.ui.lineEdit_questionsComplete.text())
        totalQuestions = int(self.ui.lineEdit_totalQuestions.text())
        
        # Calculate Julian Date if the date does not equal todays date.  Otherwise, return 0
        if julianTestDate != julianToday:
            self.ui.label_questionsPerDayEdit.setText(str((totalQuestions - questionsComplete) // 
                                                          int(self.ui.label_daysUntilTestEdit.text())))
        else:
            self.ui.label_questionsPerDayEdit.setText(str(totalQuestions - questionsComplete))
        
        # Registry
        saveToRegistry('testDate', self.ui.lineEdit_testDate.text())

    # Questions Complete Change
    def questionsCompleteEdited(self, questionsComplete):
        # Check if questions completed is an integer
        try:
            questionsComplete = int(questionsComplete)
        except:
            return
        
        totalQuestions = int(self.ui.lineEdit_totalQuestions.text())
        
        # Set Questions remaining and Percent Complete labels
        self.ui.label_questionsRemainingEdit.setText(str(totalQuestions - questionsComplete))
        self.ui.label_questionsCompleteEdit.setText(str(round(questionsComplete/totalQuestions*100, 1)) + "%")
        self.ui.label_questionsPerDayEdit.setText(str(round((totalQuestions - questionsComplete) / 
                                                        int(self.ui.label_daysUntilTestEdit.text()), 1)))
        
        # Registry
        saveToRegistry('questionsComplete', self.ui.lineEdit_questionsComplete.text())
        
    # Questions Complete Change
    def totalQuestionsEdited(self, totalQuestions):
        # Check if questions completed is an integer
        try:
            totalQuestions = int(totalQuestions)
        except:
            return
        
        questionsComplete = int(self.ui.lineEdit_questionsComplete.text())
        
        # Set Questions remaining and Percent Complete labels
        self.ui.label_questionsRemainingEdit.setText(str(totalQuestions - questionsComplete))
        self.ui.label_questionsCompleteEdit.setText(str(round(questionsComplete/totalQuestions*100, 1)) + "%")
        self.ui.label_questionsPerDayEdit.setText(str((totalQuestions - questionsComplete) // 
                                                 int(self.ui.label_daysUntilTestEdit.text())))
        
        # Registry
        saveToRegistry('totalQuestions', self.ui.lineEdit_totalQuestions.text())
  
        
############
# Registry #
############

def loadFromRegistry():
    try:
        with open('registry.txt') as json_file:
            registry = json.load(json_file)
    except:
        registry = {'testDate': '12/16/2020', 'questionsComplete': '400', 'totalQuestions': '800'}
    return registry

def saveToRegistry(key, value):
    registry = loadFromRegistry()
    registry[key] = value
    with open('registry.txt', 'w') as outfile:
        json.dump(registry, outfile, indent=4)
        

########        
# Main #
########
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    