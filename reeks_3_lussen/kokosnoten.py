piraten = int(input())
kokosnoten = int(input())

def aantal_kokosnoten(aantal):
    if aantal == 0:
        return("geen kokosnoten")
    elif aantal == 1: 
        return("1 kokosnoot")
    else:
        return(f"{aantal} kokosnoten")

for n in range(1, piraten + 1):
    # 1. Hoeveel krijg piraat n? 
    # Dat is 1/p-de van de huidige k. (gehele deling: k // p)
    deel = kokosnoten // piraten
    
    # 2. Hoeveel krijgt de aap? 
    # Dat is de rest van de deling als je k deelt door p (k % p)
    aap = kokosnoten % piraten
    
    # 3. Print de zin volgens het gevraagde formaat
    print(f"{aantal_kokosnoten(kokosnoten)} = {aantal_kokosnoten(deel)} voor piraat#{n} en {aantal_kokosnoten(aap)} voor de aap")
    
    # 4. Bereken hoeveel noten er overblijven voor de volgende piraat
    # (Het initiële aantal min wat de piraat wegneemt en wat de aap krijgt)
    kokosnoten = kokosnoten - deel - aap