import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#Nagentes(i), "|", dados(i, 1) / real(s), "|", dados(i, 2) / real(s), "|", s 
dados_names = ['Nv','custo','nviz','amostras']

folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/"

folder2 = folder +'dinamica10_Sandro/res47/res47ip/'

dados1 = pd.read_csv(folder2+'dados_47i.txt', header = None, sep = '|')
dados1.columns = dados_names

dados2 = pd.read_csv(folder2+'dados_47j.txt', header = None, sep = '|')
dados2.columns = dados_names

dados3 = pd.read_csv(folder2+'dados_47k.txt', header = None, sep = '|')
dados3.columns = dados_names

dados4 = pd.read_csv(folder2+'dados_47l.txt', header = None, sep = '|')
dados4.columns = dados_names

dados5 = pd.read_csv(folder2+'dados_47m.txt', header = None, sep = '|')
dados5.columns = dados_names

dados6 = pd.read_csv(folder2+'dados_47n.txt', header = None, sep = '|')
dados6.columns = dados_names

dados7 = pd.read_csv(folder2+'dados_47o.txt', header = None, sep = '|')
dados7.columns = dados_names

dados8 = pd.read_csv(folder2+'dados_47p.txt', header = None, sep = '|')
dados8.columns = dados_names

folder4 = folder +'dinamica10_Sandro/res45/res45aj/'

dados9 = pd.read_csv(folder4+'dados_45a.txt', header = None, sep = '|')
dados9.columns = dados_names

folder3 = folder +'dinamica10_Sandro/res45/res45kr/'

dados10 = pd.read_csv(folder3+'dados_45k.txt', header = None, sep = '|')
dados10.columns = dados_names


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

vetorNv = pd.read_csv(folder3+'vetorNv14.txt', header = None, sep = '|')
N = 12
sizeL = np.array(vetorNv)
Nl = len(sizeL)
ct = np.zeros(Nl, dtype = float)
ct2 = np.zeros(Nl, dtype = float)
lambdaN = 0.99978
for i3 in range(Nl):
	ct[i3] = sizeL[i3]/(2**N*(1-lambdaN**sizeL[i3]))
	ct2[i3] = sizeL[i3]/(2**N)


plt.loglog(lista_L[3],lista_cost[3],'-k', label = 'static')
plt.loglog(dados8.Nv,dados8.custo,'or', ms = 5, label = r'$\delta = 20 $')
plt.loglog(dados7.Nv,dados7.custo,'^y', ms = 5, label = r'$\delta = 5.0 $')
#plt.loglog(dados6.Nv,dados6.custo,'--g', ms = 4, label = r'$\delta = 4.0 $')
plt.loglog(dados5.Nv,dados5.custo,'vg', ms = 5, label = r'$\delta = 3.0 $')
plt.loglog(dados4.Nv,dados4.custo,'1', color = 'orange', ms = 5, label = r'$\delta = 2.5 $')
plt.loglog(dados9.Nv,dados9.custo,'pm', ms = 5, label = r'$\delta = 2.0 $')
#plt.loglog(dados10.Nv,dados10.custo,'--g', ms = 4, label = r'$\delta = 1.5 $')
plt.loglog(dados3.Nv,dados3.custo,'dc', ms = 5, label = r'$\delta = 1.0 $')
plt.loglog(dados2.Nv,dados2.custo,'pk', ms = 5, label = r'$\delta = 0.5 $')
plt.loglog(dados1.Nv,dados1.custo,'sb', ms = 5, label = r'$\delta = 0.25 $')
#plt.loglog(dados9.Nv,dados9.custo,'--y', ms = 4, label = r'$v_0 = 100 $')
#plt.loglog(dados10.Nv,dados10.custo,'--b', ms = 4, label = r'$v_0 = 100 $')
#plt.loglog(sizeL,ct2,'--', color = 'gray',lw = 2, label = r'$L/2^N$')
#plt.loglog(lista_L[3],lista_cost[3],'-', color = 'gray', label = 'static')
#plt.loglog(sizeL,ct,'-g',lw = 2, label = 'Eq. 4')
#plt.loglog(sizeL,ct2,'--k',lw = 2, label = r'$L/2^N$')
plt.legend(loc='upper left',fontsize = 10)
plt.xlabel(r'Number of agents $M$',fontsize = 16)
plt.ylabel(r'Computational cost $C$',fontsize = 16)
plt.title(r'Quenched: $K = 4$, $v_0 = 0$.',fontsize=14)
plt.grid(True)
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
axes.set_xlim([2,3e3])
axes.set_ylim([5.5e-1,10])
#plt.text(2.5,1.8,r'$v_0 =0$',fontsize = 14, color = 'k', backgroundcolor = 'w')
#plt.text(2.5,1.6,r'$K =4$',fontsize = 14, color = 'k', backgroundcolor = 'w')
plt.savefig('figura_9a.pdf',dpi = 300, bbox_inches='tight') 
plt.close()


plt.loglog(dados1.Nv,dados1.Nv-1,'-k', ms = 5, label = r'$N_v-1$')
plt.loglog(dados8.Nv,dados8.nviz,'or', ms = 5, label = r'$\delta = 20 $')
plt.loglog(dados7.Nv,dados7.nviz,'^y', ms = 5, label = r'$\delta = 5.0 $')
#plt.loglog(dados6.Nv,dados6.nviz,'--g', ms = 4, label = r'$\delta = 4.0 $')
plt.loglog(dados5.Nv,dados5.nviz,'vg', ms = 5, label = r'$\delta = 3.0 $')
plt.loglog(dados4.Nv,dados4.nviz,'1', color = 'orange', ms = 5, label = r'$\delta = 2.5 $')
plt.loglog(dados9.Nv,dados9.nviz,'pm', ms = 5, label = r'$\delta = 2.0 $')
#plt.loglog(dados10.Nv,dados10.nviz,'--g', ms = 4, label = r'$\delta = 1.5 $')
plt.loglog(dados3.Nv,dados3.nviz,'dc', ms = 5, label = r'$\delta = 1.0 $')
plt.loglog(dados2.Nv,dados2.nviz,'pk', ms = 5, label = r'$\delta = 0.5 $')
plt.loglog(dados1.Nv,dados1.nviz,'sb', ms = 5, label = r'$\delta = 0.25 $')
plt.legend(loc='upper left',fontsize = 10)
plt.xlabel(r'Number of agents $M$',fontsize = 16)
plt.ylabel(r'Number of neighbors',fontsize = 16)
plt.title(r'Quenched: $K = 4$, $v_0 = 0$.',fontsize=14)
plt.grid(True)
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
axes.set_xlim([2,3e3])
axes.set_ylim([1e-1,1e3])
#plt.text(140,1.3,r'$v=v_0 R \Phi_g$',fontsize = 15, color = 'b', backgroundcolor = 'w')
plt.savefig('figura_9b.pdf',dpi = 300, bbox_inches='tight') 
plt.close()
