import recursive

def toplam(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        return liste[0] + toplam(liste[1:])

liste = [2, 3, 4, 5, 6]
print(toplam(liste))