import pobierz_dane

x = pobierz_dane.ZarzadzanieDanymi()
x.Dane = [["Pomorskie", "zdało", "mężczyźni", "2010", "9165"] , ["Pomorskie", "przystąpiło", "kobiety", "2010", "11798"]]
k = [x.Dane[1]]
m = [x.Dane[0]]
y = x.Dane


def test_KorM():
    assert x.KorM("m") == m
