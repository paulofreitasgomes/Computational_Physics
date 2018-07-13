import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#Nagentes(i), "|", dados(i, 1) / real(s), "|", dados(i, 2) / real(s), "|", s 
dados_names = ['delta','custo','nviz','amostras']

folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/"

folder2 = folder +'dinamica10_Sandro/res46/C_vs_delta/res46ip/'

dados1 = pd.read_csv(folder2+'dados_46i.txt', header = None, sep = '|')
dados1.columns = dados_names

dados2 = pd.read_csv(folder2+'dados_46j.txt', header = None, sep = '|')
dados2.columns = dados_names

dados3 = pd.read_csv(folder2+'dados_46k.txt', header = None, sep = '|')
dados3.columns = dados_names

dados4 = pd.read_csv(folder2+'dados_46l.txt', header = None, sep = '|')
dados4.columns = dados_names

dados5 = pd.read_csv(folder2+'dados_46m.txt', header = None, sep = '|')
dados5.columns = dados_names

dados6 = pd.read_csv(folder2+'dados_46n.txt', header = None, sep = '|')
dados6.columns = dados_names

dados7 = pd.read_csv(folder2+'dados_46o.txt', header = None, sep = '|')
dados7.columns = dados_names

dados8 = pd.read_csv(folder2+'dados_46p.txt', header = None, sep = '|')
dados8.columns = dados_names

folder3 = folder +'dinamica10_Sandro/res58/res58gl/'

dados9 = pd.read_csv(folder3+'dados_58g.txt', header = None, sep = '|')
dados9.columns = dados_names

dados10 = pd.read_csv(folder3+'dados_58h.txt', header = None, sep = '|')
dados10.columns = dados_names

dados11 = pd.read_csv(folder3+'dados_58i.txt', header = None, sep = '|')
dados11.columns = dados_names

dados12 = pd.read_csv(folder3+'dados_58j.txt', header = None, sep = '|')
dados12.columns = dados_names

dados13 = pd.read_csv(folder3+'dados_58k.txt', header = None, sep = '|')
dados13.columns = dados_names

dados14 = pd.read_csv(folder3+'dados_58l.txt', header = None, sep = '|')
dados14.columns = dados_names

folder4 = folder +'dinamica11_random/res61/'

dados15 = pd.read_csv(folder4+'dados_61.txt', header = None, sep = '|')
dados15.columns = dados_names

linhas1 = dados1.shape[0]
lista1e9x, lista1e9y = [], []
lista2e11x, lista2e11y = [], []
lista8e14x, lista8e14y = [], []

for i1 in range(linhas1):
    lista1e9x.append(dados1.delta[i1])
    lista1e9y.append(dados1.custo[i1])
    lista2e11x.append(dados2.delta[i1])
    lista2e11y.append(dados2.custo[i1])
    lista8e14x.append(dados8.delta[i1])
    lista8e14y.append(dados8.custo[i1])
    
linhas9 = dados9.shape[0]
for i1 in range(linhas9):
    lista1e9x.append(dados9.delta[i1])
    lista1e9y.append(dados9.custo[i1])
    lista2e11x.append(dados11.delta[i1])
    lista2e11y.append(dados11.custo[i1])
    lista8e14x.append(dados14.delta[i1])
    lista8e14y.append(dados14.custo[i1])

#semilogy
#plt.semilogy(dados8.delta,dados8.custo,'Dg', ms = 4, label = r'$v_0 = 5.0$')
#plt.semilogy(dados14.delta,dados14.custo,'Dg', ms = 4)#, label = ' ' )
#plt.semilogy(dados1.delta,dados1.custo,'or', ms = 4, label = r'$v_0 = 0.0$')
#plt.semilogy(dados9.delta,dados9.custo,'or', ms = 4)#, label = ' ')
#plt.semilogy(dados2.delta,dados2.custo,'sb', ms = 4, label = r'$v_0 = 0.5$')
#plt.semilogy(dados11.delta,dados11.custo,'sb', ms = 4)#, label = ' ')

plt.semilogy(lista1e9x,lista1e9y,'or', ms = 4, label = r'$v_0 = 0.0$')
plt.semilogy(lista2e11x,lista2e11y,'^g', ms = 4, label = r'$v_0 = 0.5$')
plt.semilogy(lista8e14x,lista8e14y,'sb', ms = 4, label = r'$v_0 = 5.0$')
plt.semilogy(dados15.delta,dados15.custo,'Dk', ms = 4, label = r'\textit{annealed}',
 markeredgewidth=1, markeredgecolor='k', markerfacecolor = 'None',)
plt.legend(loc='upper left',fontsize = 10)
plt.xlabel(r'Interaction distance $\delta$',fontsize = 16)
plt.ylabel(r'Computational cost $C$',fontsize = 16)
plt.title(r'Caso \textit{quenched}: relevo $K = 4$, $M = 53$.',fontsize=14)
plt.grid(True)
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
axes.set_xlim([1.0,4.0])
#axes.set_ylim([0.7,1.0])
#plt.text(1.1,3.1,r'$M=53$',fontsize = 14)#, color = 'b', backgroundcolor = 'w')
plt.savefig('figura_7.pdf',dpi = 300, bbox_inches='tight') 
plt.close()
