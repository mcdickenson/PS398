# settings#!usr/local/bin/python
# /Users/mcdickenson/github/PS398/FinalProj/

# load packages
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
#from matplotlib import axis
from pylab import *
from numpy import arange, sin, pi

# set parameters
X,Y = meshgrid( arange(0,6,.2),arange(0,6,.2) )
U = -0.05*Y
V = -0.01*X

# create the slopefield
fig = figure()
Q = quiver(X, Y, U, V)

axis([0, 6, 0, 6])

majorLocator   = MultipleLocator(20)
majorFormatter = FormatStrFormatter('%d')
minorLocator   = MultipleLocator(5)
#ax.xaxis.set_major_locator(majorLocator)
#ax.xaxis.set_major_formatter(majorFormatter)
ax = fig.add_subplot(111)

#ax.xaxis.set_ticklabels(['0','1', '2','3','4','5','6'])
ax.xaxis.set_label_text('US')
#ax.yaxis.set_ticklabels(['0','1', '2','3','4','5','6'])
ax.yaxis.set_label_text('Japan')

title('Lanchester Squares, Iwo Jima')
pyplot.savefig('lanchester1.png')


# another plot with every third arrow
fig = figure()
Q = quiver( X[::3, ::3], Y[::3, ::3], U[::3, ::3], V[::3, ::3],
             color='r', units='x',
            linewidths=(1,), edgecolors=('k'), headaxislength=2 )

axis([0, 6, 0, 6])

majorLocator   = MultipleLocator(20)
majorFormatter = FormatStrFormatter('%d')
minorLocator   = MultipleLocator(5)
#ax.xaxis.set_major_locator(majorLocator)
#ax.xaxis.set_major_formatter(majorFormatter)
ax = fig.add_subplot(111)

#ax.xaxis.set_ticklabels(['0','1', '2','3','4','5','6'])
ax.xaxis.set_label_text('US')
#ax.yaxis.set_ticklabels(['0','1', '2','3','4','5','6'])
ax.yaxis.set_label_text('Japan')

title('Lanchester Squares, Iwo Jima')
pyplot.savefig('lanchester2.png')
