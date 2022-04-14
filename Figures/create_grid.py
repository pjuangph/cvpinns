import numpy as np 
import matplotlib.pyplot as plt 

#domain
L = [[0,1],[-2.5,2.5]]

#grid size
nx =[128,128]

#left and right states
Ul = [3.,0,3./.4]  # rho, rhou, E
Ur = [1.,0.,1./.4] # rho, rhou, E

x0 = np.linspace(L[0][0],L[0][1],nx[0]+1) # Time
x1 = np.linspace(L[1][0],L[1][1],nx[1]+1) # Spatial - x 

x0c = (x0[0:-1]+x0[1:])/2 # Center location for time (not dt)
x1c = (x1[0:-1]+x1[1:])/2 # center location for x (not dx)
xc = np.transpose(np.meshgrid(x0c,x1c,indexing='ij'),(1,2,0)) # t_1/2 and x_1/2 as meshgrid

x0 = x0[0:-1:16]
x1 = x1[0:-1:16]
x0c = (x0[0:-1]+x0[1:])/2 # Center location for time (not dt)
x1c = (x1[0:-1]+x1[1:])/2 # center location for x (not dx)
T,X  = np.meshgrid(x0,x1)
Tc, Xc =np.meshgrid(x0c,x1c)
skip = 1
plt.figure(num=1,figsize=(10,8))
for i in range(0,T.shape[0],skip):
    plt.plot(X[i,:],T[i,:],'k-')

for j in range(0,T.shape[1],skip):
    plt.plot(X[:,j],T[:,j],'k-')


for i in range(0,Tc.shape[0],skip):
    plt.plot(Xc[i,:],Tc[i,:],'bo')

for j in range(0,Tc.shape[1],skip):
    plt.plot(Xc[:,j],Tc[:,j],'bo')


plt.savefig('domain.png',dpi=300)