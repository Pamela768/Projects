'''This code solves quadratic equations
variable "squ" is the discriminant'''

import cmath
a = int(input("What is the value os a: "))
b = int(input("What is the value of b"))
c = int(input("What is the value of c: "))

squ = cmath.sqrt(b**2-(4*a*c))
add = -b + squ
sub = -b - squ

val_1= add/2*a
val_2 = sub/2*a

print (f"The values for the equation {a}x\u00b2 + {b}x + {c} are {val_1,val_2}")