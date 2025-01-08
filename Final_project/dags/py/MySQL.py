import mysql.connector


def connect_cursor_mysql():
    cnx = mysql.connector.connect(user="user", password="password",
                                  host="mysql",
                                  database="db")
    return cnx


def create_staging():
    msql_conn = connect_cursor_mysql()
    with open("/opt/airflow/dags/sql/Staging.sql") as file:
        sql_query = file.read()
    cur = msql_conn.cursor()
    cur.execute(sql_query)
    cur.close()
    msql_conn.close()
