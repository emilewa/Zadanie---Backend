import sqlite3

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





