import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sajetsajet',
    database='trial1'
)

myCursor = mydb.cursor()

# db_insert = "insert into table1(name,address) values(%s,%s)"
# db_list=[('Sanjay','TN'),('Vishal','Bihar'),('Vivek','Bihar')]

# myCursor.executemany(db_insert,db_list)
# mydb.commit()
# print(myCursor.rowcount, "Record inserted! ")
# print("Table Created!!")

# --> Table creation <--
# myCursor.execute("CREATE TABLE process (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20), arrival_time int, burst_time int, priority int, execution_time int, completion_time int )")

# ans = myCursor.fetchall()
# for x in ans:
#     print(x)

n = int(input("Enter the number of tasks: "))
tasks_list = []

for i in range(0,n):
    name=input("Name: ")
    arrival_time=int(input("Arrival time: "))
    burst_time=int(input("Burst time: "))
    priority=int(input("Priority: "))
    execution_time=-1
    completion_time=-1
    task=(name, arrival_time, burst_time, priority, execution_time, completion_time)
    tasks_list.append(task)
    print("_____________")
    print()

# for x in tasks_list:
#     print(x)

db_insert = "insert into process(name,arrival_time,burst_time,priority,execution_time,completion_time) values(%s,%s,%s,%s,%s,%s)"
myCursor.executemany(db_insert,tasks_list)
mydb.commit()

myCursor.execute("select * from process")
for x in (myCursor.fetchall()):
    print(x)
    