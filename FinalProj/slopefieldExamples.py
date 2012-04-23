#!usr/local/bin/python
# /Users/mcdickenson/github/PS398/FinalProj/
# Examples for slopefieldPlot.py
import slopefieldPlot


# Iwo Jima, no reinforcements
slopefieldPlotter(0, 6, .2, 0, 3, .2, -0.05, -0.01, xLab='US', yLab='Japan', mainLab='Lanchester Squares, No Reinforcements', drawAxes=True, filename='lanchTester')
drawVector(0, -0.05, -0.01, 0, 5.4, 2.15, 650, stepsize=0.1)
pngSave('lanchTester2')

# Iwo Jima, reinforcement example
slopefieldPlotter(0, 6, .2, 0, 3, .2, -0.05, -0.01, xLab='US', yLab='Japan', mainLab='Lanchester Squares, With Reinforcements', drawAxes=True, filename='reinfTester')
drawVector(0, -0.05, -0.01, 0, 5.4, 2.15, 300, stepsize=0.1, colorVar='b')
pngSave('reinfTester2')
drawArrow(3.2, 5.05, .9, .9, headlength=0.05, direction='R', lineColor='r')
#pyplot.plot([3.2,5.05],[.9,.9], color='r')
#pyplot.plot([5.05,4.9],[.9,.95], color='r')
#pyplot.plot([5.05,4.9],[.9,.85], color='r')
pngSave('reinfTester3')
drawVector(0, -0.05, -0.01, 0, 5.1, 0.9, 200, stepsize=0.1, colorVar='b')
pngSave('reinfTester4')

# demonstrate arrow plot (on top of existing plot)
drawArrow(1, 0, .9, .9, headlength=0.05, direction='L', lineColor='g')
drawArrow(1, 1, .5, 2.0, headlength=0.1, direction='U', lineColor='b')
drawArrow(2, 2, 2.5, 1.0, headlength=0.01, direction='D', lineColor='y')
pngSave('arrowTester')

# TODO: for reinforcements, have an option to return last xcoord, ycoord

# convert png output to gif (for use in Tkinter)
import pngToGif
pngToGif.pngToGif('reinfTester4')
