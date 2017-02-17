import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

#a variavel independente, t, deve ser o primeiro argumento
def tensaocarga(t, epsilon, tau):
	f = epsilon*(1-np.exp(-t/tau))
	return f

#importando os dados
filename = 'dados_carga_capacitor.csv' #name of the file
# filename = 'carga_aline.csv' #name of the file
f = open(filename, 'r') 
tem = [] #create a list
tens = [] 
for line in f:
	a, b = line.split(',')
	tem.append(float(a)) #corrente em mA
	tens.append(float(b))
f.close()

#converte as listas em arrays
tempo = np.array(tem) #tempo em segundos
tensao = np.array(tens) #tensao em V

chute = [10,100] #initial values

par, err = curve_fit(tensaocarga, tempo, tensao, chute)

err_eps = np.sqrt(err[0,0])
err_tau = np.sqrt(err[1,1])

print par
print err_eps, err_tau

epsilon= round(par[0],2) # valor ajustado para a resistencia
tau = round(par[1],1) # valor ajustado para a tensao residual

e_eps = round(err_eps,2)
e_tau = round(err_tau,1)

ajuste = tensaocarga(tempo, epsilon, tau)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
nome = 'carga_capacitor.png'
plt.plot(tempo, tensao, 'ob', ms = 10, label='Experimento' )
plt.plot(tempo, ajuste,'-r', lw = 4, label= r'Ajuste $V_c(t)$' )
plt.legend(loc='lower right',fontsize = 20)
plt.title('Carga do capacitor',fontsize=20)
plt.xticks(color='k', size=20)
plt.yticks(color='k', size=20)
plt.grid(True)
plt.xlabel('Tempo t (s)', {'color': 'k','fontsize': 20}) #k indica cor preta
plt.ylabel('Tensao $V_c$ (V)', {'color': 'k','fontsize': 20})
plt.text(300, 6, r'$\varepsilon = ($'+str(epsilon)+r'$\pm$'+str(e_eps)+') V',{'fontsize': 20}) 
plt.text(300, 4, r'$\tau = ($'+str(tau)+r'$\pm$'+str(e_tau)+') s',{'fontsize': 20}) 
plt.savefig(nome)
plt.show()

