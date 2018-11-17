#FINAL CON TODO
%pylab inline
#Para circuito en Serie
x = linspace(0,1,90)
y=  x[:]+1000*(1-x[:])
plt.title("Resistividad en funcion de longitud, P(L)")
plt.xlabel("L")
plt.ylabel("P")
plt.grid()
plt.plot(x,log(y), label = "Circuito en serie")
#Para circuito en Paralelo
#P(0)=1000 , P(1)=1
y= 1000/(1000*x[:]+1 -x[:])
plt.plot(x,log(y), label = "Circuito en paralelo")

pw=1

def mifun( M, O):
    return pw*(O**-M)

plt.plot(x, log(mifun(1,x)), label = "Archie M=1")
plt.plot(x, log(mifun(2,x)), label = "Archie M=2")
plt.legend(loc=0)
