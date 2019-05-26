import Interfejs        #inicjalizacja zapytań do użytkownika
import pobierz_dane     #pobranie danych zadanego plik csv
import zadania          #Metody realizujące zadania 1-5
import polacz_z_sqlite3 #Zapis i odczyt z sqlite

def main():
        print("*** Analiza zdawalności matur w latach 2010-2018 ***")
        dowykonania = Interfejs.PoleceniaDoWykonania() #dowykonania przechowuje dane wpisane przez użytkownika
        zbiordanych = pobierz_dane.ZarzadzanieDanymi()
        zbiordanych.WczytajDane(dowykonania[6])
        zbiordanych.KorM(dowykonania[1])
        if (dowykonania[7]=='tak'):
            polacz_z_sqlite3.ZapiszSQLite(zbiordanych.Dane)
        #print(zbiordanych.Dane)
        wykonajzadanie = zadania.WykonajZadanie(zbiordanych.Dane, dowykonania)
        wykonajzadanie.Wykonaj()




print("\n ************ Witaj w programie **************")

warunek = True

while warunek:
    x = ""
    main()
    print("Co dalej? \n T - Wykonaj następną analizę  \n N - Zakończ")
    while x != "T" and x !="N":
        x = input()
        if x == "N":
            warunek = False