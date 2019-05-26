
#Interfejs użytkownika, wybór poleceń

def PoleceniaDoWykonania():
#Dane z pliku czy z bazy sqlite
        print("\nCzy chcesz dane wczytać z bazy? \n  Wpisz tak (baza sqlite mydb.db tabela dane) lub nie (lokalny plik).")
        y = input()
        tak="tak"
        nie="nie"
        while y!=nie and y!=tak:
            print("Wpisz tak lub nie")
            y = input()

#Grupowanie tak / nie
        print("\n Czy chcesz grupować dane według płci? \n Wpisz tak lub nie.")
        x = input()
        plec="0"
        while x!=nie and x!=tak:
            print("Wpisz tak lub nie")
            x = input()

# Grupowanie wybór płci
        if x == tak:
            print("Wybierz płeć: \n k - jesli kobiety \n m - jesli mężczyźni")
            plec = input()
            while plec != "k" and plec != "m":
                print("Podaj k lub m :")
                plec = input()

#Czy zapisac w bazie sqllite
        print("\n Czy chcesz zapisać swoje dane w bazie sqlite? \n Wpisz tak lub nie.")
        p = input()
        while p!=nie and p!=tak:
            print("Wpisz tak lub nie")
            p = input()



#Wypisanie polceń
        print("Podaj numer polecenia z listy które chcesz wykonać:")
        Polecenia = ["Zad1","Zad2","Zad3","Zad4","Zad5"]
        for i in Polecenia:
            print(i)

#Wybór numeru polecenia do wykonania
        warunek = False
        z = ""
        #zad = input()
        #print(type(zad))
        zad = ""
        while zad.isdigit() == False or z < 1 or z > 5:
                print("podaj numer 1-5 :")
                zad = input()
                if zad.isdigit():
                    z = int(zad)

        rok = ""
        woj1 = ""
        woj2 = ""
        lista_wojewodztw = ["Dolnośląskie", "Kujawsko-pomorskie", "Lubelskie", "Lubuskie", "Łódzkie", "Małopolskie",
                        "Mazowieckie", "Opolskie", "Podkarpackie", "Podlaskie", "Pomorskie", "Śląskie",
                        "Świętokrzyskie", "Warmińsko-Mazurskie", "Wielkopolskie", "Zachodniopomorskie"]
        if z == 1 or z == 2 or z == 5:

            while (woj1 in lista_wojewodztw) == False :
                print("Podaj województwo:")
                woj1 = input()
            if z == 5:
                while (woj2 in lista_wojewodztw) == False or woj1 == woj2:
                    print("Podaj drugie województwo:")
                    woj2 = input()
        elif z == 3:
            while rok.isdigit() == False or int(rok) < 2010 or int(rok) > 2018:
                print("Podaj rok z przedziału 2010-2018: ")
                rok = input()


#Przypisanie wartości wybranych przez użytkowanika do listy
        dowykonania = [x, plec, zad, woj1, woj2, rok,y,p]
        return dowykonania

