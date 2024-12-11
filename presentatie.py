presenteer = {'vis': 10, 'vlees': 25, 'overig': 15}
totaal = sum(presenteer.values())

for sleutel, waarde in presenteer.items():
    print(f"{sleutel} : {waarde } euro")
print("====================")
print(f"Totaal {totaal} euro")
