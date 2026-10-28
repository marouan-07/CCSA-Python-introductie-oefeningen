speler1 = input().strip()
speler2 = input().strip()

if speler1 == speler2:
    print("gelijkspel")
elif (
    (speler1 == 'schaar' and (speler2 == 'blad' or speler2 == 'hagedis')) or
    (speler1 == 'blad' and (speler2 == 'steen' or speler2 == 'Spock')) or
    (speler1 == 'steen' and (speler2 == 'hagedis' or speler2 == 'schaar')) or
    (speler1 == 'hagedis' and (speler2 == 'Spock' or speler2 == 'blad')) or
    (speler1 == 'Spock' and (speler2 == 'schaar' or speler2 == 'steen'))
):
    print("speler1 wint")
else:
    print("speler2 wint")