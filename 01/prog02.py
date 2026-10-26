#print("Geben Sie eine Zahl ein: ", end="")

# klassisches EVA (Eingabe/Verarbeitung/Ausgabe)

# eingabe_ist_korrekt = False # Flag
# while not eingabe_ist_korrekt:
#     zahl = input("Geben Sie Ihr Geburtsjahr ein: ")
#     # print("Zahl entählt nur Ziffern:", zahl.isdigit() )
#     eingabe_ist_korrekt = zahl.isdigit()
#     if not eingabe_ist_korrekt:
#         print("Bitte nur Ziffern eingeben!")

# zweite Möglichkeit für eine "fuß"-gesteuerte Schleife
while True: # Endlosschleife
     zahl = input("Geben Sie Ihr Geburtsjahr ein: ")
     # print("Zahl entählt nur Ziffern:", zahl.isdigit() )
     if zahl.isdigit():
        break # wir verlassen die Schleife sofort!
     print("Bitte nur Ziffern eingeben!")

geburtsjahr = int(zahl) # umwandeln in eine Zahl

#        (int)  (str)
#alter = 2026 - zahl
alter = 2026 - geburtsjahr

print("Sie sind ungefähr", alter, "Jahre alt")
