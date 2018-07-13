import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#subprocess.call(['rm','-rf','res68ah'])
#subprocess.call(['scp','-r','-P12','pgomes@emt5.ifsc.usp.br:/home/pgomes/dados/res68ah/','.'])

#WRITE(16,*) i5,'|',Nvreal(i9),'|',custo(i9)!,'|',numvizfin(i9)
dados_names = ['amostra','Nv','custo']

folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/"

folder2 = folder +'dinamica10_Paulo/res68ah/'

dados_a = pd.read_csv(folder2+'dados_68a.txt', header = None, sep = '|')
dados_a.columns = dados_names
Na = dados_a.amostra[0]

dados_b = pd.read_csv(folder2+'dados_68b.txt', header = None, sep = '|')
dados_b.columns = dados_names
Nb = dados_b.amostra[0]

dados_c = pd.read_csv(folder2+'dados_68c.txt', header = None, sep = '|')
dados_c.columns = dados_names
Nc = dados_c.amostra[0]

dados_d = pd.read_csv(folder2+'dados_68d.txt', header = None, sep = '|')
dados_d.columns = dados_names
Nd = dados_d.amostra[0]

dados_e = pd.read_csv(folder2+'dados_68e.txt', header = None, sep = '|')
dados_e.columns = dados_names
Ne = dados_e.amostra[0]

dados_f = pd.read_csv(folder2+'dados_68f.txt', header = None, sep = '|')
dados_f.columns = dados_names
Nf = dados_f.amostra[0]

dados_g = pd.read_csv(folder2+'dados_68g.txt', header = None, sep = '|')
dados_g.columns = dados_names
Ng = dados_g.amostra[0]

dados_h = pd.read_csv(folder2+'dados_68h.txt', header = None, sep = '|')
dados_h.columns = dados_names
Nh = dados_h.amostra[0]


folder3 = folder +'dinamica18_static/res70b/'
dados_70b = pd.read_csv(folder3+'dados_70b.txt', header = None, sep = '|')
dados_70b.columns = dados_names


#importando o caso annealed
#subprocess.call(['cd','..'])
#subprocess.call(['cd','dinamica11_random'])
#subprocess.call(['rm','-rf','res71ag'])
#subprocess.call(['scp','-r','-P12','pgomes@emt1.ifsc.usp.br:/home/pgomes/dados/res71ag/','.'])

colunas_sandro = ['Nv','custo','nviz','amostras']
folder4 = folder +'dinamica11_random/res71ag/'
dados71b = pd.read_csv(folder4+'dados_71b.txt', header = None, sep = '|')
dados71b.columns = colunas_sandro

plt.loglog(dados_a.Nv,dados_a.custo/Na,'sb', ms = 4, label = r'$v_0 = 0.0 $')
#plt.loglog(dados_b.Nv,dados_b.custo/Nb,'^g', ms = 4, label = r'$v_0 = 0.25 $')
plt.loglog(dados_c.Nv,dados_c.custo/Nc,'^g', ms = 4, label = r'$v_0 = 0.5 $')
#plt.loglog(dados_d.Nv,dados_d.custo/Nd,'vc', ms = 4, label = r'$v_0 = 0.75 $')
#plt.loglog(dados_e.Nv,dados_e.custo/Ne,'pm', ms = 4, label = r'$v_0 = 1.0 $')
#plt.loglog(dados_f.Nv,dados_f.custo/Nf,'vc', ms = 4, label = r'$v_0 = 1.5 $')
#plt.loglog(dados_g.Nv,dados_g.custo/Ng,'-1c', ms = 4, label = r'$v_0 = 5.0 $')
plt.loglog(dados_h.Nv,dados_h.custo/Nh,'or', ms = 4, label = r'$v_0 = 100 $')
plt.loglog(dados_70b.Nv,dados_70b.custo,'-k', ms = 4, label = r'static')
plt.loglog(dados71b.Nv,dados71b.custo,'Dk', ms = 4, label = r'RN',
 markeredgewidth=1, markeredgecolor='k', markerfacecolor = 'None',)
plt.axvline(x=12.5,color='darkred', linestyle='--')
plt.legend(loc='lower right',fontsize = 10)
plt.xlabel(r'Number of agents $M$',fontsize = 16)
plt.ylabel(r'Computational cost $C$',fontsize = 16)
plt.title(r'Quenched: $K = 6$, $p=0.5$, $\delta = 2.0$.',fontsize=14)
plt.grid(True)
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
axes.set_xlim([2,2e3])
axes.set_ylim([4e-1,1])
#plt.text(130,1.6,r'$\delta = 2.0$',fontsize = 14)#, color = 'b', backgroundcolor = 'w')
plt.savefig('figura_18b.pdf',dpi = 300, bbox_inches='tight') 
plt.close()
