# import mysql.connector

# def insert_values(Tasks,n ):
#     '''
#         Takes an array of tasks from argument and inserts it into the process table
#     '''
#     print("Hello World")
#     mydb = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='sajetsajet',
#         database='process_scheduler'
#     )
#     myCursor = mydb.cursor()
#     print(Tasks)
#     print(n)
#     myCursor.executemany("insert into process (name, arrival_time, burst_time, priority, execution_time, completion_time) values (%s, %s, %s, %s, %s, %s,)", Tasks)
#     print(myCursor.rowcount, " was inserted")
    
import mysql.connector

def insert_values(Tasks, n):
    print("Hello World")
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sajetsajet',
        database='process_scheduler'
    )
    myCursor = mydb.cursor()
    print(Tasks)
    print(n)
    
    # Ensure 'Tasks' is a list of tuples where each tuple represents a row to be inserted
    query = "INSERT INTO process (name, arrival_time, burst_time, priority, execution_time, completion_time) VALUES (%s, %s, %s, %s, %s, %s)"
    
    myCursor.executemany(query, Tasks)
    
    mydb.commit()  # Commit the transaction
    print(myCursor.rowcount, "record(s) inserted.")

    myCursor.close()
    mydb.close()
