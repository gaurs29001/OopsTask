import mysql.connector as dbcon
import logger

lg = logger.logger()


def mysql_dbconnect():
    try:
        mydb = dbcon.connect(host="localhost", user="root", password="Root@2021")
        lg.logfile_info("Database Connection successful")
    except ConnectionError as ce:
        print(ce)
        lg.logfile_error(ce)
    else:
        return mydb


def mysql_select(query):
    try:
        in_db = mysql_dbconnect()
        cursor = in_db.cursor()
        cursor.execute(f"select count(*) from ({query}) as tb")
        count = cursor.fetchone()
        if count[0] > 0:
            cursor.execute(query)
            for i in cursor.fetchall():
                print(i)
                lg.logfile_info(i)
        else:
            print("No record fetched")
            lg.logfile_info("No record fetched")
    except Exception as dbe:
        print(dbe)
        lg.logfile_error(dbe)


def mysql_query_exec(query):
    try:
        in_db = mysql_dbconnect()
        cursor = in_db.cursor()
        cursor.execute(query)
        in_db.commit()
    except SyntaxError as se:
        print(se)
        lg.logfile_error(se)
    except dbcon.DatabaseError as de:
        print(de)
        lg.logfile_error(de)
    except dbcon.errors as dce:
        print(dce)
        lg.logfile_error(dce)
    else:
        lg.logfile_info("MySQL Query executed successfully")
