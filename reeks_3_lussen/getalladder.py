# Lees het aantal trappen in
n = int(input("Geef een geheel getal in: "))

# Buitenste lus voor elke trap van 1 tot n
for i in range(1, n + 1):
    # Binnenste lus voor de cijfers op de huidige trap van 1 tot i
    for j in range(1, i + 1):
        print(j, end="")
    # Print een lege enter om naar de volgende regel te gaan voor de volgende trap
    print()