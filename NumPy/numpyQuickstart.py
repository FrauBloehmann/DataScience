import numpy as np 

a = np.arange(15).reshape(3, 5)
print(a)
# [[ 0  1  2  3  4]
# [ 5  6  7  8  9]
# [10 11 12 13 14]]
print("\n")
print("Shape of a: ", a.shape)
print("ndim of a: ", a.ndim)
print("Type of elements of a: ", a.dtype.name)
print("itemsize (in byte): ", a.itemsize)
print("Anzahl Elemente von a : ", a.size)
print("Datentyp von a : ", type(a))

b = np.array([6, 7, 8])
print("")
print("b: ", b)
#[6 7 8]
print("Datentyp von b: ", type(b))

print("")
c = np.array([2, 3, 4])
print("Datentyp von c: ", c.dtype.name)

#To create sequences of numbers, NumPy provides the arange function which is analogous to the Python built-in range, but returns an array.
d = np.arange(10, 30, 5)
print("")
print("d: ", d)
# it accepts float arguments
e = np.arange(0, 2, 0.3)  
print("")
print("e: ", e)

# Basic Operations: Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result
f = np.array([2, 3, 4])
print("")
print("b: ", b, "f: ", f)
print("b + f: ", b + f)
print("b * f: ", b * f)
print("welche Elemente von b sind kleiner als 8: ", b < 8)

# A @ B oder A.dot(B) -> matrix product
print("")
g = np.array([[1, 1],
              [0, 1]])
h = np.array([[2, 0],
              [3, 4]])
print("g: \n", g)
print("h: \n", h)
print("Matrixprodukt g x h: \n", g @ h)