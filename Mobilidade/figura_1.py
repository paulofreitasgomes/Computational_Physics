import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

####################################################################
#folderK4 = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/referencia/K4/"
#folderK0 = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/referencia/K0/"

folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/Calibracao/referencia/K0pGT0/"

nome = ['0','01', '03', '05']
Nn = len(nome)
copy =[0.0, 0.1, 0.3, 0.5] 
tipo = ['or', '^g', 'vb', 'sk']

lista_L, lista_cost = [[] for i2 in range(Nn)], [[] for i2 in range(Nn)]

for i1 in range(Nn):
	file_p0 = open(folder + 'cost3_K0_p'+nome[i1]+'.txt',"r")
	for linha in file_p0:
		a1, b1 = linha.split()
		lista_L[i1].append(int(a1))
		lista_cost[i1].append(float(b1))
	file_p0.close()

N = 12
sizeL = np.array(lista_L[0])
Nl = len(sizeL)
ct = np.zeros(Nl, dtype = float)
ct2 = np.zeros(Nl, dtype = float)
lambdaN = 0.99978
for i3 in range(Nl):
	ct2[i3] = sizeL[i3]/(2**N)
	ct[i3] = sizeL[i3]/(2**N*(1-lambdaN**sizeL[i3]))

for i1 in range(Nn):
	plt.loglog(lista_L[i1],lista_cost[i1], tipo[i1], label = r'$p=$ '+str(copy[i1]))
plt.loglog(sizeL,ct2,'--m',lw = 2, label = r'$L/2^N$')
#plt.loglog(sizeL,ct,'-r',lw = 2, label = 'Eq. 4')
plt.legend(loc='lower right',fontsize = 10)
plt.xlabel(r'Number of agents $M$',fontsize = 16)
plt.ylabel(r'Computational cost $C$',fontsize = 16)
plt.title(r'Static case: $K=0$.',fontsize=16)
plt.grid(True)
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
axes.set_xlim([1,1e4])
axes.set_ylim([6e-2,2])
#plt.text(2,4,r'$N=12$, $K=0$, $N_s = 10^5$.',fontsize = 16, color = 'k', backgroundcolor = 'w')
plt.savefig('figura_1.pdf',dpi = 300, bbox_inches='tight') 
