#Title: Lab #3 Least Common Multiple, Samme Qandil
#input: two positive ints a and b 
#output: prints the least common multiple 
import math
print ("please put two ints above zero please and thank you")
a = int(input())
b = int(input())

lcm = a * b / math.gcd(a, b)

print (lcm)
'''
so the lcm in number theory is basically just a *b / the gcd of a*b. Since we are allowed to use the math library of code, then I suppose we are allowed to use the gcd function 
'''
