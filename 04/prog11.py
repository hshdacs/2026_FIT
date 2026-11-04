import numpy as np
from numpy.random import random
from numpy import sin, cos
#import numpy.random as nr

# Addition zweier Vektoren (konventionell)
a = [1, 2, 3, 4]
b = [5, 3, 2, 1]
#c = a + b # Konkatenierung beider Listen
c = [ a[i] + b[i] for i in range( len(a) ) ]
print(c)

# Addition zweier Matrizen
A = [ [1, 2, 3], [4, 5, 6] ]
B = [ [2, 1, 0], [2, 2, 2] ]
#C = A + B - konkateniert die Listen
C = []
for i in range(len(A)):
    zeile = []
    for j in range( len( A[i] ) ):
        zeile.append(A[i][j] + B[i][j])
    C.append(zeile)
print(C)

x = np.array( a )
Y = np.array( A )
print("type(x)=", type(x))
print("type(Y)=", type(Y))
print("x=", x)
print("Y=", Y)

# Anlegen von Arrays
v = np.zeros( 9 ) # 9 ist ein skalar
print(v)
W = np.zeros( (5,3) ) # (5,3) ist ein tupel
print(W)
W = np.zeros( (5,3), dtype=int )
print(W)
E = np.eye(8)
print(E)
print("Dimensionen:", E.ndim)
print("Anzahl der Elemente:", E.size)
print("Größe eines Elements:", E.itemsize)
print("Speicherverbrauch:", E.nbytes)
print("Datentyp:", E.dtype)
print("Größe:", E.shape)

R = random( (5,5) )
print("R=", R)

# Addtion mit numpy
a = np.array( [1, 2, 3, 4] )
b = np.array( [5, 3, 2, 1] )
c = a + b
print("c=", c)

A = np.array([ [1, 2, 3], [4, 5, 6] ])
B = np.array([ [2, 1, 0], [2, 2, 2] ])
B_t = B.transpose()
C = A + B
print("C=", C)
print("A - B", A-B)
print("A**2", A**2)
print("A*B", A*B)
print("B'", B_t)
print("A x B", A.dot(B_t))
print("A @ B", A @ B_t)

# Indizierung (Basis 0)
print("A[0][0]=A[0,0]=", A[0,0])
print("A[0:1,:] = ", A[0:1,:])
print("A[:,1:2] = ", A[:,1:2])

print("sin a", sin(a))
y = sin(a)**2 + cos(b)**2
print("y=", y)

print(A)
print("Größter Eintrag:", A.max())
print("Kleinster Eintrag:", A.min())
print("Summe aller Einträge:", A.sum())
print("Summe pro Spalte:", A.sum( axis=0 ))
print("Summe pro Zeile:", A.sum( axis=1 ))
