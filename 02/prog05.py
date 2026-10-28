# list

# Camel Case "leereListe"
# Snake Case "leere_liste"
leere_liste = []
print(leere_liste)

ganze_zahlen = [1, 2, 3, 4, 5]
print(ganze_zahlen)

wilde_liste = [1, -3, 4.7, 'x', ['y', True]]
print(wilde_liste)

# Iteration (durch alle Elemente gehen)
for element in wilde_liste:
    print(element, type(element))

# Listenoperationen
x = 'x'
print("x in wilde_liste", x in wilde_liste )
print("x not in wilde_liste", x not in wilde_liste )
print("wilde_liste + ganze_zahlen", wilde_liste + ganze_zahlen )
print("wilde_liste * 2", wilde_liste * 2 )

print("wilde_liste[2]", wilde_liste[2])
print("wilde_liste[1:4]", wilde_liste[1:4])
print("wilde_liste[0:3:2]", wilde_liste[0:3:2])
print("wilde_liste[3:]", wilde_liste[3:])
print("wilde_liste[:2]", wilde_liste[:2])
print("len(wilde_liste)", len(wilde_liste))
print("wilde_liste.count(x)", wilde_liste.count(x))
print("wilde_liste.append(17)", wilde_liste.append(17))
print("wilde_liste.insert(0,47)", wilde_liste.insert(0, 47))
print("sum(ganze_zahlen)", sum(ganze_zahlen))
print("max(ganze_zahlen)", max(ganze_zahlen))
del wilde_liste[2]
print("nach del wilde_liste[2]:", wilde_liste)

# Listengeneratoren
n = 100
lange_liste = [7]*n
print(lange_liste, len(lange_liste))

# List Comprehensions

quadrat_zahlen = [ k**2 for k in ganze_zahlen ]
print(quadrat_zahlen)

differenz_liste = [ a - b for a,b in zip(quadrat_zahlen, ganze_zahlen) ]
print(differenz_liste)

# Allgemeine Syntax: ... for ... in ... [if ...]

A = [1, 2, 3, 4]
print("A:", A)
print( [k for k in A] )
print( [k+5 for k in A if k > 1] )
print( [(k,l) for k in A for l in A] )

# Tupel (ähnlich einer Liste, aber nicht mehr veränderbar)
t = ("hallo", 7)
print(t, type(t))

