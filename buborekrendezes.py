import random
elemek = []
for i in range(0, 20):
    elemek.append(random.randint(0, 100))
print(elemek)
#valogatas
for rep in range(1, len(elemek)):
    for i in range(len(elemek)):
        valt=0
        if i != 19:
            if elemek[i] > elemek[i+1]:
                valt=elemek[i]
                elemek[i] = elemek[i+1]
                elemek[i+1] = valt
print(elemek)
