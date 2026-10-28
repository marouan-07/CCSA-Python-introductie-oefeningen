def vertaling_toevoegen(woord, vertaling_woord, woordenboek):
    woordenboek[woord] = vertaling_woord

def vertaling(woord, woordenboek):
    if woord in woordenboek:
        return woordenboek[woord]
    else:
        return "???"

woordenboek = {}
vertaling_toevoegen('woman', 'vrouw', woordenboek)
vertaling_toevoegen('flower', 'bloem', woordenboek)
vertaling_toevoegen('thirsty', 'dorst', woordenboek)
vertaling_toevoegen('dog', 'hond', woordenboek)
vertaling_toevoegen('time', 'tijd', woordenboek)

print(woordenboek)

print(vertaling('dog', woordenboek))   # Verwacht: 'hond'
print(vertaling('house', woordenboek))  # Verwacht: '???'