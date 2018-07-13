import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#WRITE(16,*) i5,'|',Nvreal(i9),'|',custo(i9)!,'|',numvizfin(i9)
dados_names = ['amostra','Nv','custo']

folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/resultados/"

folder2 = folder +'dinamica10_Paulo/res68qx/'

dados_a = pd.read_csv(folder2+'dados_68q.txt', header = None, sep = '|')
dados_a.columns = dados_names
Na = dados_a.amostra[0]

dados_b = pd.read_csv(folder2+'dados_68r.txt', header = None, sep = '|')
dados_b.columns = dados_names
Nb = dados_b.amostra[0]

dados_c = pd.read_csv(folder2+'dados_68s.txt', header = None, sep = '|')
dados_c.columns = dados_names
Nc = dados_c.amostra[0]

dados_d = pd.read_csv(folder2+'dados_68t.txt', header = None, sep = '|')
dados_d.columns = dados_names
Nd = dados_d.amostra[0]

dados_e = pd.read_csv(folder2+'dados_68u.txt', header = None, sep = '|')
dados_e.columns = dados_names
Ne = dados_e.amostra[0]

dados_f = pd.read_csv(folder2+'dados_68v.txt', header = None, sep = '|')
dados_f.columns = dados_names
Nf = dados_f.amostra[0]

dados_g = pd.read_csv(folder2+'dados_68w.txt', header = None, sep = '|')
dados_g.columns = dados_names
Ng = dados_g.amostra[0]

dados_h = pd.read_csv(folder2+'dados_68x.txt', header = None, sep = '|')
dados_h.columns = dados_names
Nh = dados_h.amostra[0]


vetorNv = pd.read_csv(folder2+'vetorNv14.txt', header = None, sep = '|')
N = 12
sizeL = np.array(vetorNv)
Nl = len(sizeL)
ct = np.zeros(Nl, dtype = float)
ct2 = np.zeros(Nl, dtype = float)
lambdaN = 0.99978
for i3 in range(Nl):
	ct2[i3] = sizeL[i3]/(2**N)
    
folder3 = folder +'dinamica18_static/res70b/'
dados_70c = pd.read_csv(folder3+'dados_70c.txt', header = None, sep = '|')
dados_70c.columns = dados_names
N70c = dados_70c.amostra[0]

dados_70c2 = pd.read_csv(folder3+'dados_70c2.txt', header = None, sep = '|')
dados_70c2.columns = dados_names
N70c2 = dados_70c2.amostra[0]

dados70 = (N70c*dados_70c.custo+N70c2*dados_70c2.custo)/(N70c+N70c2)

colunas_sandro = ['Nv','custo','nviz','amostras']
folder4 = folder +'dinamica11_random/res71ag/'
dados71c = pd.read_csv(folder4+'dados_71c.txt', header = None, sep = '|')
dados71c.columns = colunas_sandro

plt.loglog(dados_a.Nv,dados_a.custo/Na,'sb', ms = 4, label = r'$v_0 = 0.0 $')
plt.loglog(dados_b.Nv,dados_b.custo/Nb,'py', ms = 4, label = r'$v_0 = 0.25 $')
plt.loglog(dados_c.Nv,dados_c.custo/Nc,'^g', ms = 4, label = r'$v_0 = 0.5 $')
#plt.loglog(dados_d.Nv,dados_d.custo/Nd,'vc', ms = 4, label = r'$v_0 = 0.75 $')
#plt.loglog(dados_e.Nv,dados_e.custo/Ne,'pm', ms = 4, label = r'$v_0 = 1.0 $')
plt.loglog(dados_f.Nv,dados_f.custo/Nf,'vc', ms = 4, label = r'$v_0 = 1.5 $')
#plt.loglog(dados_g.Nv,dados_g.custo/Ng,'-1c', ms = 4, label = r'$v_0 = 5.0 $')
plt.loglog(dados_h.Nv,dados_h.custo/Nh,'or', ms = 4, label = r'$v_0 = 100 $')
#plt.loglog(dados_70c.Nv,dados_70c.custo,'-k', label = r'static')
plt.loglog(dados_70c.Nv,dados70,'-k', label = r'static')
plt.loglog(dados71c.Nv,dados71c.custo,'Dk', ms = 4, label = r'RN',
 markeredgewidth=1, markeredgecolor='k', markerfacecolor = 'None',)
plt.loglog(sizeL,ct2,'--k', lw = 2, label = r'$L/2^N$')
plt.axvline(x=12.5,color='darkred', linestyle='--')
plt.legend(loc='upper left',fontsize = 10)
plt.xlabel(r'Number of agents $M$',fontsize = 16)
plt.ylabel(r'Computational cost $C$',fontsize = 16)
plt.title(r'Quenched: $K = 8$, $p=0.5$, $\delta = 2.0$.',fontsize=14)
plt.grid(True)
plt.xticks(size=14)
plt.yticks(size=14)
axes = plt.gca()
axes.set_xlim([2,2e3])
axes.set_ylim([1,1.3])
#plt.text(130,1.6,r'$\delta = 2.0$',fontsize = 14)#, color = 'b', backgroundcolor = 'w')
plt.savefig('figura_18c.pdf',dpi = 300, bbox_inches='tight') 
plt.close()
