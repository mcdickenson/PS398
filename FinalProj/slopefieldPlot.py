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

def drawFinalVector(dXx, dXy, dYx, dYy, X0, Y0, stepsize=.1, colorVar='b'): # currently implemented for implicit diffEq's
    xCoords = [X0]
    yCoords = [Y0]
    x_tk = X0+((dXx*X0)+(dXy*X0))*stepsize
    y_tk = Y0+((dYx*X0)+(dYy*Y0))*stepsize
    xCoords.append(x_tk)
    yCoords.append(y_tk)
    x_tk_last = x_tk
    y_tk_last = y_tk
    # compute coordinates using Euler's method
    while (x_tk > -0.01) & (y_tk > -0.01) & (x_tk_last > 0) & (y_tk_last > 0): 
        x_tk_last = x_tk
        y_tk_last = y_tk
        x_tk = x_tk_last+((dXx*x_tk_last)+(dXy*y_tk_last))*stepsize
        y_tk = y_tk_last+((dYx*x_tk_last)+(dYy*y_tk_last))*stepsize
        xCoords.append(x_tk)
        yCoords.append(y_tk)

    pyplot.plot(xCoords, yCoords, color=colorVar)

def getEndVector(dXx, dXy, dYx, dYy, X0, Y0, numsteps, stepsize=0.01): # find where vector ends
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

    return round(x_tk, 2), round(y_tk,2) # may want to avoid rounding

def drawArrow(x1, x2, y1, y2, headlength=0.05, direction='R', lineColor='r'):
    pyplot.plot([x1, x2], [y1, y2], color = lineColor)

    if direction == 'R':
        pyplot.plot([x2,x2-(headlength*2)],[y2,y2+headlength], color=lineColor)
        pyplot.plot([x2,x2-(headlength*2)],[y2,y2-headlength], color=lineColor)

    elif direction == 'L':
        pyplot.plot([x2,x2+(headlength*2)],[y2,y2+headlength], color=lineColor)
        pyplot.plot([x2,x2+(headlength*2)],[y2,y2-headlength], color=lineColor)

    elif direction == 'U':
        pyplot.plot([x2,x2-headlength], [y2,y2-(headlength*2)], color=lineColor)
        pyplot.plot([x2,x2+headlength], [y2,y2-(headlength*2)], color=lineColor)

    elif direction == 'D':
        pyplot.plot([x2,x2-headlength], [y2,y2+(headlength*2)], color=lineColor)
        pyplot.plot([x2,x2+headlength], [y2,y2+(headlength*2)], color=lineColor)

def pngSave(name):
    pngName = str(name) + '.png'
    pyplot.savefig(pngName)

