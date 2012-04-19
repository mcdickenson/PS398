#!usr/local/bin/python
# /Users/mcdickenson/github/PS398/FinalProj/

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from pylab import *
from numpy import arange, sin, pi


# a straight line
pyplot.plot([1,2,3]) 
pyplot.savefig('example1.png')
pyplot.close()

# an M shape
pyplot.plot([1,3,1,3,1])
pyplot.savefig('example2.png')
pyplot.close()

# 2 sine curves
t = arange(0.0, 1.0, 0.01)

fig = figure(1)

ax1 = fig.add_subplot(211)
ax1.plot(t, sin(2*pi*t))
ax1.grid(True)
ax1.set_ylim( (-2,2) )
ax1.set_ylabel('1 Hz')
ax1.set_title('A sine wave or two')

for label in ax1.get_xticklabels():
    label.set_color('r')

ax2 = fig.add_subplot(212)
ax2.plot(t, sin(2*2*pi*t))
ax2.grid(True)
ax2.set_ylim( (-2,2) )
l = ax2.set_xlabel('See?')
l.set_color('g')
l.set_fontsize('large')
pyplot.savefig('example3.png')

# a slope field
# settings
X,Y = meshgrid( arange(0,2*pi,.2),arange(0,2*pi,.2) )
U = cos(X)
V = sin(Y)

# create the slopefield
figure()
Q = quiver( U, V)
qk = quiverkey(Q, 0.5, 0.92, 2, r'$2 \frac{m}{s}$', labelpos='W',
               fontproperties={'weight': 'bold'})
l,r,b,t = axis()
dx, dy = r-l, t-b
axis([l-0.05*dx, r+0.05*dx, b-0.05*dy, t+0.05*dy])
title('Minimal arguments')
pyplot.savefig('example4.png')
