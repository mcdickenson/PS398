#!usr/local/bin/python
# /Users/mcdickenson/github/PS398/FinalProj/

# load packages
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from pylab import *
from numpy import arange, sin, pi

def slopefieldPlotter(xMin, xMax, xInterval, yMin, yMax, yInterval, dXy, dYx, xLab='', yLab='', mainLab='', drawAxes=True, filename='default'):
    # set params
    global X, Y
    X,Y = meshgrid( arange(xMin,xMax,xInterval),arange(yMin,yMax,yInterval) )
    dX = dXy*Y
    dY = dYx*X

    # draw figure
    fig = figure()
    Q = quiver(X, Y, dX, dY, scale=4, scale_units='width', pivot='mid')

    # set dimensions and labels
    axis([xMin, xMax, -yMin, yMax])
    ax = fig.add_subplot(111)
    ax.xaxis.set_label_text(xLab)
    ax.yaxis.set_label_text(yLab)

    # add lines at axes and title
    if drawAxes==True:
        xl = Line2D([xMin,xMax],[0,0])
        yl = Line2D([0,0],[yMin,yMax])
        ax.add_line(xl)
        ax.add_line(yl)
    title(mainLab)

    # save file
    pngSave(filename)

def pngSave(name):
    pngName = str(name) + '.png'
    pyplot.savefig(pngName)

# draw curve (line) taking initial value
def drawVector(dXx, dXy, dYx, dYy, X0, Y0, numsteps, stepsize=0.01, colorVar='b'): # currently implemented for implicit diffEq's
    xCoords = [X0]
    yCoords = [Y0]

    # compute coordinates using Euler's method
    for i in range(1,numsteps): # maybe numsteps+1
        if i == 1: # first time thru
            x_tk = X0+((dXx*X0)+(dXy*X0))*stepsize
            y_tk = Y0+((dYx*X0)+(dYy*Y0))*stepsize
        else:
            x_tk_last = x_tk
            y_tk_last = y_tk
            x_tk = x_tk_last+((dXx*x_tk_last)+(dXy*y_tk_last))*stepsize
            y_tk = y_tk_last+((dYx*x_tk_last)+(dYy*y_tk_last))*stepsize
        xCoords.append(x_tk)
        yCoords.append(y_tk)

    pyplot.plot(xCoords, yCoords, color=colorVar)

#TODO: add options for whether to print every arrow, every third arrow, etc
#TODO: add color options
#TODO: make it easier to pass coefficient parameters
# will need dX, dY w/r/t X,Y,dX,dY,t

# Examples
# Iwo Jima, no reinforcements
slopefieldPlotter(0, 6, .2, 0, 3, .2, -0.05, -0.01, xLab='US', yLab='Japan', mainLab='Lanchester Squares, No Reinforcements', drawAxes=True, filename='lanchTester')
drawVector(0, -0.05, -0.01, 0, 5.4, 2.15, 650, stepsize=0.1)
pngSave('lanchTester2')

# Iwo Jima, reinforcement example
slopefieldPlotter(0, 6, .2, 0, 3, .2, -0.05, -0.01, xLab='US', yLab='Japan', mainLab='Lanchester Squares, With Reinforcements', drawAxes=True, filename='reinfTester')
drawVector(0, -0.05, -0.01, 0, 5.4, 2.15, 300, stepsize=0.1, colorVar='b')
pngSave('reinfTester2')
pyplot.plot([3.2,5.05],[.9,.9], color='r')
pyplot.plot([5.05,4.9],[.9,.95], color='r')
pyplot.plot([5.05,4.9],[.9,.85], color='r')
pngSave('reinfTester3')
drawVector(0, -0.05, -0.01, 0, 5.1, 0.9, 200, stepsize=0.1, colorVar='b')
pngSave('reinfTester4')

# TODO: for reinforcements, have an option to return last xcoord, ycoord
