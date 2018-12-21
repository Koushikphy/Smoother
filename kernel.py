import numpy as np 
import matplotlib.pyplot as plt 
y=[191.78,191.59,191.59,191.41,191.47,191.33,191.25,191.33,191.48,191.48,191.51,191.43,191.42,191.54,191.5975,191.555,191.52,191.25,191.15,191.01]

x = np.linspace(1 ,20,len(y))
n=1


def gauss(u):
    return np.exp(-u**2/2)/np.sqrt(2*np.pi)

#epanechnikov kernel
def parabolic(u):
    if abs(u)<=1:
        return 0.75*(1-u*u)
    return 0 


def smoother(algo,x,y,n):
    yy=[]
    for xi in x:
        num = sum( algo((xi-i)/n)*j for i,j in zip(x,y)) 
        den = sum( algo((xi-xx)/n) for xx in x)
        y0=num/den
        yy.append(y0)
    return yy


yy = smoother(parabolic,x,y,5)


plt.plot(x,yy)
plt.plot(x,y)
plt.show()