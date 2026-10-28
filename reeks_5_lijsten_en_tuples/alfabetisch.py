def alfabetisch(zin):
    # 1. Hak de zin in stukjes (woorden) op elke spatie
    woorden = zin.split()
    
    # 2. Sorteer de woorden alfabetisch
    gesorteerde_woorden = sorted(woorden)
    
    # 3. Plak de gesorteerde woorden weer aan elkaar met een spatie ertussen
    return " ".join(gesorteerde_woorden)

print(alfabetisch("Dit is een test"))