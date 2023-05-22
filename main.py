id = 1
def dodaj1produkt(id, nazwa, cena, ilosc):
    tab2 = []
    nazwa = str(input("wpisz nazwe produktu: "))
    cena = int(input("wpisz cene produktu: "))
    #cena = cena + " zł"
    ilosc = int(input("wpisz ilosc produktow: "))
    #ilosc = ilosc + " szt"
    tab2.append(id)
    tab2.append(nazwa)
    tab2.append(cena)
    tab2.append(ilosc)
    tablicaOgolna.append(tab2)

tablicaOgolna = []
tab2 = []
nazwa = ""
cena = 0
ilosc = 0
wybor = 0
num = 1
while wybor != 9:
    print("============================================")
    print("[ --- Wybierz z menu co chcesz zrobić  --- ]")
    print("============================================")
    print("[ 1 - dodaj wiele elementów do tablicy     ]")
    print("[ 2 - wyswietlanie tablicy                 ]")
    print("[ 3 - dodawanie elementu na koniec tablicy ]")
    print("[ 4 - usuwanie towaru                      ]")
    print("[ 5 - wybierz produkt po cenie             ]")
    print("[ 6 - wybierz produkt po nazwie            ]")
    print("[ 7 - sortuj po ilosci                     ]")
    print("[ 8 - usuwanie tablicy                     ]")
    print("[ 9 - wyjscie                              ]")
    print("============================================")
    print()
    wybor = int(input("wybierz opcję: "))

    if wybor == 1:
        zakres = int(input("Wpisz ile elementów chcesz dodać: "))
        for i in range(zakres):
            dodaj1produkt(id, nazwa, cena, ilosc)
            id = id + 1
    if wybor == 2:
        print('|||||||||||||||||||||||||||||||||')
        print('| id |   nazwa   | cena | ilosc |')
        print('|||||||||||||||||||||||||||||||||')
        for elementy in tablicaOgolna:
            print("| %-3d| %-10s| %-5d| %-5d |" % (elementy[0],elementy[1],elementy[2],elementy[3]))

    if wybor == 3:
        dodaj1produkt(id, nazwa, cena, ilosc)
        id = len(tablicaOgolna) + 1
    if wybor == 4:
        ind = int(input("wprowadz index do usuniecia"))
        ind = ind - 1
        tablicaOgolna.pop(ind)
    if wybor == 5:
        wyszukajPoCenie = int(input("Wybierz cenę którą chcesz wyszukać: "))
        for el in tablicaOgolna:
            if el[2] == wyszukajPoCenie:
                print(el)
    if wybor == 6:
        wyszukajPoNazwie = str(input("Wybierz nazwę produktu którą chcesz wyszukać: "))
        for el in tablicaOgolna:
            if el[1] == wyszukajPoNazwie:
                print(el)
    if wybor == 7:
        sorted_tablicaOgolna = sorted(tablicaOgolna, key=lambda x: x[3])
        for elementy in sorted_tablicaOgolna:
            print(elementy)
    if wybor == 8:
        del tablicaOgolna[:]
        id = 1

