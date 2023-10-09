from math import gcd
from sympy import mod_inverse

e = int(input("Enter e: "))

phi = int(input("Enter phi: "))

if gcd(e, phi) == 1:
    d =mod_inverse(e, phi)
    print("d = ", d)
else:
    print("unsuccessful")
