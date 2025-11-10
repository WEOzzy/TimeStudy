import sqlite3
from sqlite3 import Error
from datetime import datetime
import csv
import warnings
warnings.filterwarnings('ignore')

def main():
    print("Connecting to database")
    database ='TimeStudy.db'
    conn = sql_main(database)
    plan_id = ""
    while plan_id != "quit":
        plan_id = input("Enter PlanID, type quit to stop: ")
        if plan_id != "quit":
            update_times(conn, plan_id)
    # need to write the table to a csvfile upon quitting, could make it prettier but meh
    if plan_id == "quit":
        export_list = export_times(conn)
        filename = "TimeStudy.csv"
        with open(filename, 'w', newline='') as csvfile:
            for line in export_list:
                write_line = csv.writer(csvfile, quotechar='"')
                write_line.writerow(line_item for line_item in line)


def update_times(conn, plan_id):
    c = conn.cursor()
    #this is probably a bad way to do this but its quick
    # limited to only one entry per planid, create the row if first scan, update end time if second scan
    c.execute("SELECT * FROM AuditTimes WHERE PlanID = ?", (plan_id,))
    entry = c.fetchall()
    if len(entry) == 0:
        c.execute("INSERT INTO AuditTimes (PlanID, StartTime) VALUES (?, ?)", (plan_id, datetime.now()))
        conn.commit()
        print("Audit started")
    else:
        c.execute("UPDATE AuditTimes SET EndTime = ? WHERE PlanID = ?", (datetime.now(), plan_id))
        conn.commit()
        print("Audit ended")


def export_times(conn):
    c = conn.cursor()
    #this could be made to only do one day but I am lazy
    c.execute("SELECT * FROM AuditTimes")
    export_list = c.fetchall()
    return export_list

def sql_main(database):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS AuditTimes (
    PlanID text PRIMARY KEY NOT NULL,
    StartTime text,
    EndTime text
    );
    """

    # connect to the database
    conn = create_connection(database)
    if conn is not None:
        # create the table
        create_table(conn, create_table_sql)
    else:
        print("Could not create database connection.")

    return conn


def create_connection(time_study_db):
    """
    Create a database connection ot a sqlite database specified by time_study_db
    :param time_study_db:
    :return: connection object or None
    """
    try:
        conn = sqlite3.connect(time_study_db)
        return conn
    except Error as e:
        print(e)
    return None


def create_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)


if __name__ == '__main__':
    main()