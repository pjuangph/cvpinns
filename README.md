# Control Volume Physics-informed Neural Networks

This code implements the Control Volume Physics-informed Neural Networks (CVPINNs) method in [1]. `cvpinns.py` implements the `PDE` class. Objects of this class are constructed with mesh, quadrature rule, and PDE specifications, and provide the `getRES` function for computing CVPINNs residuals. `euler.ipynb` is an example script applying CVPINNs to recover the equation of state from the analytical solution to a Sod shock problem.

Python >= 3.5  
numpy  
scipy  
matplotlib  
toolz  
tensorflow >= 2.2  

SAND No: SAND2021-2386 O

[1] R. G. Patel, I. Manickam, N. A. Trask, M. A. Wood, M. Lee, I. Tomas, E. C. Cyr. Thermodynamically consistent physics-informed neural networks for hyperbolic systems. arXiv preprint arXiv:2012.05343, 2020.

> **Displaying Math**: This repository contains a lot of math equations. Github currently does not display latex equations. If you want to see the equations, I reccomend installing xhub google chrome: [xhub](https://github.com/nschloe/xhub)

# How does this work? 
This is a breakdown of the code and where things come from. 

## Creating the Domain 

```python
#domain
L = [[0,1],[-2.5,2.5]] # 0 to 1 is the time, -2.5 to 2.5 is the xmin and xmax values 

#grid size
nx =[128,128] # Here the author is setting the number of discretizations in time and x


#left and right states
Ul = [3.,0,3./.4]  # rho, rhou, E
Ur = [1.,0.,1./.4] # rho, rhou, E

#compute analytical solution
# What is going on here is a linspace from 0 to 1 128 points by -2.5 to 2.5 128 points 
# Since this is mgrid it's 3 dimensions (2,128,128) first dimension (0,:,:) corresponds to the time for each of the points. second dimension (1,:,:) is the points in x. This is like a linspace nx[0]*1j = 128 which is number of steps linspace(0,1,128)

x_data = np.transpose(np.mgrid[L[0][0]:L[0][1]:nx[0]*1j,
                               L[1][0]:L[1][1]:nx[1]*1j],(1,2,0))  
```

## Quadrature Specifications? 
```python
#quadrature specification. 3 segment composite trapezoid
pts=4
xi = np.linspace(-1,1,pts)
wi = np.array([1.] + [2. for _ in range(pts-2)] + [1.])
wi = 2.*wi/sum(wi)


quad = {'0':(xi,wi),'1':(xi,wi)}
```
