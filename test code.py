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