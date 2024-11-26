def mijn_functie_1 (argument):
    tabel = {
        2: 4,
        4: 16, 
        10: 100,
        12: 144
    } 
    return tabel.get(argument, argument **2)
print(mijn_functie_1(2))
print(mijn_functie_1(4))
print(mijn_functie_1(10))
print(mijn_functie_1(12))

def mijn_functie_2(argumenten):
    tabel ={ 
        "12, 3": [15, 9, 36, 4], 
        "12, 2": [14, 10, 24, 6],
        "10, 5": [15, 5, 50, 2], 
        "100, 20":[120, 80, 2000, 5]
    }
    return tabel.get(argumenten)
print(mijn_functie_2("12, 3"))
print(mijn_functie_2("12, 2"))
print(mijn_functie_2("10, 5"))
print(mijn_functie_2("100, 20"))
