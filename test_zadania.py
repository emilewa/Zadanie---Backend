import pobierz_dane
import zadania

x = pobierz_dane.ZarzadzanieDanymi()
x.Dane = [["Pomorskie", "zdało", "mężczyźni", "2010", "9165"], ["Pomorskie", "przystąpiło", "kobiety", "2010", "11798"]]
Q = [["Pomorskie", "zdało", "mężczyźni", "2010", "9165"], ["Pomorskie", "przystąpiło", "kobiety", "2010", "11798"], ["Lubelskie", "zdało", "mężczyźni", "2013", "99"], ["Lubelskie", "przystąpiło", "kobiety", "2013", "100"]]
k = x.Dane[0]
m = x.Dane[1]
y = x.Dane

#ok
def test_sumarok():
    assert zadania.SumaRok(y,"Pomorskie","zdało",2010) == 9165
    assert zadania.SumaRok(y,"Pomorskie","przystąpiło",2010) == 11798


#ok
wsp = (9165/11798)*100
wsp2 = (99/100)*100
def test_wspolczynnikZdawalnosci():
    assert zadania.WspolczynnikZdawalnosci(y,"Pomorskie",2010) == wsp
    assert zadania.WspolczynnikZdawalnosci(Q,"Lubelskie",2013) == wsp2

#ok
wynik = [[2010,11798], [2011,0], [2012,0], [2013,0], [2014,0], [2015,0], [2016,0], [2017,0], [2018,0]]
def test_Zad1():
    assert zadania.Zad1(y,"Pomorskie") == wynik


#ok
wynik2 = [[2010,wsp], [2011,0], [2012,0], [2013,0], [2014,0], [2015,0], [2016,0], [2017,0], [2018,0]]
def test_Zad2():
    assert zadania.Zad2(y,"Pomorskie") == wynik2


#ok
wynik3 = "2010 - Pomorskie"
wynikQ = "2013 - Lubelskie"
def test_Zad3():
   assert zadania.Zad3(y,2010) == wynik3
   assert zadania.Zad3(Q,2013) == wynikQ

#ok
zbior4 = [["Pomorskie", "zdało", "mężczyźni", "2010", "9165"], ["Pomorskie", "przystąpiło", "kobiety", "2010", "11798"],["Pomorskie", "zdało", "mężczyźni", "2011", "9165"], ["Pomorskie", "przystąpiło", "kobiety", "2011", "12000"]]
wynik4 = ["Wojewodztwo : Pomorskie: 2010 -> 2011", "Wojewodztwo : Pomorskie: 2011 -> 2012"]
def test_Zad4():
    assert zadania.Zad4(zbior4) == wynik4


#ok
zbior5 = [["Pomorskie", "zdało", "mężczyźni", "2010", "9165"], ["Pomorskie", "przystąpiło", "kobiety", "2010", "11798"],["Mazowieckie", "zdało", "mężczyźni", "2011", "9165"], ["Mazowieckie", "przystąpiło", "kobiety", "2011", "12000"]]
wynik5 = ["2010 - Pomorskie","2011 - Mazowieckie"]
wynikQ = ["2010 - Pomorskie","2013 - Lubelskie"]
def test_Zad5():
   assert zadania.Zad5(zbior5,"Pomorskie","Mazowieckie") == wynik5
   assert zadania.Zad5(Q,"Pomorskie","Lubelskie") == wynikQ