import matplotlib.pyplot as plt
import numpy as np
import math

omega = 1.0
alfa = 1.2
delta = 1.3
teta = 1.4
a = 1.5
b = 2.0
c = 2.5
tempo = np.linspace(0,2*math.pi/omega,50)
n = 0
for t in tempo:
	plt.clf()
	#sol
	plt.scatter(0,0, s=250, marker= 'o', color="yellow")
	#Planet1
	plt.scatter(math.cos(t*delta), math.sin(t*delta), s=250, marker= 'o', color="r")
	#Planet2
	plt.scatter(math.cos(t*alfa)*a, math.sin(t*alfa)*a, s=250, marker= 'o', color="b")
	#Planet3
	plt.scatter(math.cos(t*omega)*b, math.sin(t*omega)*b, s=250, marker= 'o', color="purple")
	#Planet4
	#plt.scatter(math.cos(t*alfa+c), math.sin(t*alfa), s=250, marker= 'o', color="black")
	plt.xticks([])
	plt.yticks([])
	axes = plt.gca()
	axes.set_xlim([-5,5])
	axes.set_ylim([-5,5])
	plt.savefig('imagens/nome_'+str(n)+'.png')
	n += 1
	#plt.show()
