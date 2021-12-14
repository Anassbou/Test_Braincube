import scipy.integrate as integ
import numpy as np
import matplotlib.pyplot as plt

Ntot=100
N0 = np.array([1])  #conditon initiale


def f(t,N):
    return 0.01*N*(Ntot-N)

solution=integ.solve_ivp(f,[0, 10],N0,method='LSODA') 

#*******pour tracer les 3 courbes************
t = np.linspace(0, 10, 20)
dt=10/19                # t[1]-t[0]
Nnum = np.zeros(20) 
Ntot=100
alpha=0.01
Nnum[0]=1

for i in range(19):
    Nnum[i+1]=Nnum[i]+Nnum[i]*alpha*dt*(Ntot-Nnum[i]) #solution numerique d'euler

Nalg=Ntot/(1+99*np.exp(-t))      #Solution algébrique

    
plt.plot(t,Nnum,t,Nalg,solution.t,solution.y[0],'o')
plt.title("evolution du nombre d'individu infectés  ")
plt.ylabel("individu infecté")
plt.xlabel("temps")
plt.legend(['avec la méthode d euler','solution Algébrique','solution avec scipy LSODA'])

plt.show()

