import pracownicy

krotka = (
    ['Anna', 'ANNECKA', 19, '00321298765', '500-900-789'],
    ['Beta', 'Beacka', 19, '98080898762', '600-300-800'],
    ['Cezary', 'Cezarski', '98030291234', 20, '400-234-456'],
    ['Dariusz', 'Darecki', '908-039-200', 17, '01241298763'],
    ['Franciszek', 'Francki', '99120498765', 18, '200-987-123'],
    ['Franciszek', '98120498765', 20, '900-987-123']
)

filePath = 'osoby.txt'

list = []
for x in range(0, krotka.__len__()):
    try:
        o = pracownicy.Osoba(krotka[x])
        list.append(o)
    except ValueError as vE:
        print("value error")

for x in range(0, list.__len__()):
    print(list[x])
    with open(filePath, "a+") as file:
        file.write(str(list[x]))
    file.close()