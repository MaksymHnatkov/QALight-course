import sqlite3

con = sqlite3.connect("CarSalesDB.db")
curs = con.cursor()

curs.execute("""CREATE TABLE cars
                  (id INTEGER PRIMARY KEY,
                  company TEXT, 
                  model TEXT, 
                  release_year INTEGER,
                  fuel_type TEXT,
                  FOREIGN KEY (release_year) REFERENCES taxes(year),
                  FOREIGN KEY (company) REFERENCES companies(name))""")

curs.execute("""CREATE TABLE companies
                  (id INTEGER PRIMARY KEY,
                  name TEXT,
                  country TEXT,
                  models_number INTEGER)
                  """)

curs.execute("""CREATE TABLE taxes 
                  (id INTEGER PRIMARY KEY,
                  year INTEGER,
                  tax FLOAT)
                  """)

curs.execute('INSERT INTO cars VALUES (1, "BMW", "323d", 1995, "diesel")')
curs.execute('INSERT INTO cars VALUES (2, "Audi", "A6", 1998, "diesel")')
curs.execute('INSERT INTO cars VALUES (3, "Opel", "Astra", 1993, "gasoline")')
curs.execute('INSERT INTO companies VALUES (1, "Audi", "Germany", 23)')
curs.execute('INSERT INTO companies VALUES (2, "BMW", "Germany", 46)')
curs.execute('INSERT INTO companies VALUES (3, "Opel", "Germany", 17)')
curs.execute('INSERT INTO taxes VALUES (1, 1991, 540.5)')
curs.execute('INSERT INTO taxes VALUES (2, 1992, 530.0)')
curs.execute('INSERT INTO taxes VALUES (3, 1993, 526.5)')
curs.execute('INSERT INTO taxes VALUES (4, 1994, 520.3)')
curs.execute('INSERT INTO taxes VALUES (6, 1995, 514.5)')
curs.execute('INSERT INTO taxes VALUES (7, 1996, 501.4)')
curs.execute('INSERT INTO taxes VALUES (8, 1997, 498.8)')
curs.execute('INSERT INTO taxes VALUES (9, 1998, 490.2)')
curs.execute('INSERT INTO taxes VALUES (10, 1999, 485.5)')

con.commit()

curs.close()
con.close()

