import math, cmath, time
import numpy as np
import matplotlib.pyplot as plt
#from scipy import spatial
#from matplotlib.markers import *

#Inicio da marcacao do tempo de calculo
start_time = time.clock()
	 



####################################################################


#Nv, Q, L, v, p_walk, d_int, c_rec, samples, rho, grid
file1 = open('parametros_Q110_N16384_S100_v1_del1p4_G22.txt',"r")
for linha in file1:
	a1, b1, c1, d1, e1, f1, g1, h1, j11, l11 = linha.split()
file1.close()

Nv, Q, L, v = int(a1), int(b1), round(float(c1)), float(d1)
p_walk, d_int = float(e1), float(f1)
c_rec, samples, rho  = float(g1), int(h1), float(j11)
grid = l11


#lista = ['0p2', '0p4', '0p6', '0p8', '1', '1p2', '1p3', '1p4', '1p5', '1p6', '1p7', '1p9']
#valores = np.array([0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.9])
lista = ['0p1', '0p2', '0p3', '0p4', '0p5', '0p6', '0p7', '0p8', '0p9']
lista += ['1', '1p1', '1p2', '1p3', '1p4', '1p5', '1p6', '1p7', '1p8', '1p9', '2p0']
listavalores = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1] 
listavalores += [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
valores = np.array(listavalores)
nv = len(lista)
Gamma = 22

coeficiente, slope = np.empty((nv,Gamma+1)), np.empty((nv,Gamma+1))
taxa_rec = np.empty(Gamma+1)

#c_rec, alpha, slope, intercept
	
for i1 in range(nv):
	file = open('coeficiente_Q110_N16384_S100_v1_del'+lista[i1]+'_G22.txt','r')
	t4 = 0
	for linhas in file:
		a3, b3, c3, d3 = linhas.split()
		taxa_rec[t4] = float(a3)
		coeficiente[i1,t4] = float(b3)
		slope[i1,t4] = float(c3)
		t4 += 1
	file.close()

coemin = 0.0

vecx, vecy, vecz = [], [], []
for t5 in range(Gamma+1):
	for i5 in range(nv):
		if coeficiente[i5,t5] > coemin:
			vecx.append(taxa_rec[t5])
			vecy.append(valores[i5]) 
			vecz.append(coeficiente[i5,t5])


#***********************************
#importando os arquivos da regiao 1: 0.12 < c < 0.16
regiao1 = ['0p1', '0p2', '0p3', '0p4', '0p5', '0p6', '0p7']
regiao1 += ['0p8', '0p9', '1p0', '1p1', '1p2', '1p3', '1p4']
regiao1 += ['1p5', '1p6', '1p7', '1p8', '1p9', '2p0']
nv1 = len(regiao1)
Ncrec_r1 = 8


coef_r1, slope_r1 = np.empty((nv1,Ncrec_r1)), np.empty((nv1,Ncrec_r1))
taxa_rec_r1 = np.empty(Ncrec_r1)

for i2 in range(nv1):
	file = open('coeficiente_N16384_r1_del'+regiao1[i2]+'.txt','r')
	t4 = 0
	for linhas in file:
		a3, b3, c3, d3 = linhas.split()
		taxa_rec_r1[t4] = float(a3)
		coef_r1[i2,t4] = float(b3)
		slope_r1[i2,t4] = float(c3)
		t4 += 1
	file.close()


for t5 in range(Ncrec_r1):
	for i5 in range(nv1):
		if coef_r1[i5,t5] > coemin:
			vecx.append(taxa_rec_r1[t5])
			vecy.append(valores[i5]) 
			vecz.append(coef_r1[i5,t5])

# comin = np.amin(coeficiente)
# comax = np.amax(coeficiente)

clmap = plt.cm.get_cmap('jet') #rainbow, plasma, Reds,Pubu, Purbles, 

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
sc = plt.scatter(vecx, vecy, c = vecz, s = 305, marker = 's', linewidth = 0.0, vmin = coemin, vmax = 1.0, cmap = clmap)
clb = plt.colorbar(sc)
clb.set_label(r'$\alpha(c,\delta)$', fontsize = 18, labelpad=-30, y=1.09, rotation=0)
plt.xlabel(r'Recovery rate $c$', fontsize = 16) #k indica cor preta
plt.ylabel(r'Distance $\delta/a$', fontsize = 16)
# titulo2 = r'$N=$ '+str(Nsqrt)+'$^2$,  $\eta = $ '+str(eta)+',  $t = $ '+str(evolucoes)+r',  $\vert \Psi \vert =$ '+str(Psi_medio)
# plt.title(titulo2)
axes = plt.gca()
axes.set_ylim([0.05,2.05])
axes.set_xlim([-0.002,0.165])
plt.savefig('figura5_scatter_jet2.png', dpi = 300, bbox_inches='tight')
#plt.savefig('figura5_scatter_jet.pdf', dpi = 300, bbox_inches='tight')
plt.close()

