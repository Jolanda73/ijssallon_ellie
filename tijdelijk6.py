prijzen = {
"aardbei": 3,
"vanille": 4,
"chocolade": 5} 
aanbieding = prijzen ["vanille"] * 0.8

reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € { aanbieding:2f}"
reclame_tekst2 = reclame_tekst [:63]

reclame_tekst3 = reclame_tekst2.upper()

reclame_tekst4 = [reclame_tekst3]

el = reclame_tekst4
print(el)

reclame_tekst4 = ["Vandaag", "in", "de", "aanbieding", ":", "vanille-ijs", "1 liter", "-", "slechts", "€", 3.20]
for el in reclame_tekst4:
	print(el)