"""
Simple Numerical Laplace Equation Solution using Finite Difference Method
https://www.codeproject.com/Articles/1087025/Using-Python-to-Solve-Computational-Physics-Proble
"""

import numpy as np
import matplotlib.pyplot as plt

# Set maximum iteration
maxIter = 500

# Set Dimension and delta
lenX = lenY = 20 #we set it rectangular
delta = 1

# Boundary condition
Ttop = 100
Tbottom = 0
Tleft = -50
Tright = -100

# Initial guess of interior grid
Tguess = 30

# Set colour interpolation and colour map
colorinterpolation = 50
colourMap = plt.cm.jet #you can try: colourMap = plt.cm.coolwarm

# Set meshgrid
X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

# Set array size and set the interior value with Tguess
T = np.empty((lenX, lenY))
T.fill(Tguess)

# Set Boundary condition
T[(lenY-1):, :] = Ttop
T[:1, :] = Tbottom
T[:, (lenX-1):] = Tright
T[:, :1] = Tleft

# Iteration (We assume that the iteration is convergence in maxIter = 500)
print("Please wait for a moment")
for iteration in range(0, maxIter):
	for i in range(1, lenX-1, delta):
		for j in range(1, lenY-1, delta):
			T[i, j] = 0.25 * (T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])

print("Iteration finished")

# Configure the contour

nome = 'difusao_temperatura1.pdf'

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
contorno1 = '$T_c =$ '+str(Ttop)+', $T_b =$'+str(Tbottom)
contorno2 = ', $T_e =$'+str(Tleft)+', $T_d =$'+str(Tright)
contorno = contorno1 + contorno2


plt.title(contorno, fontsize = 20)
plt.contourf(X, Y, T, colorinterpolation, cmap=colourMap)
#plt.colorbar()
clb = plt.colorbar()
clb.set_label(r'$T(x,y)$', fontsize = 20, labelpad=-10, y=1.07, rotation=0)
plt.xticks(color='k', size=20)
plt.yticks(color='k', size=20)
plt.xlabel('eixo $x$ (cm)', {'color': 'k','fontsize': 20}) #k indica cor preta
plt.ylabel('eixo $y$ (cm)', {'color': 'k','fontsize': 20})
plt.savefig(nome, dpi = 200)
plt.show()

