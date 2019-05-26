***Informacje o autorze***

Autor:			Emilia Lewandowska
Email:			emilka1611@gmail.com
Data utworzenia:	24.05.2019


***Opis projektu***

Aplikacja realizuj¹ca zadanie polegaj¹ce na analizie pliku z strony https://dane.gov.pl/dataset/1567/resource/17363 zawieraj¹cego dane dotyczace analizy zdawalnoœci matur w latach 2010-2018.
Program pozwala przeanalizowaæ zadany plik w celu wyœwietlenia danych zapytañ 1-5, na ekranie u¿ytkownika. 
Odczyt danych z pliku lokalnego o nazwie "Liczba_osób_które_przystapi³y_lub_zda³y_egzamin_maturalny.csv" lub z bazy danych sqllite. 
U¿ytkownik ma mo¿liwoœæ zapisania danych w bazie danych sqlite.

1) obliczenie œredniej liczby osób, które przyst¹pi³y do egzaminu dla danego województwa na przestrzeni lat, do podanego roku w³¹cznie, 
np.

2015 - 123456,


gdzie 123456 jest œredni¹ z lat (2010-2015)



2) obliczenie procentowej zdawalnoœci dla danego województwa na przestrzeni lat, 
np.


2010 - 50 %

2011 - 52 %

2012 - 57 %

itd. ...


3) podanie województwa o najlepszej zdawalnoœci w konkretnym roku, 
np.


rok - województwo A



4) wykrycie województw, które zanotowa³y regresjê (mniejszy wspó³czynnik zdawalnoœci w kolejnym roku), je¿eli takowe znajduj¹ siê w zbiorze, 
np.


województwo A: 2012 -> 2013

województwo B: 2017 -> 2018



5) porównanie dwóch województw - dla podanych dwóch województw wypisanie, które z województw mia³o lepsz¹ zdawalnoœæ w ka¿dym dostêpnym roku, 
np. przy porównaniu województwa A i B


2010 - A

2011 - B

2012 - B

2013 - A

itd. ...



***Wymagania techniczne i technologia wykorzystana***

- Python 3.7

- Do realizacji zadañ 1-5 ko¿ystano z funkcji dostêpnych w standardowej bibliotece

- Obs³uga po³¹czenia z baz¹ wyko¿ystuj¹c biblioteke sqlite3

Za³o¿enia:
- zak³adamy istnienie bazy dabych sqlite o nazwie mydb.db

Testowanie:
- testy pytest wybranych funkcji 
- aplikacja uruchamiana i testowana na urz¹dzeniu z systemem Microsoft Windows 10 Home, z wyko¿ystaniem œrodowiska PyCharm.


***Opis interfejsu***

Interfejs u¿ytkownika sk³ada siê z wyœwietlanych pytañ, u¿ytkownik zgodniez instrukcjami odpowiada na pytanie wpisuj¹c s³owo.

Pytania i dostêpne odpowiedzi:

Pytanie:	"Czy chcesz dane wczytaæ z bazy?"
Odpowiedzi:	"tak" (baza sqlite mydb.db tabela dane) / "nie" (lokalny plik).

Pytanie:	"Czy chcesz grupowaæ dane wed³ug p³ci?" 
Odpowiedzi:	"tak" / "nie"


Pytanie:	"Czy chcesz zapisaæ swoje dane w bazie sqlite?" 
Odpowiedzi:	"tak" / "nie"


Pytanie:	"Podaj numer polecenia z listy które chcesz wykonaæ:" 
Odpowiedzi:	'1' / '2' / '3' / '4' / '5'

Je¿eli zad1, zad2 oraz dwókrotnie dla zad5. 
Pytanie : 	"Podaj województwo:"
Odpowiedzi:	Nazwa województwa	

Je¿eli zad3
Pytanie:	"Podaj rok z przedzia³u 2010-2018:" 	
Odpowiedzi:	Liczba z przedzia³u 2010 - 2018
	

Pytanie:	"Co dalej?"	
Odpowiedzi:	T - Wykonaj nastêpn¹ analizê / N - Zakoñcz


Powy¿sze zapytania wykonywane s¹ cyklicznie jeœli u¿ytkonik zdecyduje siê na kontynuacje analiz.


***Opis funkcji, sposób wywo³ania i przyk³adowy kod.***

Aplikacja uruchamiana jest z pliku "plik_glowny.py".
Plik ten zawiera funkcjê main(), odpowiada za generowanie zapytania. 
Dane dotycz¹ce wybranych opcji przez u¿ytkownika przechowywane s¹ i przekazyane do poszczególnych funkcji, w liscie o nazwie "dowykonania".

Klasa "WykonajZadanie" otrzymuje listê z danymi na których wykonuje zadanie oraz listê "dowykonania". Dowykonania przechowuje dane wpisane przez u¿ytkownika, podczas wywo³ania funkcji z pliku interfejs. 
dowykonania = [czy grupowac , po kim grupujemy kobiety czy mê¿czyŸni , ktore zadanie wykonujemy 1-5, wojewodztwo 1 , wojewodztwo 2, rok, czy chcesz dane wczytac do bazy, czy zapisac w bazie]

Klasa "ZarzadzanieDanymi" przechowuje listê z danymi oraz informacje o ograniczeniu zbioru wzglêdem p³ci. Zawiera funkcjê ograniczaj¹c¹ zbiór, oraz funkcje wczytuj¹c¹ dane z pliku b¹dŸ z bazy sqlite.
Demonstracja po³¹czenia z sqlite:

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

