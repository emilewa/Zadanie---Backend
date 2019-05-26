
#Klasa odpowiadajaca za wywołanie odpowiedzniej funkcji wykonującej zadanie
class WykonajZadanie:
    def __init__(self,object,dowykonania): #dowykonania przechowuje dane wpisane przez użytkownika [czy grupowac , po kim grupujemy k/m , ktore zadanie wykonujemy 1-5, wojewodztwo 1 , wojewodztwo 2, rok, czy chcesz dane wczytac do bazy, czy zapisac w bazie ]
        self.dowykonania = dowykonania
        self.object = object

    def Wykonaj(self):
        if self.dowykonania[2] == "1":
            Zad1(self.object, self.dowykonania[3])
        elif self.dowykonania[2] == "2":
            Zad2(self.object, self.dowykonania[3])
        elif self.dowykonania[2] == "3":
            Zad3(self.object, self.dowykonania[5])
        elif self.dowykonania[2] == "4":
            Zad4(self.object)
        elif self.dowykonania[2] == "5":
            Zad5(self.object, self.dowykonania[3], self.dowykonania[4])
        else:
            print("Coś poszło nie tak :(")




lista_wojewodztw = ["Dolnośląskie", "Kujawsko-pomorskie", "Lubelskie", "Lubuskie", "Łódzkie", "Małopolskie",
                        "Mazowieckie", "Opolskie", "Podkarpackie", "Podlaskie", "Pomorskie", "Śląskie",
                        "Świętokrzyskie", "Warmińsko-Mazurskie", "Wielkopolskie", "Zachodniopomorskie"]



#1) obliczenie średniej liczby osób, które przystąpiły do egzaminu dla danego województwa w danym roku
def Zad1(object,wojewodztwo):
    przystapili = []
    for i in range(2010,2019):
        print(str(i)+" - "+str(SumaRok(object,wojewodztwo,"przystąpiło",i)))
        przystapili.append([i,SumaRok(object,wojewodztwo,"przystąpiło",i)])
    return przystapili


def SumaRok(Object,woj,przystapilo,rok):
    i=1
    ile=0
    for row in Object:
        if row[0]==woj and row[1]==przystapilo and row[3]==str(rok) :
            #print(row[4])
            ile += int(row[4])
            i = i +1
    return ile


def WspolczynnikZdawalnosci(object,wojewodztwo,rok):
    if SumaRok(object, wojewodztwo, "przystąpiło", rok) > 0:
        procent = SumaRok(object, wojewodztwo, "zdało", rok) / SumaRok(object, wojewodztwo, "przystąpiło", rok) * 100
        return procent
    else:
        return 0


#2) obliczenie procentowej zdawalności dla danego województwa na przestrzeni lat
def Zad2(object,wojewodztwo):
    r = []
    for rok in range(2010,2019):
        procent = WspolczynnikZdawalnosci(object,wojewodztwo,rok)
        #procent = SumaRok(object, wojewodztwo,"zdało" , i)/SumaRok(object,wojewodztwo,"przystąpiło",i)*100
        print(str(rok)+" - "+str(procent)+" %")
        r.append([rok,procent])
    return r


#3) podanie województwa o najlepszej zdawalności w konkretnym roku, np.rok - województwo A
def Zad3(object,rok):
    naj = 0
    z=0
    ktorewoj=""
    i=0
    for c in lista_wojewodztw:
        wojewodztwo = c
        ++z
        i = rok
        procent = WspolczynnikZdawalnosci(object,str(wojewodztwo),i)
        #procent = SumaRok(object, str(wojewodztwo), "zdało", i) / SumaRok(object, str(wojewodztwo), "przystąpiło", i) * 100
        if naj < procent:
            naj = procent
            ktorewoj = c
    print(str(rok)+" - "+ktorewoj)
    wynik = str(rok)+" - "+ktorewoj
    return wynik

#4) wykrycie województw, które zanotowały regresję (mniejszy współczynnik zdawalności w kolejnym roku), jeżeli takowe znajdują się w zbiorze, np.
def Zad4(object):
    z = 0
    ktora =0
    #lista_wojewodztw = ["Dolnośląskie", "Kujawsko-pomorskie", "Lubelskie", "Lubuskie", "Łódzkie", "Małopolskie", "Mazowieckie", "Opolskie", "Podkarpackie", "Podlaskie", "Pomorskie", "Śląskie","Świętokrzyskie", "Warmińsko-Mazurskie", "Wielkopolskie", "Zachodniopomorskie"]
    Regresja = []
    for i in range(2010, 2018):
        for z in range(0,len(lista_wojewodztw)):
            wojewodztwo = lista_wojewodztw[z]
            z = z+1
            i2 = i+1
            ktora = ktora+1
            if WspolczynnikZdawalnosci(object, str(wojewodztwo), i) - WspolczynnikZdawalnosci(object, str(wojewodztwo), i2) > 0:
                        Regresja.append("Wojewodztwo : "+wojewodztwo+": "+str(i)+" -> "+str(i2))

    for r in Regresja:
        print(r)
    return Regresja


#5) porównanie dwóch województw - dla podanych dwóch województw wypisanie, które z województw miało lepszą zdawalność w każdym dostępnym roku, np. przy porównaniu województwa A i B
def Zad5(object, woj1, woj2):
    wynik = []
    for i in range(2010, 2019):
       if WspolczynnikZdawalnosci(object, woj1, i) < WspolczynnikZdawalnosci(object, woj2, i):
            zm = str(i)+" - "+woj2
            print(zm)
            wynik.append(zm)
       elif WspolczynnikZdawalnosci(object, woj1, i) > WspolczynnikZdawalnosci(object, woj2, i):
            zm = str(i) + " - " + woj1
            print(zm)
            wynik.append(zm)
    return wynik
