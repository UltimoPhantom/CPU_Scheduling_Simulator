import mysql.connector

def insert_values(self):
    '''
        Takes an array of tasks from argument and inserts it into the process table
    '''
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sajetsajet',
        database='process_scheduler'
    )
    