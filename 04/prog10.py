# Hausaufgaben

def ist_primzahl(zahl):
    if zahl < 2:
        return False;
    for teiler in range(2,zahl//2): # [2,zahl)
        if zahl % teiler == 0:
            #print("Teiler gefunden", teiler)
            return False
    return True

def weihnachtsbaum_zeichnen(höhe):
    #Mit Schleifen und Strings
    #Für jede Zeile werden zunächst die benötigten Leerzeichen und anschließend die benötigte Anzahl an Sternen berechnet. Durch die Multiplikation von Strings mit einer Zahl entstehen die entsprechenden Wiederholungen. Die beiden Strings werden anschließend zusammengefügt und als Zeile des Tannenbaums ausgegeben.
    for i in range (1, höhe+1):
        leerzeichen = " " * (höhe - i) #Anzahl Leerzeichen vor den Sternen
        sterne = "*" * (2 * i - 1)      #Anzahl Sterne
        print(leerzeichen + sterne)     #Verbindet die Strings

    #Stamm
    for i in range(2):
        leerzeichen_stamm = " " * (höhe - 1)
        print(leerzeichen_stamm + "*")

weihnachtsbaum_zeichnen(3)
weihnachtsbaum_zeichnen(16)

print( ist_primzahl(11777) )
# suchen einer Primzahl
for prim in range(1_000_041, 10_000_000, 2):
    if ist_primzahl(prim):
        print("{} ist eine Primzahl".format(prim))
        break
