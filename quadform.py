quit = False
import cmath
a = float(input("A:"))
b = float(input("B:"))
c = float(input("C:"))
d = (b**2) - (4*a*c)
if d == 0:
    print ("No Solution")
elif cmath.sqrt(d) == cmath.sqrt(-2 or 2):
    print ("This is a problem with the square root of negative 2. Please solve yourself.")
else:
    s1 = (-b + cmath.sqrt(d))/(2*a)
    s2 = (-b - cmath.sqrt(d))/(2*a)
    print("{} and {} are the answers".format(s1, s2))
