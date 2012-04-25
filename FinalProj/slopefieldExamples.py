#!usr/local/bin/python
# /Users/mcdickenson/github/PS398/FinalProj/
# Examples for slopefieldPlot.py
import slopefieldPlot as sp


# Iwo Jima, no reinforcements
sp.slopefieldPlotter(0, 6, .2, 0, 3, .2, -0.05, -0.01, xLab='US', yLab='Japan', mainLab='Lanchester Squares, No Reinforcements', drawAxes=True, filename='lanchTester')
sp.drawVector(0, -0.05, -0.01, 0, 5.4, 2.15, 650, stepsize=0.1)
sp.pngSave('lanchTester2')

# Iwo Jima, reinforcement example
sp.slopefieldPlotter(0, 6, .2, 0, 3, .2, -0.05, -0.01, xLab='US', yLab='Japan', mainLab='Lanchester Squares, With Reinforcements', drawAxes=True, filename='reinfTester')
sp.drawVector(0, -0.05, -0.01, 0, 5.4, 2.15, 300, stepsize=0.1, colorVar='b')
sp.pngSave('reinfTester2')
sp.drawArrow(3.2, 5.05, .9, .9, headlength=0.05, direction='R', lineColor='r')
sp.pngSave('reinfTester3')
sp.drawVector(0, -0.05, -0.01, 0, 5.1, 0.9, 200, stepsize=0.1, colorVar='b')
sp.pngSave('reinfTester4')

# demonstrate arrow plot (on top of existing plot)
sp.drawArrow(1, 0, .9, .9, headlength=0.05, direction='L', lineColor='g')
sp.drawArrow(1, 1, .5, 2.0, headlength=0.1, direction='U', lineColor='b')
sp.drawArrow(2, 2, 2.5, 1.0, headlength=0.01, direction='D', lineColor='y')
sp.pngSave('arrowTester')

# check how/whether getEndVector and drawFinalVector are working
sp.slopefieldPlotter(0, 6, .2, 0, 4, .2, -0.05, -0.01, xLab='US', yLab='Japan', mainLab='Test of Vector Drawing', drawAxes=True, filename='vecTester')
sp.drawVector(0, -0.05, -0.01, 0, 4, 3, 100, stepsize=0.1, colorVar='b')
xtmp, ytmp = sp.getEndVector(0, -0.05, -0.01, 0, 4, 3, 100, stepsize=0.1)
sp.drawArrow(xtmp, xtmp+1, ytmp, ytmp, headlength=0.05, direction='R', lineColor='r')
sp.drawArrow(xtmp+1, xtmp+1, ytmp, ytmp+1, headlength=0.05, direction='U', lineColor='r')
sp.drawFinalVector(0, -0.05, -0.01, 0, xtmp+1, ytmp+1, stepsize=.1, colorVar='g')
sp.pngSave('vecTester')

# check how/whether getFinalCoord is working
sp.getFinalCoord(0, -0.05, -0.01, 0, 5.4, 2.1)

# convert png output to gif (for use in Tkinter)
import pngToGif
pngToGif.pngToGif('reinfTester4')
