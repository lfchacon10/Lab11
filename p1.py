import numpy as np
import matplotlib.pyplot as plt 
    
pw=1
cementacionM = [1.2,1.5,1.8,2.1,2.4]
porosidadO = np.linspace(0,1,1000) 

def mifun( M, O):
    return pw*(O**-M)

plt.title( "Resistividad en funcion de porosidad")
plt.xlabel("Porosidad")
plt.ylabel("Resistividad del Bloque")
plt.grid()

for i in range ( len(cementacionM)):
    lbl = "M: "+ str(cementacionM[i])
    plt.loglog( porosidadO, mifun(cementacionM[i] ,porosidadO) , label = lbl)
plt.legend(loc=0)
