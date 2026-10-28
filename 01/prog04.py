import math
import sys

# Einige Tricks in Python
# (bitte mit Vorsicht verwenden)

a = 5
b = 7
x, y = 3, 9
a, b = b, a
c = d = e = 4
z = 23

print("+" + ("-"*20) + "+")
print("|{:>20}|".format(a))
print("|{:<20}|".format(y))
print("|{:^20}|".format(math.pi))
print("+" + ("-"*20) + "+")

print("{:10.3f}".format(math.e))
print("{:10.3e}".format(math.e))

print("Dezimal {:d}".format(z))
print("Octal {:o}".format(z))
print("Hexadezimal {:x}".format(z))
print("Binär {:b}".format(z))

i  = 5; print(i) # Zuweisungsoperator (=)
i += 5; print(i) # i = i + 5
i -= 5; print(i)
i *= 5; print(i)
i **=5; print(i) # i hoch 5
i /= 5; print(i)
i //=5; print(i) # ganzzahlige Division
i %= 5; print(i) # Modulo (Rest der ganz. Div.)

i = float('inf')
print(i)
print(i-i) # nan - not a number
print(sys.float_info)
print(sys.int_info)

a = 4
b = 10.5
print("a < b", a < b)
print("a > b", a > b)
print("a <= b", a <= b)
print("a >= b", a >= b)
print("a == b", a == b)
print("a != b", a != b)
