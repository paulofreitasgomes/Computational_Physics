import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def get_cmap(n, name='gnuplot'):
	'''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
	RGB color; the keyword argument name must be a standard mpl colormap name.'''
	return plt.cm.get_cmap(name, n)

###############################################################


#Nv, Q, L, v, p_walk, d_int, c_rec, samples, rho, grid
file1 = open('parametros_N16384_v0p1_c0p01.txt',"r")
for linha in file1:
	a1, b1, c1, d1, e1, f1, g1, h1, j11, l11 = linha.split()
file1.close()

Nv, Q, L, v = int(a1), int(b1), round(float(c1)), float(d1)
p_walk, d_int = float(e1), float(f1)
c_rec, samples, rho  = float(g1), float(h1), float(j11)
grid = l11


lista = ['0', '01', '03', '05', '07', '09', '11', '13', '14', '15', '16', '17', '18', '19', '20', '21']
nl = len(lista)
#Grafico das contagens
tempo = np.empty(Q)
cont_inf = np.empty((nl,Q))
for i1 in range(nl):
	file = open('contagens_N16384_v0p1_c0p'+str(lista[i1])+'.csv','r')
	t4 = 0
	for linhas in file:
		a3, b3, c3, d3 = linhas.split()
		tempo[t4] = int(a3)
		cont_inf[i1][t4] = float(c3)
		t4 += 1
	file.close()
	#plt.loglog(tempo,cont_inf[i1], lw = 2, label = r'$c=$ 0.'+str(lista[i1]))

# plt.title(r'$N=64^2$, $S=50$, $v=0.2$.',fontsize = 16)
# plt.legend(loc='lower left',fontsize = 16)
# plt.xlabel(r'$t$ (iterations)',fontsize = 16)
# plt.ylabel(r'$i(t)$',fontsize = 16)
# plt.grid(True)
# axes = plt.gca()
# axes.set_xlim([0,Q])
# #axes.set_ylim([0,1.1])
# #plt.text(80,92,'susceptible',fontsize = 14, color = 'g', backgroundcolor = 'w')
# plt.savefig('transicao_v0p2_v1.png',dpi = 300, bbox_inches='tight') 
# plt.close() 


#Grafico usando colormap
nValues = np.array([0.0, 0.01, 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21])
nval = len(nValues)

# setup the normalization and the colormap
normalize = mcolors.Normalize(vmin=nValues.min(), vmax=nValues.max())
colormap = cm.seismic #winter #rainbow #jet #cool, copper

#for n in nValues:
for n in range(nval):
	plt.loglog(tempo,cont_inf[n], color=colormap(normalize(nValues[n])))
	# if nValues[n] == 0.1765:
	# 	plt.loglog(tempo,cont_inf[n], '--', color=colormap(normalize(nValues[n])), lw = 3, label = r'$c=0.1765$')
	# else:
	# 	plt.loglog(tempo,cont_inf[n], '-', color=colormap(normalize(nValues[n])))

# setup the colorbar
scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(nValues)
#plt.colorbar(scalarmappaple)
clb = plt.colorbar(scalarmappaple)
clb.set_label(r'rate $c$', fontsize = 16, labelpad=-40, y=1.07, rotation=0)
#plt.title(r'$N=64^2$, $S=50$, $v=0.2$.',fontsize = 16)
#plt.legend(loc='lower left',fontsize = 14)
plt.xlabel(r'$t$ (iterations)',fontsize = 16)
plt.ylabel(r'$i(t)$',fontsize = 16)
plt.grid(True)
#plt.legend(loc='upper left',fontsize = 16)
axes = plt.gca()
axes.set_xlim([0,Q])
#axes.set_ylim([1e-6,1])
plt.text(1.5,0.4,r'$v=0.1$, $\delta = a$.',fontsize = 14, color = 'k')#, backgroundcolor = 'w')
plt.text(15,0.15,r'$c=0.0$',fontsize = 14, color = colormap(normalize(0.0)))#, backgroundcolor = 'w')
plt.text(12,3e-4,r'$c=0.21$',fontsize = 14, color = colormap(normalize(0.21)))#, backgroundcolor = 'w')
plt.savefig('transicao_v0p1_c.png',dpi = 300, bbox_inches='tight') 
plt.savefig('transicao_v0p1_c.pdf',dpi = 300, bbox_inches='tight') 