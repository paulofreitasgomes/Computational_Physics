import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#Nagentes(i), "|", dados(i, 1) / real(s), "|", dados(i, 2) / real(s), "|", s 
dados_names = ['Nv','custo','nviz','amostras']

folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/"

folder2 = folder +'dinamica10_principal/K0/res60ip/'

dados1 = pd.read_csv(folder2+'dados_60i.txt', header = None, sep = '|')
dados1.columns = dados_names

dados2 = pd.read_csv(folder2+'dados_60j.txt', header = None, sep = '|')
dados2.columns = dados_names

dados3 = pd.read_csv(folder2+'dados_60k.txt', header = None, sep = '|')
dados3.columns = dados_names

dados4 = pd.read_csv(folder2+'dados_60l.txt', header = None, sep = '|')
dados4.columns = dados_names

dados5 = pd.read_csv(folder2+'dados_60m.txt', header = None, sep = '|')
dados5.columns = dados_names

dados6 = pd.read_csv(folder2+'dados_60n.txt', header = None, sep = '|')
dados6.columns = dados_names

dados7 = pd.read_csv(folder2+'dados_60o.txt', header = None, sep = '|')
dados7.columns = dados_names

dados8 = pd.read_csv(folder2+'dados_60p.txt', header = None, sep = '|')
dados8.columns = dados_names


#Importando os dados do caso aleatorio

folder3 = folder +'dinamica11_random/res50ip/'

dados11 = pd.read_csv(folder3+'dados_50k.txt', header = None, sep = '|')
dados11.columns = dados_names


folderK0GT0 = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/Calibracao/referencia/K0pGT0/"
nome = ['0','01', '03', '05']
Nn = len(nome)
copy =[0.0, 0.1, 0.3, 0.5] 
tipo = ['or', '^g', 'vb', 'sk']
lista_L, lista_cost = [[] for i2 in range(Nn)], [[] for i2 in range(Nn)]
for i1 in range(Nn):
    file_p0 = open(folderK0GT0+'cost3_K0_p'+nome[i1]+'.txt',"r")
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


plt.loglog(dados1.Nv,dados1.custo,'sr', ms = 4, label = r'$v_0 = 0.0 $')
#plt.loglog(dados2.Nv,dados2.custo,'^g', ms = 4, label = r'$v_0 = 0.25 $')
#plt.loglog(dados3.Nv,dados3.custo,'pm', ms = 4, label = r'$v_0 = 0.5 $')
#plt.loglog(dados4.Nv,dados4.custo,'vc', ms = 4, label = r'$v_0 = 1.0 $')
#plt.loglog(dados5.Nv,dados5.custo,'-og', ms = 4, label = r'$v_0 = 2.0 $')
#plt.loglog(dados6.Nv,dados6.custo,'-v', color = 'orange', ms = 4, label = r'$v_0 = 5 $')
#plt.loglog(dados7.Nv,dados7.custo,'-1c', ms = 4, label = r'$v_0 = 10 $')
plt.loglog(dados8.Nv,dados8.custo,'ob', ms = 4, label = r'$v_0 = 100 $')
#markeredgewidth=1, markeredgecolor='c', markerfacecolor = 'None',)
#plt.loglog(sizeL,ct2,'--', color = 'gray',lw = 2, label = r'$L/2^N$')
plt.loglog(lista_L[3],lista_cost[3],'-', lw = 2, color = 'k', label = 'static')
plt.axvline(x=12.5,color='darkred', linestyle='--')
#plt.loglog(lista_L[3],lista_cost[3],'-k', label = 'static')
plt.legend(loc='lower right',fontsize = 12)
plt.xlabel(r'Number of agents $M$',fontsize = 16)
plt.ylabel(r'Computational cost $C$',fontsize = 16)
plt.title(r'Caso \textit{quenched}: relevo $K = 0$, $\delta = 2.0$.',fontsize=14)
plt.grid(True)
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
axes.set_xlim([2,2e3])
axes.set_ylim([0.07,1.0])
#plt.text(130,1.6,r'$\delta = 2.0$',fontsize = 14)#, color = 'b', backgroundcolor = 'w')
plt.savefig('figura_14b.pdf',dpi = 300, bbox_inches='tight') 
plt.close()
