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
conn = sqlite3.connect('TimeStudy.db')


def fetch_plan_id(plan_id):
    c = conn.cursor()
    # get the details of the plan id or create a new row for the plan id
    pass