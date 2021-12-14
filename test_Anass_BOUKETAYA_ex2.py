# *** exercice 2 ***

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 20)
dt=10/19                # t[1]-t[0]
Nnum = np.zeros(20) 
Ntot=100
alpha=0.01
Nnum[0]=1

for i in range(19):
    Nnum[i+1]=Nnum[i]+Nnum[i]*alpha*dt*(Ntot-Nnum[i])

Nalg=Ntot/(1+99*np.exp(-t))      #Solution algébrique

    
plt.plot(t,Nnum,t,Nalg)
plt.title("evolution du nombre d'individu infectés  ")
plt.ylabel("individu infecté")
plt.xlabel("temps")
plt.legend(['avec la méthode d euler','solution Algébrique'])

plt.show()

""" oui il y une différence entre les 2 courbes,
cette erreur est due à la discretisation du temps qui dans l'équation
differentielle est considere continue, pour minimiser l'erreur il faut ajouter
plusieurs points dans la liste t, plus le nombre de points t est grand 
plus l'erreur sera minimale """
