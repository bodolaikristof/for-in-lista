import random

szamok = []

for i in range(10):
    veletlen = random.randint(0, 50)
    
    if veletlen % 4 == 0:
         szamok.append(veletlen)
         
print("A 4-gyel osztható számpk Listája:")
print(szamok)
         
print("A lista elemeinek száma:",
len(szamok))      