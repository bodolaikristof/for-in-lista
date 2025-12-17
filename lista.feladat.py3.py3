lista = [1, 2, 3, 4, 6, 9, 12, 15, 18, 20, 21, 24, 30, 33, 36, 40]

harom_paros = []

for szam in lista:
    if szam % 3 == 0 and szam % 2 == 0:
        harom_paros.append(szam)
        
print("A 3-mal osztható páros számok a Listában:")
print(harom_paros)
print("A lista elemszáma:",len(harom_paros))