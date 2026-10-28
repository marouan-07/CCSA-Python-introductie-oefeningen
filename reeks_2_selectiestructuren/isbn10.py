# Maak een lege lijst aan
getallen = []

# Vraag 10 keer om een getal en voeg het toe aan de lijst
for i in range(10):
    getallen.append(int(input()))

# Bereken de som volgens de ISBN-10 formule uit de opgave
# x1 tot x9 komen overeen met index 0 tot 8 in de lijst
som = 0
for i in range(9):
    som += (i + 1) * getallen[i]

controle = som % 11

# Controleer of het controlegetal overeenkomt met het 10e cijfer (index 9)
if controle == getallen[9]:
    print("OK")
else:
    print("FOUT")