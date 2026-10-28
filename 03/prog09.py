# Funktionen

# prinzipiell eine gute idee, aber macht zu viel!
def mittelwert(beschreibung, data_set: list):
    if not isinstance(data_set, list):
        print("Fehler, keine Liste für die Mittelwertberechnung")
        # Ende der Funktion, weil nix mehr funktionieren kann !?
        return
    #print("Wir sind in der Funktion mittelwert(...)")
    m_wert = sum(data_set)/len(data_set)
    print("Mittelwert {} = {:.2f}".format(beschreibung, m_wert))
    #print("Wir verlassen die Funktion mittelwert(...)")

def berechne_mittelwert(data_set: list) -> float:
    if not isinstance(data_set, list):
        print("Fehler, keine Liste für die Mittelwertberechnung")
        # Ende der Funktion, weil nix mehr funktionieren kann !?
        return 0
    return sum(data_set)/len(data_set)

def ausgabe_mittelwert(beschreibung, mittelwert: float):
    print("Mittelwert {} = {:.2f}".format(beschreibung, mittelwert))

def ausgabe_mittelwert_4nk(beschreibung, mittelwert: float):
    print("Mittelwert {} = {:.4f}".format(beschreibung, mittelwert))

data_list_1 = [12, 15, 2, 99, 43, 67, 8]
data_list_2 = [9, 12, 55, 76, 43, 13, 44, 63, 39]

ausgabe_mittelwert(1, berechne_mittelwert(data_list_1))
ausgabe_mittelwert_4nk(2, berechne_mittelwert(data_list_2))

# mittelwert(1, data_list_1)
# mittelwert(2, data_list_2)

# mittelwert_1 = sum(data_list_1)/len(data_list_1)
# print("Mittelwert 1 = {:.2f}".format(mittelwert_1))
# mittelwert_2 = sum(data_list_2)/len(data_list_2)
# print("Mittelwert 2 = {:.2f}".format(mittelwert_2))
