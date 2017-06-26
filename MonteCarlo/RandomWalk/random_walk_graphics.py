
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Q = 15 #Q - 1 is the maximum value of time
Np = 10 # number of particles

tempo = np.arange(1,Q,1) 
niter = len(tempo) #number of iterations on time

#creating matrices to store the positions of all particles
xp = np.zeros((Np,niter+1)) 
yp = np.zeros((Np,niter+1))
zp = np.zeros((Np,niter+1))

#initial positions
posX = 0.0
posY = 0.0

#the random step can be forward (+1), backward (-1) or none.
for i1 in xrange(Np):	
	for t1 in tempo:
		xp[i1][t1] = xp[i1][t1-1] + random.randint(-1,1)
		yp[i1][t1] = yp[i1][t1-1] + random.randint(-1,1)
		zp[i1][t1] = zp[i1][t1-1] + random.randint(-1,1)
		
#checking the maximum value of displacement in each direction
#to define the range of the axis for the graphic
Lxmax = max(abs(xp[i3][niter]) for i3 in xrange(Np))
Lymax = max(abs(yp[i3][niter]) for i3 in xrange(Np))
Lzmax = max(abs(zp[i3][niter]) for i3 in xrange(Np))

#generating the figures in 2D
for t2 in tempo:
	for i2 in xrange(Np):
		plt.plot(xp[i2][0:t2],yp[i2][0:t2], lw = 2)
	title1 = '2D random walk. $N=$ '+str(Np)+', $t=$ '+str(t2)+'.'
	plt.title(title1)
	plt.xlabel("x",fontsize = 14)
	plt.ylabel("y",fontsize = 14)
	plt.plot(xp[0][0],yp[0][0], 'sk', ms = 7) #marks the initial position
	plt.grid(True)
	axes = plt.gca()
	axes.set_xlim([-Lxmax,Lxmax])
	axes.set_ylim([-Lymax,Lymax])
	plt.savefig("walk2D_"+str(t2)+".png",dpi = 300) 
	plt.close() 
	
#generating the figures in 3D
for t3 in tempo:
	title2 = '3D random walk. $N=$ '+str(Np)+', $t=$ '+str(t3)+'.'
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	for i3 in xrange(Np):
		ax.plot(xp[i3][0:t3], yp[i3][0:t3], zp[i3][0:t3], lw = 2)
	ax.plot([0.0], [0.0], [0.0],'sk', ms = 7)
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('z')
	ax.set_xlim([-Lxmax,Lxmax])
	ax.set_ylim([-Lymax,Lymax])
	ax.set_zlim([-Lzmax,Lzmax])
	ax.set_title(title2)
	plt.savefig('walk3D_'+str(t3)+'.png', dpi = 400)
	plt.close()

