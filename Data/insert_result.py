import mysql.connector

def insert_result(Tasks, tq):
    '''
        This function takes an array of tasks and time quantum and stores them to database.
        Stores to Process, Simulation table
    '''    
    
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sajetsajet',
        database='process_scheduler'
    )
    
    myCursor = mydb.cursor()
    
    # Ensure 'Tasks' is a list of tuples where each tuple represents a row to be inserted
    query = "INSERT INTO result (simulationID, processIDs, averageWaitingTime, averageTurnAroundTime) VALUES (%s, %s, %s, %s)"
    val = ()
    myCursor.executemany(query, Tasks)
    
    tasks_name = ""
    for i in Tasks:
            tasks_name = tasks_name + i[0] + ' '
            
    if tq == -1:
        algo_ID = 1
    else: 
        algo_ID = 2
    
    if tasks_name != "":
        query = "INSERT INTO simulation (algorithmID, TimeQuantum, Numberof_processes, SimulationTime, processIDs) VALUES (%s, %s, %s, %s, %s)"
        val = (algo_ID, tq, len(Tasks), -1, tasks_name)
        myCursor.execute(query,val)
        
        mydb.commit()  # Commit the transaction
        print(myCursor.rowcount, "record(s) inserted.")
    
    myCursor.execute("select * from process")
    myCursor.execute("select * from simulation")

    myCursor.close()
    mydb.close()




def trial():
    
        mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sajetsajet',
        database='process_scheduler'
        )
    
        myCursor = mydb.cursor()
        myCursor.execute("select max(simulationID) from simulation")
        max_simulation_id = myCursor.fetchone()[0]
        print(max_simulation_id)
        
trial()