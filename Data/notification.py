import mysql.connector

def notification(name):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sajetsajet',
        database='process_scheduler'
    )
    
    myCursor = mydb.cursor()

    # Create a temporary table to store the result of the subquery
    myCursor.execute("CREATE TEMPORARY TABLE temp_table SELECT MAX(id) AS max_id FROM process WHERE name = %s", (name,))

    # Update the status using the temporary table
    myCursor.execute("UPDATE process SET status = 1 WHERE id IN (SELECT max_id FROM temp_table)")

    # Drop the temporary table
    myCursor.execute("DROP TEMPORARY TABLE IF EXISTS temp_table")

    mydb.commit()

    myCursor.close()
    mydb.close()

notification('T3')
