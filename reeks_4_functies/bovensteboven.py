def bovensteboven(n):
    # getal naar string om het te kunnen lezen
    s = str(n)

    # lege string van getal maken
    omgedraaid = ""

   # Loop door elk cijfer van achter naar voren (met reversed of negatieve stap)
    for cijfer in reversed(s):
        if cijfer == '0':
            omgedraaid += '0'
        elif cijfer == '3':
            omgedraaid += '3'
        elif cijfer == '6':
            omgedraaid += '9'
        elif cijfer == '8':
            omgedraaid += '8'
        elif cijfer == '9':
            omgedraaid += '6'
        else:
            # Als er een ongeldig cijfer in zit (bijv. 1, 2, 3, 4, 5, 7), kan het niet
            return False
            
    # Controleer of het omgedraaide getal gelijk is aan het origineel
    return int(omgedraaid) == n

def volgende(n):
    huidige = n + 1
    while not bovensteboven(huidige):
        huidige += 1
    return huidige

print(bovensteboven(2965))
print(volgende(1961))