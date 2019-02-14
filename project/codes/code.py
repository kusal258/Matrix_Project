import numpy as np
import matplotlib.pyplot as plt
L=np.array([1,1,-2])
D=np.array([1,1])
O=np.array([0,0])
d=np.abs((L[2])/np.sqrt(L[0]*L[0]+L[1]*L[1]) )
a=2*np.sqrt(3)*d
area=np.sqrt(3)*a*a/4
print(area,d)
A=np.array([1-np.sqrt(3),1+np.sqrt(3)])
B=np.array([1+np.sqrt(3),1-np.sqrt(3)])
C=np.array([-2,-2])
len=10
lam_1=np.linspace(0,1,len)
x_AB=np.zeros((2,len))
x_OD=np.zeros((2,len))
x_BC=np.zeros((2,len))
x_CA=np.zeros((2,len))
for i in range(len):
	temp1=A+lam_1[i]*(B-A)
	x_AB[:,i]=temp1.T
	temp2=O+lam_1[i]*(D-O)
	x_OD[:,i]=temp2.T
	temp3=B+lam_1[i]*(C-B)
	x_BC[:,i]=temp3.T
	temp4=C+lam_1[i]*(A-C)
	x_CA[:,i]=temp4.T
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_OD[0,:],x_OD[1,:],label='$OD$')
plt.plot(D[0],D[1],'o')
plt.plot(A[0],A[1],'o')
plt.plot(C[0],C[1],'o')
plt.text(D[0]*(1+0.1),D[1]*(1+0.1),'D')
plt.text(A[0]*(1-0.1),A[1]*(1+0.05),'A')
plt.text(C[0]*(1-0.1),C[1]*(1+0.05),'C')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1+0.02),B[1]*(1-0.1),'B')
plt.text(-0.1,0,'O')
plt.plot(O[0],O[1],'o')

plt.xlabel('&x&')
plt.ylabel('&y&')
plt.legend(loc='best')
plt.grid()
plt.show()
