import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sajetsajet',
    database='trial1'
)

myCursor = mydb.cursor()

task_names = ""
Tasks = {('T1',2,3,1),('T2',2,3,4),('T3',4,5,2)}

print(len(Tasks))