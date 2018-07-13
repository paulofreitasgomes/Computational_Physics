import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#Nagentes(i), "|", dados(i, 1) / real(s), "|", dados(i, 2) / real(s), "|", s 
dados_names = ['v0','custo','nviz','amostras']

folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/"

folder2 = folder +'dinamica10_Sandro/res46/C_vs_v0/res46ah/'

dados1 = pd.read_csv(folder2+'dados_46a.txt', header = 1, sep = '|')
dados1.columns = dados_names

dados2 = pd.read_csv(folder2+'dados_46b.txt', header = None, sep = '|')
dados2.columns = dados_names

dados3 = pd.read_csv(folder2+'dados_46c.txt', header = None, sep = '|')
dados3.columns = dados_names

dados4 = pd.read_csv(folder2+'dados_46d.txt', header = None, sep = '|')
dados4.columns = dados_names

dados5 = pd.read_csv(folder2+'dados_46e.txt', header = None, sep = '|')
dados5.columns = dados_names

dados6 = pd.read_csv(folder2+'dados_46f.txt', header = None, sep = '|')
dados6.columns = dados_names

dados7 = pd.read_csv(folder2+'dados_46g.txt', header = None, sep = '|')
dados7.columns = dados_names

dados8 = pd.read_csv(folder2+'dados_46h.txt', header = None, sep = '|')
dados8.columns = dados_names


folder4 = folder +'dinamica10_Sandro/res58/res58af/'

dados1b = pd.read_csv(folder4+'dados_58a.txt', header = None, sep = '|')
dados1b.columns = dados_names

dados2b = pd.read_csv(folder4+'dados_58b.txt', header = None, sep = '|')
dados2b.columns = dados_names

dados3b = pd.read_csv(folder4+'dados_58c.txt', header = None, sep = '|')
dados3b.columns = dados_names

dados4b = pd.read_csv(folder4+'dados_58d.txt', header = None, sep = '|')
dados4b.columns = dados_names

dados5b = pd.read_csv(folder4+'dados_58e.txt', header = None, sep = '|')
dados5b.columns = dados_names

dados6b = pd.read_csv(folder4+'dados_58f.txt', header = None, sep = '|')
dados6b.columns = dados_names

folder3 = folder +'dinamica10_Sandro/res58/res58mn/'

dados7b = pd.read_csv(folder3+'dados_58m.txt', header = None, sep = '|')
dados7b.columns = dados_names

dados8b = pd.read_csv(folder3+'dados_58n.txt', header = None, sep = '|')
dados8b.columns = dados_names




#semilogx

plt.loglog(dados6b.v0,dados6b.custo,'^b', ms = 4, label = r'$\delta = 5.0$')
plt.loglog(dados1b.v0,dados1b.custo,'1y', ms = 4, label = r'$\delta = 2.5$')
plt.loglog(dados8b.v0,dados8b.custo,'vm', ms = 4, label = r'$\delta = 2.2$')
plt.loglog(dados7b.v0,dados7b.custo,'p', color = 'orange', ms = 4, label = r'$\delta = 2.1$')
plt.loglog(dados8.v0,dados8.custo,'Dk', ms = 4, label = r'$\delta = 2.00$')
#plt.loglog(dados7.v0,dados7.custo,'-1c', ms = 6, label = r'$\delta = 1.90$')
#plt.semilogx(dados4.v0,dados4.custo,'-sy', ms = 4, label = r'$\delta = 1.70$')
plt.loglog(dados6.v0,dados6.custo,'sc', ms = 4, label = r'$\delta = 1.80$')
#plt.loglog(dados5.v0,dados5.custo,'-og', ms = 4, label = r'$\delta = 1.75$')
#plt.loglog(dados3.v0,dados3.custo,'-p', color = 'orange', ms = 4, label = r'$\delta = 1.65$')
plt.semilogx(dados2.v0,dados2.custo,'og', ms = 4, label = r'$\delta = 1.60$')
plt.loglog(dados1.v0,dados1.custo,'dr', ms = 4, label = r'$\delta = 1.50$')
plt.legend(loc='upper right',fontsize = 10)
plt.xlabel(r'Velocity $v_0$',fontsize = 16)
plt.ylabel(r'Computational cost $C$',fontsize = 16)
plt.title(r'Caso \textit{quenched}: relevo $K = 4$, $M = 53$.',fontsize=14)
plt.grid(True)
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
#axes.set_xlim([0.05,130])
#axes.set_ylim([0.7,1.0])
plt.text(25,2.2,r'$M=53$',fontsize = 14)#, color = 'b', backgroundcolor = 'w')
plt.savefig('figura_6.pdf',dpi = 300, bbox_inches='tight') 
plt.close()
