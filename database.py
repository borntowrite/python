import sqlite3
from test2 import Employee

conn = sqlite3.connect("employ.db")
##conn = sqlite3.connect(":memory:") #this won't throw error since this will refresh everthing and start from scratch again
c = conn.cursor()
##c.execute("""create table python_db (
##                        first text,
##                        last text,
##                        pay integer
##                    )""")
##c.execute("""
##insert into python_db values ('Mary', 'Lee', 5000))
##""")
print("-------------------------------------------------")
emp_4 = Employee("Srinivas", "Rao", 40)
emp_5 = Employee("Aravind", "Sankaran", 30)
##print(emp_4)
##print(emp_5)

##c.execute("insert into python_db values (?,?,?)", (emp_4.first, emp_4.last, emp_4.pay))
##c.execute("insert into python_db values (:first, :last, :pay)", {'first': emp_5.first, 'last': emp_5.last, 'pay': emp_5.pay})
c.execute("select * from python_db")
print(c.fetchall())
c.execute("select * from python_db where last = :last", { 'last': 'Lee'})
print(c.fetchall())
c.execute("select * from python_db where last = ?", ('Rao',))
print(c.fetchall())

conn.commit()
conn.close()
 
