import sqlite3
conn = sqlite3.connect('company.db')
print("Connected")

conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES(1, 'Praise', 'Marvel', 21, 100000.04, 'Manager')");
conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES(1, 'Precious', 'Joy', 19, 85000.23, 'Treasurer')");
conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES(1, 'Paul', 'Wema', 20, 50000.44, 'Clerk')");
conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES(1, 'Sonia', 'Patience', 18, 31000.56, 'Secretary')");
conn.commit()
print("Successfully inserted values in Company1 table")