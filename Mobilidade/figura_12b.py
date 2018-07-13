import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#Nagentes(i), "|", dados(i, 1) / real(s), "|", dados(i, 2) / real(s), "|", s 
dados_names = ['v0','custo','nviz','amostras']

folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/"

folder2 = folder +'dinamica12_eixoX/res49ah/'

dados1 = pd.read_csv(folder2+'dados_49e.txt', header = None, sep = '|')
dados1.columns = dados_names

dados2 = pd.read_csv(folder2+'dados_49f.txt', header = None, sep = '|')
dados2.columns = dados_names

dados3 = pd.read_csv(folder2+'dados_49g.txt', header = None, sep = '|')
dados3.columns = dados_names

dados4 = pd.read_csv(folder2+'dados_49h.txt', header = None, sep = '|')
dados4.columns = dados_names

vp = math.sqrt(53)

plt.plot(dados1.v0,dados1.custo,'-sr', ms = 4, label = r'$\delta = 1.4$')
#plt.plot(dados2.v0,dados2.custo,'-or', ms = 4, label = r'$\delta = 1.6$')
#plt.plot(dados3.v0,dados3.custo,'-pk', ms = 4, label = r'$\delta = 1.8$')
plt.plot(dados4.v0,dados4.custo,'-ob', ms = 4, label = r'$\delta = 2.0$')
plt.legend(loc='upper right',fontsize = 12)
plt.xlabel(r'Velocity $v_0$',fontsize = 16)
plt.ylabel(r'Computational cost $C$',fontsize = 16)
#plt.title(r'$\textbf{v} = v\textbf{x}$, $p = 0.5$, $M = 53$, $v_p= $ '+str(round(vp,2))+'.',fontsize=16)
plt.grid(True)
for i2 in [1,2,3,4,5]:
    plt.axvline(x=i2*vp,color='k', linestyle='--')
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
#axes.set_xlim([-2.0,80])
#axes.set_ylim([0.0,60])
#plt.text(140,1.3,r'$v=v_0 R \Phi_g$',fontsize = 15, color = 'b', backgroundcolor = 'w')
plt.savefig('figura_12b.pdf',dpi = 300, bbox_inches='tight') 
plt.close()
