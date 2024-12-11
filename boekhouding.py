import csv
# from Helper import decoreer, fooi_pp, onderstreep
#from presentatie import presenteer, totaal

inkomsten = {'Aarbeien-ijs-totaal': 1000,'Vanille-ijs-totaal': 2000, 'Chocolade-ijs-totaal': 1500, 'Waterijsjes-totaal':750}
totaal_inkomsten = sum (inkomsten.values())

for sleutel, waarde in inkomsten.items():
    print(f"{ sleutel} : { waarde} euro")
print("============")
print(f"totaal {totaal_inkomsten} euro")

with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
    writer.writerow([key.value])