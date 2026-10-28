# dict (aka Dictionary, Table, Map)

leeres_dict = {}
print(leeres_dict, type(leeres_dict))

übersetzung = {
    "house": "Haus",
    "cat": "Katze",
    "dog": "Hund",
    2: "two"
}

übersetzung[1] = "one"
print(übersetzung)
print(übersetzung["cat"])
print(übersetzung[1])
print( "mouse" in übersetzung )
print( "Katze" in übersetzung )
print( übersetzung.keys() )
print( übersetzung.values() )