"""
http://www-personal.umich.edu/~mejn/cp/
"""


import matplotlib.pyplot as plt
from math import sqrt,sin,pi
from numpy import empty
import pylab

wavelength = 5.0
k = 2*pi/wavelength
xi0 = 1.0
separation = 20.0      # Separation of centers in cm
side = 100.0           # Side of the square in cm
points = 500           # Number of grid points along each side
spacing = side/points  # Spacing of points in cm


# Calculate the positions of the centers of the circles
x1 = side/2 + separation/2
y1 = side/2
x2 = side/2 - separation/2
y2 = side/2

# Make an array to store the heights
xi = empty([points,points],float)

# Calculate the values in the array
for i in range(points):
    y = spacing*i
    for j in range(points):
        x = spacing*j
        r1 = sqrt((x-x1)**2+(y-y1)**2)
        r2 = sqrt((x-x2)**2+(y-y2)**2)
        xi[i,j] = xi0*sin(k*r1) + xi0*sin(k*r2)


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
pylab.imshow(xi,origin="lower",extent=[0,side,0,side])
pylab.plot(x1,y1,'ok', ms = 16)
pylab.plot(x2,y2,'ok', ms = 16)
clb = pylab.colorbar()
clb.set_label(r'$h(x,y)$', fontsize = 20, labelpad=-10, y=1.07, rotation=0)
pylab.title("Ondas na agua: duas fontes", fontsize = 20)
pylab.xlabel("$x$ (cm)", fontsize = 20)
pylab.ylabel("$y$ (cm)", fontsize = 20)
pylab.savefig('ondas_2.pdf', dpi = 200)
pylab.show()
