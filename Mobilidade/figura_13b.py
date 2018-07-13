import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#Nagentes(i), "|", dados(i, 1) / real(s), "|", dados(i, 2) / real(s), "|", s 
dados_names = ['Nv','custo','nviz','amostras']

folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/"

folder2 = folder +'dinamica10_Sandro/res63ad/'

dados1 = pd.read_csv(folder2+'dados_63a.txt', header = None, sep = '|')
dados1.columns = dados_names

dados2 = pd.read_csv(folder2+'dados_63b.txt', header = None, sep = '|')
dados2.columns = dados_names

dados3 = pd.read_csv(folder2+'dados_63c.txt', header = None, sep = '|')
dados3.columns = dados_names

dados4 = pd.read_csv(folder2+'dados_63d.txt', header = None, sep = '|')
dados4.columns = dados_names

#caso v0 = 0

folder3 = folder +'dinamica10_Sandro/res47/res47ip/'
dados47k = pd.read_csv(folder3+'dados_47k.txt', header = None, sep = '|')
dados47k.columns = dados_names

#caso aleatorio

folder4 = folder +'dinamica11_random/res50ip/'
dados50j = pd.read_csv(folder4+'dados_50j.txt', header = None, sep = '|')
dados50j.columns = dados_names
N50j = dados50j.amostras[0]

folder5 = folder +'dinamica11_random/res59ad/'

dados59a = pd.read_csv(folder5+'dados_59a.txt', header = None, sep = '|')
dados59a.columns = dados_names
N59a = dados59a.amostras[0]

dados_random = ( N50j * dados50j.custo + N59a * dados59a.custo ) / ( N50j+N59a )

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

vetorNv = pd.read_csv(folder2+'vetorNv14.txt', header = None, sep = '|')
N = 12
sizeL = np.array(vetorNv)
Nl = len(sizeL)
ct = np.zeros(Nl, dtype = float)
ct2 = np.zeros(Nl, dtype = float)
lambdaN = 0.99978
for i3 in range(Nl):
	ct[i3] = sizeL[i3]/(2**N*(1-lambdaN**sizeL[i3]))
	ct2[i3] = sizeL[i3]/(2**N)


plt.loglog(dados47k.Nv,dados47k.custo,'sb', ms = 4, label = r'$v_0 = 0.0 $')
#markeredgewidth=1, markeredgecolor='r', markerfacecolor = 'None')
plt.loglog(dados1.Nv,dados1.custo,'^g', ms = 4, label = r'$v_0 = 0.5 $')
plt.loglog(dados2.Nv,dados2.custo,'pm', ms = 4, label = r'$v_0 = 1.0 $')
plt.loglog(dados3.Nv,dados3.custo,'vc', ms = 4, label = r'$v_0 = 1.5 $')
plt.loglog(dados4.Nv,dados4.custo,'or', ms = 4, label = r'$v_0 = 100 $')
plt.loglog(dados50j.Nv,dados_random,'Dk', ms = 4, label = r'RN',
 markeredgewidth=1, markeredgecolor='k', markerfacecolor = 'None',)
#plt.loglog(sizeL,ct2,'--', color = 'gray',lw = 2, label = r'$L/2^N$')
plt.loglog(lista_L[3],lista_cost[3],'-', color = 'gray',lw = 2, label = 'static')#
plt.axvline(x=3.1,color='darkred', linestyle='--')
#plt.loglog(lista_L[3],lista_cost[3],'-k', label = 'static')
plt.legend(loc='lower right',fontsize = 10)
plt.xlabel(r'Number of agents $M$',fontsize = 16)
plt.ylabel(r'Computational cost $C$',fontsize = 16)
plt.title(r'Caso \textit{quenched}: relevo $K = 4$, $\delta = 1.0$.',fontsize=14)
plt.grid(True)
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
axes.set_xlim([2,2e3])
axes.set_ylim([6e-1,1.2])
#plt.text(130,1.6,r'$\delta = 2.0$',fontsize = 14)#, color = 'b', backgroundcolor = 'w')
plt.savefig('figura_13b.pdf',dpi = 300, bbox_inches='tight') 
plt.close()
