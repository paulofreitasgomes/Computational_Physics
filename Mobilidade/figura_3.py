import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#Nagentes(i), "|", dados(i, 1) / real(s), "|", dados(i, 2) / real(s), "|", s 
dados_names = ['Nv','custo','nviz','amostras']

folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/dinamica8/res30abcdef/"

dados30a = pd.read_csv(folder+'dados_30a.txt', header = 1, sep = '|')
dados30a.columns = dados_names

dados30b = pd.read_csv(folder+'dados_30b.txt', header = 1, sep = '|')
dados30b.columns = dados_names


dados30c = pd.read_csv(folder+'dados_30c.txt', header = 1, sep = '|')
dados30c.columns = dados_names

dados30d = pd.read_csv(folder+'dados_30d.txt', header = 1, sep = '|')
dados30d.columns = dados_names

dados30e = pd.read_csv(folder+'dados_30e.txt', header = 1, sep = '|')
dados30e.columns = dados_names

dados30f = pd.read_csv(folder+'dados_30f.txt', header = 1, sep = '|')
dados30f.columns = dados_names

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


plt.loglog(dados30a.Nv,dados30a.custo,'-sg', ms = 4, label = r'$v_0 = 5 $')
plt.loglog(dados30b.Nv,dados30b.custo,'--og', ms = 4, label = r'$v_0 = 0 $')
plt.loglog(dados30c.Nv,dados30c.custo,'-sr', ms = 4, label = r'$v_0 = 5 $')
plt.loglog(dados30d.Nv,dados30d.custo,'--or', ms = 4, label = r'$v_0 = 0 $')
plt.loglog(dados30e.Nv,dados30e.custo,'-sb', ms = 4, label = r'$v_0 = 5 $')
plt.loglog(dados30f.Nv,dados30f.custo,'--ob', ms = 4, label = r'$v_0 = 0 $')

#plt.loglog(sizeL,ct2,'--', color = 'gray',lw = 2, label = r'$L/2^N$')
#plt.loglog(lista_L[3],lista_cost[3],'-', color = 'gray', label = 'static')
#plt.loglog(sizeL,ct,'-g',lw = 2, label = 'Eq. 4')
plt.loglog(sizeL,ct2,'--k',lw = 2, label = r'$L/2^N$')
plt.loglog(lista_L[3],lista_cost[3],'-k', label = 'static')
plt.legend(loc='upper left',fontsize = 10)
plt.xlabel(r'Number of agents $M$',fontsize = 16)
plt.ylabel(r'Computational cost $C$',fontsize = 16)
#plt.title(r'$K=4$, $p = 0.5$, $\delta = 2.0$.',fontsize=16)
plt.grid(True)
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
axes.set_xlim([2,6e3])
axes.set_ylim([6e-1,1.9])
plt.text(120,1.7,r'$v_i(t)=v_0 R \Phi_i(t)$',fontsize = 15, color = 'g', backgroundcolor = 'w')
plt.text(120,1.5,r'$v(t)=v_0 R \Phi_M(t)$',fontsize = 15, color = 'r', backgroundcolor = 'w')
plt.text(140,1.3,r'$v=v_0 R \Phi_g$',fontsize = 15, color = 'b', backgroundcolor = 'w')
plt.savefig('figura_3.pdf',dpi = 300, bbox_inches='tight') 
plt.close()
