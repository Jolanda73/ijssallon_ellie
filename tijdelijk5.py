prijzen = {
"aardbei": 3,
"vanille": 4,
"chocolade": 5} 
aanbieding = prijzen ["vanille"] * 0.8

reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € { aanbieding:2f}"
reclame_tekst2 = reclame_tekst [:63]
print(reclame_tekst2)