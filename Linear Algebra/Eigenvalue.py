#### Eigenvalue and Eigenvector

import numpy as np

"""
A·V = λ·V
λ: Eigenvalue
V: Eigenvector
"""

A = np.array([[3.14, 1.59, 2.65],
              [2.71, 8.28, 1.82],
              [6.62, 6.06, 8.96]])

print("The Source Matrix：\n{}".format(A))

λ, V = np.linalg.eig(A)

print("The eigenvalue：\n{}" .format(λ))
print("The eigenvector：\n{}".format(V))

print("Print every eigenvalues and the corresponding eigenvectors.")
for n in range(0,len(V)):
    val = λ[n]
    vec = V[:,n]
    lef = np.dot(A,  vec)
    rig = np.dot(val,vec)
    print("The eigenvalue: %f corresponds eigenvector:" %val, vec, ";")
    print("Then, A·V equals:", lef, "and λ·V equals:", rig, ".\n")