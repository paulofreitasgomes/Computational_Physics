import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#function y = Rx + Vr
def leideohm(x, R, Vr):
	f = R*x+Vr
	return f

#importando os dados
filename = 'dados_Ohm.txt' #name of the file
f = open(filename, 'r') 
corr = [] #create a list
tens = [] 
for line in f:
    a, b = line.split()
    corr.append(float(a)) #corrente em mA
    tens.append(float(b))
f.close()

#converte as listas em arrays
corrente = 1e-3*np.array(corr) #convertendo para A
tensao = np.array(tens) #V

#chute = [100,-0.9] #initial values

par, err = curve_fit(leideohm, corrente, tensao)

eres = np.sqrt(err[0,0])
eV0 = np.sqrt(err[1,1])

print par
print eres, eV0

res= round(par[0],1) # valor ajustado para a resistencia
#a multiplicacao por 1000 e por que a corrente esta em mA
V0 = par[1] # valor ajustado para a tensao residual

ajuste = corrente*res + V0

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
nome = 'ajuste_Lei_de_Ohm.png'
plt.plot(corrente, tensao, 'ob', ms=12, label='Dados' )
plt.plot(corrente, ajuste,'-r', lw = 4, label='$V = RI+V_0$')
plt.legend(loc='upper left')
plt.title('Lei de Ohm e Ajuste Linear',fontsize=20)
plt.xticks(color='k', size=20)
plt.yticks(color='k', size=20)
plt.grid(True)
plt.xlabel('Corrente I (A)', {'color': 'k','fontsize': 20}) #k indica cor preta
plt.ylabel('Tensao V (V)', {'color': 'k','fontsize': 20})
plt.text(0.06, 4,r'$R = ($'+str(res)+r'$\pm$'+str(round(eres,1))+r') $\Omega$',{'fontsize': 20}) 
plt.text(0.06, 2,r'$V_0 = ($'+str(round(V0,2))+r'$\pm$'+str(round(eV0,2))+r') V',{'fontsize': 20})
plt.savefig(nome) 
plt.show()

