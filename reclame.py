#12
from algemene_functies import mijn_functie_2

def mijn_functie_2(korte_lijst):
    return sum(korte_lijst)

def hoog_en_laag(invoer_lijst):
    hoogste = max(invoer_lijst)
    laagste = min(invoer_lijst)
    return [hoogste, laagste]

def meervoudig(invoer_lijst):
    if len(invoer_lijst) < 5 or len(invoer_lijst) > 10:
        raise ValueError("De lijst moet tussen de 5 en 10 elementen bevatten.")
    return hoog_en_laag(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)  
    resultaat = mijn_functie_2(korte_lijst)  
    return resultaat

if __name__ == "__main__":
    invoer_lijst_2 = [10, 5, 3, 2, 1, 2, 9] 
    resultaat = combinatie(invoer_lijst_2)  
    print(f"Het resultaat van de combinatie is: {resultaat}")

#5
def mijn_aanbieding_1():
    tabel = {
        "smaak": "aardbei",
        "prijs": 4,
        "korting": 0.1
    }
    nieuwe_prijs = tabel["prijs"] * (1 - tabel["korting"])

    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {tabel['smaak']}, "
          f"van €{tabel['prijs']} naar €{nieuwe_prijs:.2f}!")

#6
def inkomsten_totaal():
    inkomsten = [220, 430, 125, 160, 205, 90, 345]
    totaal = sum(inkomsten)
    return totaal
totaal= inkomsten_totaal()
print(f"Het totaal van de inkomsten is:{totaal}")

#7
def inkomsten_totaal(btw):  
    inkomsten = [220, 430, 125, 160, 205, 90, 345]
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw

    return f"Het totaal van alle inkomsten van dee week is {totaal:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
btw_percentage = 0.09
resultaat = inkomsten_totaal(btw_percentage)
print(resultaat)

#8
def hoog_laag(mijn_lijst):
      if len(mijn_lijst) != 7:
        raise ValueError("De lijst moet precies 7 waarden bevatten.")
      hoogste = max (mijn_lijst)
      laagste = min (mijn_lijst)
      return [hoogste, laagste]

inkomsten = [220, 430, 125, 160, 205, 90, 345]
resultaat = hoog_laag(inkomsten)
print(resultaat)

#9
def gemiddelde(mijn_lijst):
      if len(mijn_lijst) != 7:
        mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
      totaal = sum(mijn_lijst)  
      return totaal / len(mijn_lijst)
      
resultaat = gemiddelde([220, 430, 125, 160, 205, 90, 345])
print(f"Het gemiddelde van de inkomsten is: {resultaat:.2f} euro")

#10 
def gemiddelde(mijn_lijst):
      if len(mijn_lijst) != 7:
        mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
      totaal = sum(mijn_lijst)  
      return totaal / len(mijn_lijst)

def inkomsten_totaal():
    inkomsten = [220, 430, 125, 160, 205, 90, 345]
    totaal = sum(inkomsten)
    return totaal
totaal = inkomsten_totaal()
resultaat = gemiddelde([220, 430, 125, 160, 205, 90, 345])

print(f"Het totaal bedrag aan inkomsten deze week is: {totaal:.2f} euro")
print(f"De gemiddelde inkomsten deze week zijn: {resultaat:.2f} euro")

#11
def hoog_en_laag (invoer_lijst):
    hoogste = max(invoer_lijst)
    laagste = min(invoer_lijst)
    return{hoogste, laagste}

def meervoudig(invoer_lijst):
    if len(invoer_lijst) < 5 or len (invoer_lijst) > 10:
        raise ValueError("De lijst moet tussen de 5 en 10 elementen bevatten.")
    return hoog_en_laag(invoer_lijst)

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
resultaat = meervoudig(invoer_lijst)
print(f"De hoogste en de laagste waarde in de lijst zijn: {resultaat}")
