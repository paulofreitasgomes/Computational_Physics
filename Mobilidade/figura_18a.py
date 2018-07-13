import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#diretorio71 = '/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/dinamica10_Paulo/'
##subprocess.call(['cd',diretorio71])
#subprocess.call(['cd','/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/dinamica10_Paulo/'])
#subprocess.call(['rm','-rf','res71hl'])
#subprocess.call(['scp','-r','-P12','pgomes@emt1.ifsc.usp.br:/home/pgomes/dados/res71hl/','.'])
#diretorio3 = '/home/paulo/Dropbox/Profissional/usp/relatorio/figuras/Mobilidade'
#subprocess.call(['cd',diretorio3])

dados_names = ['amostra','Nv','custo']
folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/"
folder2 = folder +'dinamica10_Paulo/res71hl//'

dados_a = pd.read_csv(folder2+'dados_71h.txt', header = None, sep = '|')
dados_a.columns = dados_names
Na = dados_a.amostra[0]

dados_b = pd.read_csv(folder2+'dados_71i.txt', header = None, sep = '|')
dados_b.columns = dados_names
Nb = dados_b.amostra[0]

dados_c = pd.read_csv(folder2+'dados_71j.txt', header = None, sep = '|')
dados_c.columns = dados_names
Nc = dados_c.amostra[0]

dados_d = pd.read_csv(folder2+'dados_71k.txt', header = None, sep = '|')
dados_d.columns = dados_names
Nd = dados_d.amostra[0]

dados_e = pd.read_csv(folder2+'dados_71l.txt', header = None, sep = '|')
dados_e.columns = dados_names
Ne = dados_e.amostra[0]


#importando o caso annealed

#diretorio4 = '/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/dinamica11_random/'
#subprocess.call(['cd','diretorio4'])
#subprocess.call(['rm','-rf','res71ag'])
#subprocess.call(['scp','-r','-P12','pgomes@emt1.ifsc.usp.br:/home/pgomes/dados/res71ag/','.'])
#subprocess.call(['cd',diretorio3])

colunas_sandro = ['Nv','custo','nviz','amostras']
folder4 = folder +'dinamica11_random/res71ag/'
dados71a = pd.read_csv(folder4+'dados_71a.txt', header = None, sep = '|')
dados71a.columns = colunas_sandro

#importando o caso estatico
folder3 = folder +'dinamica18_static/res70b/'
dados_70h = pd.read_csv(folder3+'dados_70h.txt', header = None, sep = '|')
dados_70h.columns = dados_names

plt.loglog(dados_a.Nv,dados_a.custo/Na,'sb', ms = 4, label = r'$v_0 = 0.0 $')
#plt.loglog(dados_b.Nv,dados_b.custo/Nb,'^g', ms = 4, label = r'$v_0 = 0.5 $')
#plt.loglog(dados_c.Nv,dados_c.custo/Nc,'pm', ms = 4, label = r'$v_0 = 1.0 $')
#plt.loglog(dados_d.Nv,dados_d.custo/Nd,'vc', ms = 4, label = r'$v_0 = 1.5 $')
plt.loglog(dados_e.Nv,dados_e.custo/Ne,'or', ms = 4, label = r'$v_0 = 100 $')
plt.loglog(dados71a.Nv,dados71a.custo,'Dk', ms = 4, label = r'Annealed',
 markeredgewidth=1, markeredgecolor='k', markerfacecolor = 'None',)
plt.loglog(dados_70h.Nv,dados_70h.custo,'-k', ms = 4, label = r'static')
plt.axvline(x=12.5,color='darkred', linestyle='--')
plt.legend(loc='lower right',fontsize = 10)
plt.xlabel(r'Number of agents $M$',fontsize = 16)
plt.ylabel(r'Computational cost $C$',fontsize = 16)
plt.title(r'Quenched: $K = 2$, $\delta = 2.0$, $p=0.5$.',fontsize=14)
plt.grid(True)
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
axes.set_xlim([2,3e3])
axes.set_ylim([2.5e-1,1])
#plt.text(130,1.6,r'$\delta = 2.0$',fontsize = 14)#, color = 'b', backgroundcolor = 'w')
plt.savefig('figura_18a.pdf',dpi = 300, bbox_inches='tight') 
plt.close()
