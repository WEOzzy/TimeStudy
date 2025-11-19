import sqlite3
from sqlite3 import Error
from datetime import datetime
import csv
import warnings
warnings.filterwarnings('ignore')

"""
connect to the da
"""

# create and maintain the database connection for frequent operations
# update this to take information from an external file for more flexability
def get_connection():
    database = 'TimeStudy.db'
    conn = sqlite3.connect(database)
    return conn

def fetch_plan_id(conn, plan_id):
    c = conn.cursor()
    # get the details of the plan id or create a new row for the plan id
    c.execute("SELECT * FROM AuditTimes WHERE PlanID = ?", (plan_id,))
    scan_times = c.fetchall()
    print(scan_times)
    if len(scan_times) == 0:
        print("Started time study for ", plan_id)
        c.execute("INSERT INTO AuditTimes (PlanID, StartTime) VALUES (?, ?)", (plan_id, datetime.now()))
        conn.commit()
    else:
        print("Need to pull the records and populate the GUI for updating")

def create_table(conn):
    """
    create a table if one does not exist, this is the base fields for what I am studying
    conditional logic should determine the fields in the gui based on the table making it
    independent of the table allowing to build a time study from a custom table and not
    require table creation
    :param conn:
    :return: conn
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS AuditTimes (
    PlanID text PRIMARY KEY NOT NULL,
    StartTime text,
    BootSelectionTime text,
    SoftthinksStartTime text,
    ImageSelectionTime text,
    DiagCompleteTime text,
    SysprepBootTime text,
    WinDriversDPKTime text,
    EndTime text
    );
    """
    # create the table
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("table created successfully")
    except Error as e:
        print("ERROR")
        print(e)
