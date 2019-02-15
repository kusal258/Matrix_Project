import numpy as np
import matplotlib.pyplot as plt
P=np.array([1,0])
C=np.array([-1,-2])
r=2*(np.sqrt(2))
len=5000
x_PC=np.zeros((2,len))
D=np.linspace(0,2,len)
v=np.linspace(-(np.pi)/2,(3*np.pi)/2,len)
Z=np.zeros((2,len))
for i in range(len):
	 dia=P+D[i]*(C-P)
	 x_PC[:,i]=dia.T
	 T_1=np.array([(-1+r*np.cos(v[i])),(-2+r*np.sin(v[i]))])
	 Z[:,i]=T_1.T
Q=P+D[len-1]*(C-P)
print Q
plt.plot(x_PC[0,:],x_PC[1,:],label='$diameter$')
plt.plot(Z[0,:],Z[1,:],label='$circle$')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1-0.04),Q[1]*(1),'Q')
plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1+0.1),P[1]*(1-0.1),'P (1,0)')
plt.plot(C[0],C[1],'o')
plt.text(C[0]*(1-0.1),C[1]*(1),'C (-1,-2)')
plt.legend(loc='best')
plt.grid()
plt.show()
