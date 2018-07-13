import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#subprocess.call(['rm','-rf','res72ah'])
#subprocess.call(['scp','-r','-P12','pgomes@emt6.ifsc.usp.br:/home/pgomes/dados/res72ah/','.'])

dados_names = ['amostra','Nv','custo']
folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/"
folder2 = folder +'dinamica10_Paulo/res72ah/'

dados_a = pd.read_csv(folder2+'dados_72a.txt', header = None, sep = '|')
dados_a.columns = dados_names
Na = dados_a.amostra[0]

dados_b = pd.read_csv(folder2+'dados_72b.txt', header = None, sep = '|')
dados_b.columns = dados_names
Nb = dados_b.amostra[0]

dados_c = pd.read_csv(folder2+'dados_72c.txt', header = None, sep = '|')
dados_c.columns = dados_names
Nc = dados_c.amostra[0]

dados_d = pd.read_csv(folder2+'dados_72d.txt', header = None, sep = '|')
dados_d.columns = dados_names
Nd = dados_d.amostra[0]

dados_e = pd.read_csv(folder2+'dados_72e.txt', header = None, sep = '|')
dados_e.columns = dados_names
Ne = dados_e.amostra[0]

dados_f = pd.read_csv(folder2+'dados_72f.txt', header = None, sep = '|')
dados_f.columns = dados_names

dados_g = pd.read_csv(folder2+'dados_72g.txt', header = None, sep = '|')
dados_g.columns = dados_names

dados_h = pd.read_csv(folder2+'dados_72h.txt', header = None, sep = '|')
dados_h.columns = dados_names



#importando o caso annealed

colunas_sandro = ['Nv','custo','nviz','amostras']
folder4 = folder +'dinamica11_random/res71ag/'
dados71d = pd.read_csv(folder4+'dados_71d.txt', header = None, sep = '|')
dados71d.columns = colunas_sandro

#caso estatico
folder3 = folder +'dinamica18_static/res70b/'
dados_70d = pd.read_csv(folder3+'dados_70d.txt', header = None, sep = '|')
dados_70d.columns = dados_names
N70d = dados_70d.amostra[0]

dados_70d2 = pd.read_csv(folder3+'dados_70d2.txt', header = None, sep = '|')
dados_70d2.columns = dados_names
N70d2 = dados_70d2.amostra[0]

dados_70d3 = pd.read_csv(folder3+'dados_70d3.txt', header = None, sep = '|')
dados_70d3.columns = dados_names
N70d3 = dados_70d3.amostra[0]

dados_70d4 = pd.read_csv(folder3+'dados_70d4.txt', header = None, sep = '|')
dados_70d4.columns = dados_names
N70d4 = dados_70d4.amostra[0]

dados_70d5 = pd.read_csv(folder3+'dados_70d5.txt', header = None, sep = '|')
dados_70d5.columns = dados_names
N70d5 = dados_70d5.amostra[0]

dados_70d6 = pd.read_csv(folder3+'dados_70d6.txt', header = None, sep = '|')
dados_70d6.columns = dados_names
N70d6 = dados_70d6.amostra[0]

dados70 = N70d*dados_70d.custo + N70d2*dados_70d2.custo + N70d3*dados_70d3.custo
dados70 += N70d4*dados_70d4.custo + N70d5*dados_70d5.custo + N70d6*dados_70d6.custo

dados70 = dados70/(N70d+N70d2+N70d3+N70d4+N70d5+N70d6)


plt.loglog(dados_a.Nv,dados_a.custo,'sb', ms = 4, label = r'$v_0 = 0.0 $')
#plt.loglog(dados_b.Nv,dados_b.custo,'^g', ms = 4, label = r'$v_0 = 0.25 $')
plt.loglog(dados_c.Nv,dados_c.custo,'vg', ms = 4, label = r'$v_0 = 0.5 $')
#plt.loglog(dados_d.Nv,dados_d.custo,'vc', ms = 4, label = r'$v_0 = 1.0 $')
#plt.loglog(dados_e.Nv,dados_e.custo,'py', ms = 4, label = r'$v_0 = 1.5 $')
plt.loglog(dados_f.Nv,dados_f.custo,'or', ms = 4, label = r'$v_0 = 100 $')
#plt.loglog(dados_g.Nv,dados_g.custo,'-r', ms = 4, label = r'$\delta = 1.0 $')
#plt.loglog(dados_h.Nv,dados_h.custo,'-b', ms = 4, label = r'$\delta = 1.5 $')
plt.loglog(dados71d.Nv,dados71d.custo,'Dk', ms = 4, label = r'RN',
 markeredgewidth=1, markeredgecolor='k', markerfacecolor = 'None',)
plt.loglog(dados_70d.Nv,dados70,'-k', label = r'static')
plt.axvline(x=12.5,color='darkred', linestyle='--')
plt.legend(loc='upper right',fontsize = 10)
plt.xlabel(r'Number of agents $M$',fontsize = 16)
plt.ylabel(r'Computational cost $C$',fontsize = 16)
plt.title(r'Quenched: $K = 10$, $\delta = 2.0$, $p=0.5$.',fontsize=14)
plt.grid(True)
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
axes.set_xlim([2,3e3])
axes.set_ylim([0.95,1.2])
#plt.text(130,1.6,r'$\delta = 2.0$',fontsize = 14)#, color = 'b', backgroundcolor = 'w')
plt.savefig('figura_18d.pdf',dpi = 300, bbox_inches='tight') 
plt.close()
