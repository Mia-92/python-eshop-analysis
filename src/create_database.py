import sqlite3

conn = sqlite3.connect('training_database.sqlite')
cur = conn.cursor()
cur.execute('PRAGMA foreign_keys = ON;')

cur.executescript('''DROP TABLE IF EXISTS Polozky_objednavky;
                  DROP TABLE IF EXISTS Objednavky;
                  DROP TABLE IF EXISTS Produkty;
                  DROP TABLE IF EXISTS Customers;
                  DROP TABLE IF EXISTS Status_objednavky;
                  DROP TABLE IF EXISTS Kategorie;
                  DROP TABLE IF EXISTS Mesto;      
                ''')

cur.executescript('''CREATE TABLE Mesto (
                  id_mesto INTEGER PRIMARY KEY AUTOINCREMENT,
                  mesto TEXT NOT NULL);
                  
                  CREATE TABLE Kategorie (
                  id_kategorie INTEGER PRIMARY KEY AUTOINCREMENT,
                  kategorie TEXT NOT NULL);
                  
                  CREATE TABLE Status_objednavky (
                  id_status INTEGER PRIMARY KEY AUTOINCREMENT,
                  status TEXT NOT NULL);
                  
                  CREATE TABLE Customers (
                  id_zakaznika INTEGER PRIMARY KEY AUTOINCREMENT,
                  email TEXT UNIQUE NOT NULL,
                  id_mesto INTEGER,
                  jmeno TEXT NOT NULL,
                  prijmeni TEXT NOT NULL,
                  FOREIGN KEY (id_mesto) REFERENCES Mesto (id_mesto)
                  );

                  CREATE TABLE Produkty (
                  id_produkt INTEGER PRIMARY KEY AUTOINCREMENT,
                  nazev TEXT NOT NULL,
                  id_kategorie INTEGER,
                  nakupni_cena REAL NOT NULL,
                  doporucena_cena REAL NOT NULL,
                  FOREIGN KEY (id_kategorie) REFERENCES Kategorie (id_kategorie)
                  );

                  CREATE TABLE Objednavky (
                  id_objednavky INTEGER PRIMARY KEY AUTOINCREMENT,
                  id_zakaznika INTEGER,
                  id_status INTEGER,
                  datum_cas DATETIME NOT NULL,
                  FOREIGN KEY (id_zakaznika) REFERENCES Customers (id_zakaznika),
                  FOREIGN KEY (id_status) REFERENCES Status_objednavky (id_status)
                  );
                  
                  CREATE TABLE Polozky_objednavky (
                  id_polozky INTEGER PRIMARY KEY AUTOINCREMENT,
                  id_objednavky INTEGER NOT NULL,
                  id_produkt INTEGER,
                  mnozstvi INTEGER NOT NULL,
                  prodejni_cena REAL NOT NULL,
                  FOREIGN KEY (id_objednavky) REFERENCES Objednavky (id_objednavky),
                  FOREIGN KEY (id_produkt) REFERENCES Produkty (id_produkt)
                  )
                               
            ''')

conn.commit()