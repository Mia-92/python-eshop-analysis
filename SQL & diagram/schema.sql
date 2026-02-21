BEGIN TRANSACTION;
DROP TABLE IF EXISTS "Customers";
CREATE TABLE Customers (
                  id_zakaznika INTEGER PRIMARY KEY AUTOINCREMENT,
                  email TEXT UNIQUE NOT NULL,
                  id_mesto INTEGER,
                  jmeno TEXT NOT NULL,
                  prijmeni TEXT NOT NULL,
                  FOREIGN KEY (id_mesto) REFERENCES Mesto (id_mesto)
                  );
DROP TABLE IF EXISTS "Kategorie";
CREATE TABLE Kategorie (
                  id_kategorie INTEGER PRIMARY KEY AUTOINCREMENT,
                  kategorie TEXT NOT NULL);
DROP TABLE IF EXISTS "Mesto";
CREATE TABLE Mesto (
                  id_mesto INTEGER PRIMARY KEY AUTOINCREMENT,
                  mesto TEXT NOT NULL);
DROP TABLE IF EXISTS "Objednavky";
CREATE TABLE Objednavky (
                  id_objednavky INTEGER PRIMARY KEY AUTOINCREMENT,
                  id_zakaznika INTEGER,
                  id_status INTEGER,
                  datum_cas DATETIME NOT NULL,
                  FOREIGN KEY (id_zakaznika) REFERENCES Customers (id_zakaznika),
                  FOREIGN KEY (id_status) REFERENCES Status_objednavky (id_status)
                  );
DROP TABLE IF EXISTS "Polozky_objednavky";
CREATE TABLE Polozky_objednavky (
                  id_polozky INTEGER PRIMARY KEY AUTOINCREMENT,
                  id_objednavky INTEGER NOT NULL,
                  id_produkt INTEGER,
                  mnozstvi INTEGER NOT NULL,
                  prodejni_cena REAL NOT NULL,
                  FOREIGN KEY (id_objednavky) REFERENCES Objednavky (id_objednavky),
                  FOREIGN KEY (id_produkt) REFERENCES Produkty (id_produkt)
                  );
DROP TABLE IF EXISTS "Produkty";
CREATE TABLE Produkty (
                  id_produkt INTEGER PRIMARY KEY AUTOINCREMENT,
                  nazev TEXT NOT NULL,
                  id_kategorie INTEGER,
                  nakupni_cena REAL NOT NULL,
                  doporucena_cena REAL NOT NULL,
                  FOREIGN KEY (id_kategorie) REFERENCES Kategorie (id_kategorie)
                  );
DROP TABLE IF EXISTS "Status_objednavky";
CREATE TABLE Status_objednavky (
                  id_status INTEGER PRIMARY KEY AUTOINCREMENT,
                  status TEXT NOT NULL);
COMMIT;
