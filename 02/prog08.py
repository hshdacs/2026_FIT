import copy
# Fallstricke

# komplexe Datentypen: mutable (veränderbare)
# Listen: list
# Wörterbücher: dict
# Mengen: set

# Fall 1
meine_liste = [1, 2, 3, 4]
zweite_liste = meine_liste
zweite_liste[1] = 17
print("meine_liste:", meine_liste)
print("zweite_liste:", zweite_liste)
print( id(meine_liste), id(zweite_liste) )

# Python: primitive Datentypen: immutable (unveränderbar)
# Zahlen: int, float, complex
# Boolesche Variablen: bool
# Zeichenkette: str
# Tupel: tuple
# Spezielle Datentypen: decimal, frozenset, bytes, range

a = 17
b = a
a = 47
print("a:", a)
print("b:", b)

x = "Hallo"
y = x
#x[1] = "e" # das geht nicht (immutable)
x = "Welt"
print(x, y)

k = (1, 2)
l = k
#k[1] = 0   # das geht auch nicht
k = (3, 4)
print(k, l)

# Wie kopiert man eine Liste
# Fall 1 - gelöst
meine_liste = [1, 2, 3, 4]
zweite_liste = meine_liste[:]
zweite_liste[1] = 17
print("meine_liste:", meine_liste)
print("zweite_liste:", zweite_liste)
print( id(meine_liste), id(zweite_liste) )

# Fall 2
lst1 = ['a', 'b', ['ab', 'ba']]
lst2 = lst1[:]
lst2[0] = 'x'
lst2[2][1] = 'xy'
print("lst1", lst1)
print("lst2", lst2)

# Fall 2 - gelöst
lst1 = ['a', 'b', ['ab', 'ba']]
lst2 = copy.deepcopy(lst1)
lst2[0] = 'x'
lst2[2][1] = 'xy'
print("(gel) lst1", lst1)
print("(gel) lst2", lst2)

