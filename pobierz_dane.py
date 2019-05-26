import csv
import polacz_z_sqlite3

class ZarzadzanieDanymi:

    def __init__(self):
        self.plec = ''
        self.Dane = []

# Ogranicza zbiór do płci
    def KorM(self, plec):
        dane = []
        if plec == "k" or plec == "m":
            if plec=="k":
                plec="kobiety"
            elif plec=="m":
                plec="mężczyźni"

            for row in self.Dane:
                if row[2] == plec:
                    dane.append(row)
            self.Dane = dane
        return self.Dane

# Funkcja wczytuje dane z pliku csv do self.Dane
    def WczytajDane(self,dane_z):
        tak = 'tak'
        nie = 'nie'

        if dane_z==nie:
            Dane = []
            try:

                with open("Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv", "r") as csvfile:
                    csvreader = csv.reader(csvfile, delimiter=";")
                    for row in csvreader:
                        Dane.append(row)
            except:
                print("Błąd z plikiem")
            self.Dane = Dane
            #return Dane
        elif dane_z==tak:
            try:
                self.Dane = polacz_z_sqlite3.CzytajSQLite()
            except:
                print("Błąd baza sqlite")