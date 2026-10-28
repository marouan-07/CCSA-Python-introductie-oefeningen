def maximale_blootstelling(db):
    if db < 80:
        return -1.0
    
    # Bereken hoeveel stappen van 3 dB we boven 80 zitten
    stappen = int((db - 80) // 3)
    
    # Basis tijdsduur is 8 uur = 28800 seconden, telkens halveren per stap
    tijd = 28800.0 / (2 ** stappen)
    
    return tijd

print(maximale_blootstelling(40))