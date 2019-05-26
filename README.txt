***Informacje o autorze***

Autor:			Emilia Lewandowska
Email:			emilka1611@gmail.com
Data utworzenia:	24.05.2019


***Opis projektu***

Aplikacja realizuj�ca zadanie polegaj�ce na analizie pliku z strony https://dane.gov.pl/dataset/1567/resource/17363 zawieraj�cego dane dotyczace analizy zdawalno�ci matur w latach 2010-2018.
Program pozwala przeanalizowa� zadany plik w celu wy�wietlenia danych zapyta� 1-5, na ekranie u�ytkownika. 
Odczyt danych z pliku lokalnego o nazwie "Liczba_os�b_kt�re_przystapi�y_lub_zda�y_egzamin_maturalny.csv" lub z bazy danych sqllite. 
U�ytkownik ma mo�liwo�� zapisania danych w bazie danych sqlite.

1) obliczenie �redniej liczby os�b, kt�re przyst�pi�y do egzaminu dla danego wojew�dztwa na przestrzeni lat, do podanego roku w��cznie, 
np.

2015 - 123456,


gdzie 123456 jest �redni� z lat (2010-2015)



2) obliczenie procentowej zdawalno�ci dla danego wojew�dztwa na przestrzeni lat, 
np.


2010 - 50 %

2011 - 52 %

2012 - 57 %

itd. ...


3) podanie wojew�dztwa o najlepszej zdawalno�ci w konkretnym roku, 
np.


rok - wojew�dztwo A



4) wykrycie wojew�dztw, kt�re zanotowa�y regresj� (mniejszy wsp�czynnik zdawalno�ci w kolejnym roku), je�eli takowe znajduj� si� w zbiorze, 
np.


wojew�dztwo A: 2012 -> 2013

wojew�dztwo B: 2017 -> 2018



5) por�wnanie dw�ch wojew�dztw - dla podanych dw�ch wojew�dztw wypisanie, kt�re z wojew�dztw mia�o lepsz� zdawalno�� w ka�dym dost�pnym roku, 
np. przy por�wnaniu wojew�dztwa A i B


2010 - A

2011 - B

2012 - B

2013 - A

itd. ...



***Wymagania techniczne i technologia wykorzystana***

- Python 3.7

- Do realizacji zada� 1-5 ko�ystano z funkcji dost�pnych w standardowej bibliotece

- Obs�uga po��czenia z baz� wyko�ystuj�c biblioteke sqlite3

Za�o�enia:
- zak�adamy istnienie bazy dabych sqlite o nazwie mydb.db

Testowanie:
- testy pytest wybranych funkcji 
- aplikacja uruchamiana i testowana na urz�dzeniu z systemem Microsoft Windows 10 Home, z wyko�ystaniem �rodowiska PyCharm.


***Opis interfejsu***

Interfejs u�ytkownika sk�ada si� z wy�wietlanych pyta�, u�ytkownik zgodniez instrukcjami odpowiada na pytanie wpisuj�c s�owo.

Pytania i dost�pne odpowiedzi:

Pytanie:	"Czy chcesz dane wczyta� z bazy?"
Odpowiedzi:	"tak" (baza sqlite mydb.db tabela dane) / "nie" (lokalny plik).

Pytanie:	"Czy chcesz grupowa� dane wed�ug p�ci?" 
Odpowiedzi:	"tak" / "nie"


Pytanie:	"Czy chcesz zapisa� swoje dane w bazie sqlite?" 
Odpowiedzi:	"tak" / "nie"


Pytanie:	"Podaj numer polecenia z listy kt�re chcesz wykona�:" 
Odpowiedzi:	'1' / '2' / '3' / '4' / '5'

Je�eli zad1, zad2 oraz dw�krotnie dla zad5. 
Pytanie : 	"Podaj wojew�dztwo:"
Odpowiedzi:	Nazwa wojew�dztwa	

Je�eli zad3
Pytanie:	"Podaj rok z przedzia�u 2010-2018:" 	
Odpowiedzi:	Liczba z przedzia�u 2010 - 2018
	

Pytanie:	"Co dalej?"	
Odpowiedzi:	T - Wykonaj nast�pn� analiz� / N - Zako�cz


Powy�sze zapytania wykonywane s� cyklicznie je�li u�ytkonik zdecyduje si� na kontynuacje analiz.


***Opis funkcji, spos�b wywo�ania i przyk�adowy kod.***

Aplikacja uruchamiana jest z pliku "plik_glowny.py".
Plik ten zawiera funkcj� main(), odpowiada za generowanie zapytania. 
Dane dotycz�ce wybranych opcji przez u�ytkownika przechowywane s� i przekazyane do poszczeg�lnych funkcji, w liscie o nazwie "dowykonania".

Klasa "WykonajZadanie" otrzymuje list� z danymi na kt�rych wykonuje zadanie oraz list� "dowykonania". Dowykonania przechowuje dane wpisane przez u�ytkownika, podczas wywo�ania funkcji z pliku interfejs. 
dowykonania = [czy grupowac , po kim grupujemy kobiety czy m�czy�ni , ktore zadanie wykonujemy 1-5, wojewodztwo 1 , wojewodztwo 2, rok, czy chcesz dane wczytac do bazy, czy zapisac w bazie]

Klasa "ZarzadzanieDanymi" przechowuje list� z danymi oraz informacje o ograniczeniu zbioru wzgl�dem p�ci. Zawiera funkcj� ograniczaj�c� zbi�r, oraz funkcje wczytuj�c� dane z pliku b�d� z bazy sqlite.
Demonstracja po��czenia z sqlite:

*Funkcja odcztu z bazy:
def CzytajSQLite():
    polaczenie = sqlite3.connect('mydb.db')
    polaczenie.row_factory = sqlite3.Row
    kursor = polaczenie.cursor()
    kursor.execute("""SELECT Terytorium, Przystapilo, Rok, Plec, Ilosc FROM dane""")
    dane = []
    G = kursor.fetchall()
    for x in G:
        row =[x['Terytorium'], x['Przystapilo'], x['Rok'], x['Plec'], x['Ilosc']]
        dane.append(row)
    polaczenie.close()
   return dane

*Funkcja zapisu do bazy: 
def ZapiszSQLite(dane):
    polaczenie = sqlite3.connect('mydb.db')
    polaczenie.row_factory = sqlite3.Row
    kursor = polaczenie.cursor()
    kursor.execute("DROP TABLE IF EXISTS dane;")
    kursor.execute(
        """CREATE TABLE dane(Terytorium varchar(50) NOT NULL, Przystapilo varchar(30) NOT NULL, Rok varchar(30) NOT NULL, Plec varchar(30) NOT NULL, Ilosc varchar(30) NOT NULL)""")
    kursor.executemany('INSERT INTO dane VALUES(?,?,?,?,?)', dane)
    polaczenie.commit()
    polaczenie.close()

