# import dependencies
import os
import sqlite3
import pandas as pd

# read the dataset in to panads
data_url = "https://github.com/matterholt/APP_CRUD-v1/blob/master/iris.csv"
headers = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
data_tabel = pd.read_csv(data_url, header=None, names=headers, converters={"zip": str})

# Cear example.bd if it exist
if os.path.exists("example.db"):
    os.remove("example.db")

# Create a database
conn = sqlite3.connect("example.db")

# add the data to our database
data_tabel.to_sql(
    "data_table",
    conn,
    dtype={
        "sepal_length": "VARCHAR(256)",
        "sepal_width": "VARCHAR(256)",
        "petal_length": "VARCHAR(256)",
        "petal_width": "VARCHAR(256)",
        "species": "VARCHAR(256)",
    },
)


"""
************************
Defining queries
SELECT, DELETE INSERT AND UPDATE queries
************************
"""

conn.row_factory = sqlite3.Row

# Make convenience functions for running SQL queries
#
# Select Query
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows


# Insert query
def sql_edit_insert(query, var):
    cur = conn.cursor()
    cur.execute(query, var)
    conn.commit()


# Delete Query
def sql_delete(query, var):
    cur = conn.cursor()
    cur.execute(query, var)


# Update Query
def sql_query2(query, var):
    cur = conn.cursor()
    cur.execute(query, var)
    rows = cur.fetchall()
    return rows
