import numpy as np

#material properties to decide how stress and strain affect it
Young_modulus = 210*10^9
Cross_section = 0.05
length = 10

#element stiffness matrix
k = (Young_modulus * cross_section/Length) * np.array([
  [1, -1],
  [-1, 1]
])
print(k)
