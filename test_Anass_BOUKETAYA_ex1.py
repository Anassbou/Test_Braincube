# *** exercice 1 ***

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
    
    
plt.plot(t,Nnum)
plt.title("evolution du nombre d'individu infectés  ")
plt.ylabel("individu infecté")
plt.xlabel("temps")
plt.show()







    


    

