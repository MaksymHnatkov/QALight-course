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
                  models_amount INTEGER)
                  """)

curs.execute("""CREATE TABLE taxes 
                  (id INTEGER PRIMARY KEY,
                  year INTEGER,
                  tax FLOAT)
                  """)

curs.execute('INSERT INTO cars (company,model,release_year,fuel_type) VALUES ("BMW", "323d", 1995, "diesel")')
curs.execute('INSERT INTO cars (company,model,release_year,fuel_type) VALUES ("Audi", "A6", 1998, "diesel")')
curs.execute('INSERT INTO cars (company,model,release_year,fuel_type) VALUES ("Opel", "Astra", 1993, "gasoline")')
curs.execute('INSERT INTO companies (name,country,models_amount) VALUES ("Audi", "Germany", 23)')
curs.execute('INSERT INTO companies (name,country,models_amount) VALUES ("BMW", "Germany", 46)')
curs.execute('INSERT INTO companies (name,country,models_amount) VALUES ("Opel", "Germany", 17)')
curs.execute('INSERT INTO taxes (year,tax) VALUES (1991, 540.5)')
curs.execute('INSERT INTO taxes (year,tax) VALUES (1992, 530.0)')
curs.execute('INSERT INTO taxes (year,tax) VALUES (1993, 526.5)')
curs.execute('INSERT INTO taxes (year,tax) VALUES (1994, 520.3)')
curs.execute('INSERT INTO taxes (year,tax) VALUES (1995, 514.5)')
curs.execute('INSERT INTO taxes (year,tax) VALUES (1996, 501.4)')
curs.execute('INSERT INTO taxes (year,tax) VALUES (1997, 498.8)')
curs.execute('INSERT INTO taxes (year,tax) VALUES (1998, 490.2)')
curs.execute('INSERT INTO taxes (year,tax) VALUES (1999, 485.5)')

con.commit()

curs.close()
con.close()
