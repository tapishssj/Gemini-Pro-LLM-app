import sqlite3

##connection 

connection=sqlite3.connect("employee.db")

##cursor object to insert, create, retrieve

cursor = connection.cursor()

table_info ="""

Create Table EMPLOYEE (NAME VARCHAR(25), DEPARTMENT VARCHAR(25), SALARY INT);


"""

cursor.execute(table_info)

##Insert records

cursor.execute('''INSERT into EMPLOYEE values('AA','OPS',50000)''')
cursor.execute('''INSERT into EMPLOYEE values('BB','DEV',90000)''')
cursor.execute('''INSERT into EMPLOYEE values('CC','TRL',40000)''')
cursor.execute('''INSERT into EMPLOYEE values('DD','IT',5000)''')
cursor.execute('''INSERT into EMPLOYEE values('EE','OPS',51000)''')
cursor.execute('''INSERT into EMPLOYEE values('FF','IT',80000)''')
cursor.execute('''INSERT into EMPLOYEE values('GG','TL',150000)''')

print("records are ")

data = cursor.execute('''SELECT * FROM EMPLOYEE''')

for row in data:
    print(row)


##Close the connection
    
    connection.commit()
    connection.close

