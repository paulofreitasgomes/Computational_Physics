import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

folderK4 = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/Calibracao/referencia/K4/"
nome = ['0','01', '03', '05b']
Nn = len(nome)
copy =[0.0, 0.1, 0.3, 0.5] 
tipo = ['or', '^g', 'vb', 'sk']
lista_L, lista_cost = [[] for i2 in range(Nn)], [[] for i2 in range(Nn)]
for i1 in range(Nn):
	file_p0 = open(folderK4+'custo_'+nome[i1]+'.txt',"r")
	for linha in file_p0:
		a1, b1 = linha.split()
		lista_L[i1].append(int(a1))
		lista_cost[i1].append(float(b1))
	file_p0.close()

vetorNv = pd.read_csv('vetorNv14.txt', header = None, sep = '|')
N = 12
sizeL = np.array(vetorNv)
Nl = len(sizeL)
ct = np.zeros(Nl, dtype = float)
ct2 = np.zeros(Nl, dtype = float)
lambdaN = 0.99978
for i3 in range(Nl):
	ct[i3] = sizeL[i3]/(2**N*(1-lambdaN**sizeL[i3]))
	ct2[i3] = sizeL[i3]/(2**N)
    
['or', '^g', 'vb', 'sk']

#plt.loglog(sizeL,ct,'-g',lw = 2, label = 'Eq. 4')

plt.loglog(lista_L[0],lista_cost[0],'or', label = r'$p=0.0$')
plt.loglog(lista_L[1],lista_cost[1],'^g', label = r'$p=0.1$')
plt.loglog(lista_L[2],lista_cost[2],'vb', label = r'$p=0.3$')
plt.loglog(lista_L[3],lista_cost[3],'sk', label = r'$p=0.5$')
plt.loglog(sizeL,ct2,'--m',lw = 2, label = r'$L/2^N$')
plt.legend(loc='upper left',fontsize = 10)
plt.xlabel(r'Number of agents $M$',fontsize = 16)
plt.ylabel(r'Computational cost $C$',fontsize = 16)
plt.title(r'Static case: $K=4$.',fontsize=16)
plt.grid(True)
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
axes.set_xlim([2,3e3])
axes.set_ylim([5.5e-1,10])
#plt.text(140,1.3,r'$v=v_0 R \Phi_g$',fontsize = 15, color = 'b', backgroundcolor = 'w')
plt.savefig('figura_2.pdf',dpi = 300, bbox_inches='tight') 
plt.close()
