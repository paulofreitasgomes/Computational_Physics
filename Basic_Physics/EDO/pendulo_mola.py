from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import *

N = 600 #numero de passos
#quanto maior, mais suave sera o grafico final
# 400 ja da um grafico suave

"""
Temos 4  parametros para determinar: L, Ldot, theta e thetadot
Assim, iremos usar um vetor de 4 dimensoes para representar o estado do sistema
Cada linha desse vetor representa o sistema em um instante. 
As diferentes linhas estao separadas por dt.
"""

def spring_pendulum(y,time):
	g0 = y[1]
	g1 = (L0+y[0])*y[3]**2 - k/m*y[0] + gravity * math.cos(y[2])
	g2 = y[3]
	g3 = -(gravity * math.sin(y[2]) + 2.0*y[1]*y[3])/(L0+y[0])
	return np.array([g0, g1, g2, g3])

"""
Esta funcao define as equacoes diferenciais. 
"""

y = np.zeros([4]) #cria o vetor de estado

#Parametros iniciais
L0 = 1.0 #comprimento no equilibrio
L = 1.0 #comprimento esticado inicial
v0 = 0.0 #velocidade inicial
theta0 = 0.3 #angulo inicial em radianos
omega0 = 0.0 #velocidade angular inicial

#Definindo o estado inicial

y[0] = L
y[1] = v0
y[2] = theta0
y[3] = omega0

time = np.linspace(0,25,N) #cria o vetor do tempo

k = 3.5 #constante da mola em N/m
m = 0.2 # massa, em kg
gravity = 9.8 #g, em m/s2

#Fazendo os calculos
answer = odeint(spring_pendulum, y, time)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.title('Evolucao temporal',fontsize=20)
plt.plot(time,answer[:,0], '-b', lw = 3, label = r'$L(t)$')
plt.plot(time,answer[:,2], '-r', lw = 3, label = r'$\theta(t)$')
plt.xlabel("Tempo $t$ (s)", fontsize = 20)
plt.ylabel("Comprimento e angulo", fontsize = 20)
plt.legend(loc='upper right',fontsize = 20)
plt.xticks(color='k', size=20)
plt.yticks(color='k', size=20)
plt.grid(True)
plt.savefig('evolucao.pdf')
plt.show()
plt.close()


#Graficos
xdata = (L0 + answer[:,0])*sin(answer[:,2])
ydata = -(L0 + answer[:,0])*cos(answer[:,2])

Npontos = len(ydata)

print answer.shape

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.title('Trajetoria da massa em funcao do tempo',fontsize=20)
plt.plot(xdata,ydata, '-b', lw = 4)
plt.plot(xdata[0],ydata[0], 'or', ms = 12, label = r'$\vec{r}(0)$')
plt.plot(xdata[Npontos-1],ydata[Npontos-1], 'ok', ms = 12, label = r'$\vec{r}(t_f)$')
plt.xlabel("Posicao horizontal $x(t)$", fontsize = 20)
plt.ylabel("Posicao vertical $y(t)$", fontsize = 20)
plt.legend(loc='lower center',fontsize = 20)
plt.xticks(color='k', size=20)
plt.yticks(color='k', size=20)
plt.grid(True)
plt.savefig('trajetoria.pdf')
plt.show()
plt.close()
