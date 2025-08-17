def create_database():
    import mysql.connector
    from mysql.connector import errorcode
    try:
        cnx = mysql.connector.connect(user='root', password='@Trevour256!',
                                      host='localhost',port ='3308')
        cursor = cnx.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        cursor.execute("USE alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
create_database()