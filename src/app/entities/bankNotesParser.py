def NotesToMoney(notes:dict):
    total = 0
    for value in notes.keys():
        total += int(value) * notes[value]
    return total
