import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#Nv, Q, L, v, p_walk, d_int, c_rec, samples, rho, grid
file1 = open('parametros_N16384_v1_c0p06_S100_d3.txt',"r")
for linha in file1:
	a1, b1, c1, d1, e1, f1, g1, h1, j11, l11 = linha.split()
file1.close()

Nv, Q, L, v = int(a1), int(b1), round(float(c1)), float(d1)
p_walk, d_int = float(e1), float(f1)
c_rec, samples, rho  = float(g1), float(h1), float(j11)
grid = l11

lista = ['0p5', '0p75', '1', '1p25', '1p5', '1p75', '2', '2p25', '2p5', '2p75', '3']
#lista = ['1', '2', '3']
nlis = len(lista)
#nValues = np.array([0.25, 0.50, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 4, 5, 6, 7])
nValues = np.array([0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.50, 2.75, 3])/2
nval = len(nValues)

#escala = np.linspace(0,1,nlis)

#Grafico das contagens
tempo = np.empty(Q)
cont_inf = np.empty((nval,Q))
for i1 in range(nval):
	file = open('contagens_N16384_v1_c0p06_S100_d'+lista[i1]+'.csv','r')
	t4 = 0
	for linhas in file:
		a3, b3, c3, d3 = linhas.split()
		tempo[t4] = int(a3)
		cont_inf[i1][t4] = float(c3)
		t4 += 1
	file.close()

# setup the normalization and the colormap
normalize = mcolors.Normalize(vmin=nValues.min(), vmax=nValues.max())
#normalize = mcolors.Normalize(vmin=escala.min(), vmax=escala.max())
comap = cm.viridis #seismic# jet

#for n in nValues:
for n in range(nval):
	#plt.loglog(tempo,cont_inf[n], lw = 2, color=comap(normalize(nValues[n])))
	if nValues[n] == 1.0:
		plt.loglog(tempo,cont_inf[n], '--', lw = 2, color=comap(normalize(nValues[n])), label = r'$\delta=a$')
	else:
		plt.loglog(tempo,cont_inf[n], '-', lw = 2, color=comap(normalize(nValues[n])))

# setup the colorbar
scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=comap)
scalarmappaple.set_array(nValues)
#plt.colorbar(scalarmappaple)
clb = plt.colorbar(scalarmappaple)
clb.set_label(r'Distance $\delta/a$', fontsize = 16, labelpad=-50, y=1.07, rotation=0)
#titulo = r'$N=$ '+str(Nv)+r', $v=$ '+str(v)+r', $S=$ '+str(samples)+r', $c=$ '+str(round(c_rec,2))+'.'
#plt.title(titulo,fontsize = 16)
plt.legend(loc='upper left',fontsize = 16)
plt.xlabel(r'Time $t$ (iterations)',fontsize = 16)
plt.ylabel(r'Infected individuals $i(t)$',fontsize = 16)
plt.grid(True)
plt.axvline(x=7.0, lw = 2, color = 'r')
plt.axvline(x=110, lw = 2, color = 'r')
axes = plt.gca()
axes.set_xlim([1,Q])
axes.set_ylim([1e-7,1])
plt.text(11,0.3,r'$c = 0.06$, $v=1.5$.',fontsize = 16)#, color = '#840000')#, backgroundcolor = 'w')
#plt.savefig('figura4_N16384_v1p0_d.pdf',dpi = 300, bbox_inches='tight')
plt.savefig('figura4_N16384_v1p0_d.png',dpi = 300, bbox_inches='tight') 
