# Houdt het aantal stappen bij
aantal_stappen = 0

def hanoi(n, bron="A", doel="C", hulp="B"):
    global aantal_stappen
    
    # Als dit de eerste aanroep is van buitenaf, reset de teller even
    # (handig als je de functie meerdere keren achter elkaar wilt testen)
    
    if n == 1:
        print(f"Schijf 1 van {bron} naar {doel}")
        aantal_stappen += 1
    else:
        # Stap 1: verplaats n-1 schijven van bron naar hulp
        hanoi(n - 1, bron, hulp, doel)
        
        # Stap 2: verplaats de grootste schijf (n) van bron naar doel
        print(f"Schijf {n} van {bron} naar {doel}")
        aantal_stappen += 1
        
        # Stap 3: verplaats de n-1 schijven van hulp naar doel
        hanoi(n - 1, hulp, doel, bron)

# Functie om de hoofdaanroep te doen inclusief het printen van de stappen zoals gevraagd
def los_hanoi_op(n):
    global aantal_stappen
    aantal_stappen = 0  # Reset teller
    
    hanoi(n)
    
    print(f"{aantal_stappen} stappen gedaan")


print(los_hanoi_op(4))