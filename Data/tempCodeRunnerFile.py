        mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sajetsajet',
        database='process_scheduler'
        )
    
        myCursor = mydb.cursor()
        myCursor.execute("select * from process")