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
y1 = side/2 - separation/2
x2 = side/2 - separation/2
y2 = side/2 - separation/2
x3 = side/2
y3 = side/2 + separation/2

# Make an array to store the heights
xi = empty([points,points],float)

# Calculate the values in the array
for i in range(points):
    y = spacing*i
    for j in range(points):
        x = spacing*j
        r1 = sqrt((x-x1)**2+(y-y1)**2)
        r2 = sqrt((x-x2)**2+(y-y2)**2)
        r3 = sqrt((x-x3)**2+(y-y3)**2)
        xi[i,j] = xi0*sin(k*r1) + xi0*sin(k*r2) + xi0*sin(k*r3)


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
pylab.plot(x1,y1,'ow', ms = 15)
pylab.plot(x2,y2,'ow', ms = 15)
pylab.plot(x3,y3,'ow', ms = 15)
pylab.imshow(xi,origin="lower",extent=[0,side,0,side])
clb = pylab.colorbar()
clb.set_label(r'$h(x,y)$', fontsize = 20, labelpad=-10, y=1.07, rotation=0)
pylab.title("Ondas na agua: 3 fontes", fontsize = 20)
pylab.xlabel("$x$ (cm)", fontsize = 20)
pylab.ylabel("$y$ (cm)", fontsize = 20)
pylab.savefig('ondas_3.pdf', dpi = 200)
pylab.show()
