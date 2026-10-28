# set

# Vergleich list vs set
# list: geordnete Menge, doppelte Einträge
# set: ungeordnete Menge, keine doppelten Einträge

leeres_set = set()
print(leeres_set, type(leeres_set))

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
print(A, B)

print( "2 in A", 2 in A)
print( "9 in B", 9 in B)

# Operationen mit sets
print("Vereinigung A und B", A.union(B))
print("ebenso", A | B)  # A oder B
print("Schnittmenge A und B", A.intersection(B))
print("ebenso", A & B)  # A und B
print("Differenz A und B", A.difference(B))
print("ebenso", A - B)

for x in A:
    print(x)