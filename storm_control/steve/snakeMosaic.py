# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import sys
import re
from PyQt5 import QtCore, QtGui, QtWidgets

# Debugging
import storm_control.sc_library.hdebug as hdebug

# UIs.
import storm_control.steve.qtdesigner.steve_ui as steveUi
import storm_control.hal4000.qtWidgets.qtRangeSlider as qtRangeSlider
import storm_control.steve.qtRegexFileDialog as qtRegexFileDialog
 
# Graphics
import storm_control.steve.mosaicView as mosaicView
import storm_control.steve.objectives as objectives
import storm_control.steve.positions as positions
import storm_control.steve.sections as sections

# Communications
import storm_control.steve.capture as capture

# Misc
import storm_control.steve.coord as coord
import storm_control.sc_library.parameters as params

A = mosaicView.createGrid(5,5)
originX = 100
originY = 100
p = []
for x in A:
    p[0] = originX + int(str(x[0]))
    p[1] = originY + int(str(x[1]))
B = mosaicView.createSpiral(5)
print(A)
print(B)
print(p)
