import random, math
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


def get_cmap(n, name='gnuplot'):
	'''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
	RGB color; the keyword argument name must be a standard mpl colormap name.'''
	return plt.cm.get_cmap(name, n)
	

def gera_posicoes():
	cmap = get_cmap(Nv)
	for t2 in range(Q):
		for i2 in range(Nv):
			#plt.plot(posX[i2][0:t2+1],posY[i2][0:t2+1], lw = 2, color = cmap(i2))
			plt.scatter(posX[t2][i2], posY[t2][i2], s=150, marker= 'o', color = cmap(i2)) 
		title1 = r'2D random walk. $N=$'+str(Nv)+', $t=$'+str(t2)+', $v=$'+str(v)+', $p=$'+str(p_walk)+', $d=$'+str(d)+'.'
		plt.title(title1)
		plt.xlabel("x",fontsize = 14)
		plt.ylabel("y",fontsize = 14)
		plt.grid(True)
		axes = plt.gca()
		axes.set_xlim([0,L])
		axes.set_ylim([0,L])
		plt.savefig("imagens/posicoes_"+str(t2)+".png",dpi = 300) 
		plt.close() 


def gera_grafo(Q,Nv,arestas,arquivo,L):
	estado = np.loadtxt(arquivo)
	grafo = []
	nos = [i for i in range(Nv)]
	pos_nos = []
	l_cores = [[] for t in range(Q)]
	infected, susceptible, recovered = [], [], []
	for t3 in range(Q):
		grafo.append(nx.Graph())
		grafo[t3].add_nodes_from(nos)
		grafo[t3].add_edges_from(arestas[t3])
		dicionario = {}
		for i3 in range(Nv):
			dicionario[nos[i3]] = [posX[t3][i3],posY[t3][i3]]
		pos_nos.append(dicionario)
		n_sus, n_inf, n_rec = 0, 0, 0
		for i3 in range(Nv):
			if estado[t3][i3] == 0:
				cor = 'g' #susceptible
				n_sus += 1
			if estado[t3][i3] == 1:
				cor = 'r' #infected
				n_inf += 1
			if estado[t3][i3] == 2:
				cor = 'b' #recovered
				n_rec +=1
			l_cores[t3].append(cor)
		susceptible.append(n_sus)
		infected.append(n_inf)
		recovered.append(n_rec)
	for t5 in range(Q):
		nx.draw_networkx_nodes(grafo[t5], with_labels=True, pos = pos_nos[t5], node_size = 35, node_color = l_cores[t5], linewidth = 1.0)
		nx.draw_networkx_edges(grafo[t5], with_labels=True, pos = pos_nos[t5], width = 1.0, edge_color = 'gray')
		title2 = r'$N=$ '+str(Nv)+r', $v=$ '+str(v)+r', $t=$ '+str(t5)+'.'
		#title2 += ', $N_s=$'+str(susceptible[t5])+', $N_i=$'+str(infected[t5])+', $N_r=$'+str(recovered[t5])
		plt.title(title2, fontsize = 16)
		plt.xlabel(r"$x$",fontsize = 16)
		plt.ylabel(r"$y$",fontsize = 16)
		#plt.grid(True)
		axes = plt.gca()
		axes.set_xlim([0,L])
		axes.set_ylim([0,L])
		# plt.text(0.92*L,0.9*L,'sus',fontsize = 10, color = 'g', backgroundcolor = 'w')
		# plt.text(0.92*L,0.8*L,'inf',fontsize = 1, color = 'r', backgroundcolor = 'w')
		# plt.text(0.92*L,0.7*L,'rec',fontsize = 1, color = 'b', backgroundcolor = 'w')
		plt.savefig("imagens/rede_"+str(t5)+".pdf",dpi = 300, bbox_inches='tight') 
		plt.close() 





###############################################################

#Nv, Q, L, v, p_walk, d_int, p_in, samples 
file1 = open('parametros.csv',"r")
for linha in file1:
	a1, b1, c1, d1, e1, f1, g1, h1= linha.split()
file1.close()

Nv, Q, L, v = int(a1), int(b1), round(float(c1)), float(d1)
p_walk, d_int = float(e1), float(f1)
p_in, samples  = float(g1), float(h1)
#L = tamanho da caixa, modulo da distancia deslocada, p_walk = probabilidade de andar quando interagindo
#d = distancia de corte para definir a interacao entre dois individuos

posX = np.loadtxt("posicao_x.csv")
posY = np.loadtxt("posicao_y.csv")
# #posX = matriz com len(posX) linhas e len(posX[0]) colunas 
#Q, Nv = len(posX), len(posX[0]) # = numero de linhas, numero de colunas
#posX[0] = primeira linha da matriz, que corresponde aos valores de todos os individuos na primeira iteracao
#print(posX[0][0])
#print(posX[Q-1][Nv-1])
#gera_posicoes() #cria o grafico com os individuos

file2 = open('interacoes.csv','r')
conj_linhas = file2.readlines()
#cada linha e um elemento da lista do tipo string
vizinhos = []
for linhas in conj_linhas:
	vizinhos.append([int(i) for i in linhas.split()])
file2.close()

#vizinhos = lista com varias linhas
#coluna 1 = tempo, coluna 2 = individuo, coluna 3 = numero de vizinhos, colunas 4, 5... identificacao dos individuos
#se coluna 3 = 0, coluna 4 = 0 e nao ha colunas 5, 6, ....

arestas = [[] for i2 in range(Q)]
for lista in vizinhos:
	Nviz = lista[2]
	viz_ind = 3
	if Nviz > 0:
		ind_t = lista[0]-1
		while viz_ind <= Nviz+2:
			arestas[ind_t].append((lista[1],lista[viz_ind]))
			viz_ind += 1


#Construcao dos grafos
gera_grafo(Q,Nv,arestas,'estado.csv',L)

