import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#Nv, Q, L, v, p_walk, d_int, c_rec, samples, rho, grid
file1 = open('parametros.txt',"r")
for linha in file1:
	a1, b1, c1, d1, e1, f1, g1, h1, j11, l11 = linha.split()
file1.close()

Nv, Q, L, v = int(a1), int(b1), round(float(c1)), float(d1)
p_walk, d_int = float(e1), float(f1)
c_rec, samples, rho  = float(g1), float(h1), float(j11)
grid = l11

lista = ['0', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '20']

nl = len(lista)
#Grafico das contagens
tempo = np.empty(Q)
cont_inf = np.empty((nl,Q))
for i1 in range(nl):
	file = open('contagens_N16384_v1_S100_d2_c'+str(lista[i1])+'.csv','r')
	t4 = 0
	for linhas in file:
		a3, b3, c3, d3 = linhas.split()
		tempo[t4] = int(a3)
		cont_inf[i1][t4] = float(c3)
		t4 += 1
	file.close()
	#plt.loglog(tempo,cont_inf[i1], lw = 2, label = r'$v=$ '+str(lista2[i1]))

nValues = np.array([0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12])
nval = len(nValues)

if nl == nval: print('Valores corretos.')

# setup the normalization and the colormap
normalize = mcolors.Normalize(vmin=nValues.min(), vmax=nValues.max())
colormap = cm.viridis

#for n in nValues:
for n in range(nval):
	#plt.loglog(tempo,cont_inf[n], lw = 2, color=colormap(normalize(nValues[n])))
	if nValues[n] == 0.06:
		plt.loglog(tempo,cont_inf[n], '--', lw = 2, color=colormap(normalize(nValues[n])), label = r'$c=0.06$')
	else:
		plt.loglog(tempo,cont_inf[n], '-', lw = 2, color=colormap(normalize(nValues[n])))

# setup the colorbar
scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(nValues)
#plt.colorbar(scalarmappaple)
clb = plt.colorbar(scalarmappaple)
clb.set_label(r'rate $c$', fontsize = 16, labelpad=-50, y=1.07, rotation=0)
#titulo = r'$N=$ '+str(Nv)+r', $v=$ '+str(v)+r', $S=$ '+str(samples)+r', $d=$ '+str(round(d_int,2))+'.'
#plt.title(titulo,fontsize = 16)
plt.legend(loc='upper left',fontsize = 16)
plt.xlabel(r'Time $t$ (iterations)',fontsize = 16)
plt.ylabel(r'Infected individuals $i(t)$',fontsize = 16)
plt.grid(True)
plt.axvline(x = 7.0, lw = 2, color = 'r')
plt.axvline(x = 110, lw = 2, color = 'r')
axes = plt.gca()
axes.set_xlim([1,Q])
#axes.set_ylim([1e-6,0.03])
plt.text(12,0.2,r'$v=1.0$, $\delta=a$',fontsize = 16)#, color = '#840000')#, backgroundcolor = 'w')
plt.savefig('figura4_v1p0_c.pdf',dpi = 300, bbox_inches='tight')
plt.savefig('figura4_v1p0_c.png',dpi = 300, bbox_inches='tight') 