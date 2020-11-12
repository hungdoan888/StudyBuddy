# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:57:42 2020

@author: hungd
"""

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
includefiles = ['C:/Users/hungd/Desktop/Python_Practice/StudyBuddy/cat.PNG', 
                'C:/Users/hungd/Desktop/Python_Practice/StudyBuddy/studyBuddy_ui.py']
includes = []
excludes = []
packages = ["os"]

# GUI applications require a different base on Windows (the default is for a
# console application).
base = "Console"
setup(  name = "studyBuddy",
        version = "0.1",
        description = "Used to determine how much you should study for an upcoming test",
        options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
        executables = [Executable("studyBuddy_main.py", base=base)])
