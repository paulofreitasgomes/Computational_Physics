import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import math

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def cria_lista_links(arquivo,folder = ''):
    colunas2 = ['ag1','ag2']
    links = pd.read_csv(folder+arquivo, header = None, sep = '|')
    links.columns = colunas2
    Nedges = links.shape[0]
    lista_links = []
    for i1 in range(Nedges):
        lista_links.append((links.ag1[i1],links.ag2[i1]))
    return lista_links, Nedges
        
def cria_posicoes(arquivo,folder = ''):
    ##write(10, *) i,'|', X(i),'|', Y(i),'|',Mphi(XM1(i))
    colunas = ['agente','posX','posY','Phi']
    #folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/"
    #folder += "resultados/dinamica8/res41/teste_b/resultados/"
    posicoes = pd.read_csv(folder+arquivo, header = None, sep = '|')
    posicoes.columns = colunas
    Nv = posicoes.shape[0]
    return posicoes, Nv

def grafico_posicoes(posicoes,grafo,centro,raio,):
    dicionario = {}
    for i3 in range(Nv):
        dicionario[nos[i3]] = [posicoes.posX[i3],posicoes.posY[i3]]
    nx.draw_networkx_nodes(grafo, with_labels=True, pos = dicionario,
     node_size = 35, node_color = 'b', node_shape = 'o', linewidth = 1.0)
    nx.draw_networkx_edges(grafo, with_labels=True, pos = dicionario,
     width = 0.5, edge_color = 'k')
    title2 = r'$M=$ '+str(Nv)
    plt.title(title2, fontsize = 16)
    plt.xlabel(r'$x$',fontsize = 16)
    plt.ylabel(r'$y$',fontsize = 16)
    plt.grid(True)
    plt.axis('scaled')
    # plt.xticks((100, 200, 300, 400, 500), ('100', '200', '300','400','500'), size=14)
    # plt.yticks((100, 200, 300, 400, 500), ('100', '200', '300','400','500'), size=14)
    plt.xticks(size=14)
    plt.yticks(size=14)
    lado = math.sqrt(float(Nv) / 0.0512 )
    trajetoria = plt.Circle(centro, raio, edgecolor = 'r', facecolor = 'none')
    axes = plt.gca()
    axes.add_artist(trajetoria)
    axes.set_xlim([0,lado])
    axes.set_ylim([0,lado])
    # plt.text(0.92*L,0.9*L,'sus',fontsize = 10, color = 'g', backgroundcolor = 'w')
    plt.savefig('grafico1.png',dpi = 300, bbox_inches='tight')
    plt.close() 

def grafico_posicoes_Phi(posicoes,grafo,centro,raio):
    dicionario = {}
    for i3 in range(Nv):
        dicionario[nos[i3]] = [posicoes.posX[i3],posicoes.posY[i3]]
    #lista_links, Nedges = cria_lista_links(conexoes)
    #grafo = nx.Graph()
    #grafo.add_nodes_from(nos)
    #grafo.add_edges_from(lista_links)
    Phimax = max(posicoes.Phi)
    Phimin = min(posicoes.Phi)
    nodes = nx.draw_networkx_nodes(grafo, with_labels=True, pos = dicionario, node_size = 35, node_color = posicoes.Phi, vmin = Phimin, vmax = Phimax, cmap = 'inferno', node_shape = 'o', linewidth = 1.0)
    nx.draw_networkx_edges(grafo, with_labels=True, pos = dicionario, width = 0.5, edge_color = 'k')
    title2 = r'$M=$ '+str(Nv)+r', $\delta=1$.'
    #plt.title(title2, fontsize = 16)
    clb = plt.colorbar(nodes)
    clb.set_label(r'$\Phi$', fontsize = 16, labelpad=-40, y=1.05, rotation=0)
    plt.xlabel(r'$x$',fontsize = 16)
    plt.ylabel(r'$y$',fontsize = 16)
    plt.grid(True)
    plt.axis('scaled')
    plt.xticks(size=14)
    plt.yticks(size=14)
    lado = math.sqrt(float(Nv) / 0.0512 )
    trajetoria = plt.Circle(centro, raio, edgecolor = 'b', facecolor = 'none')
    axes = plt.gca()
    axes.add_artist(trajetoria)
    axes.set_xlim([0,lado])
    axes.set_ylim([0,lado])
    # plt.text(0.92*L,0.9*L,'sus',fontsize = 10, color = 'g', backgroundcolor = 'w')
    plt.savefig('figura_19_NK.pdf',dpi = 300, bbox_inches='tight')
    plt.close()

###############################################################

folder = "/home/paulo/Dropbox/Profissional/usp/Mobilidade/"
folder += "resultados/dinamica10_Paulo/res73/"
posicoes, Nv = cria_posicoes(folder +'rede.txt')
nos = [i+1 for i in range(Nv)]
conexoes, Nedges = cria_lista_links(folder +'links.txt')
grafo = nx.Graph()
grafo.add_nodes_from(nos)


rho = 512/1e4
delta = 1.0

raio = delta / math.sqrt(rho)

centro = (20.3459606,20.3631611)



grafo.add_edges_from(conexoes)
#grafico_posicoes(posicoes,grafo,centro,raio)
grafico_posicoes_Phi(posicoes,grafo,centro,raio)








