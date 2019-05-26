import csv
import urllib.request
import io

# Import pliku z serwera (błąd)

def csv_import(url):
    url_open = urllib.request.urlopen(url)
    csvfile = csv.reader(io.TextIOWrapper(url_open, encoding='utf-8'), delimiter=';')
    return csvfile

def csv_import2(url):
    url_open = urllib.request.urlopen(url)
    csvfile = csv.reader(io.StringIO(url_open.read().decode('utf-8')), delimiter=';')
    return csvfile;

# Reading file
csvfile = csv_import('http://emilewa.cba.pl/csv/Zeszyt2.csv')

#csvreader = csv.reader(csvfile, delimiter=";")
#for row in csvreader:
#    print(row)
#import pandas as pd
#csv = pd.read_csv("http://emilewa.cba.pl/csv/Zeszyt1.csv")
#print
# csv.columns