'''
****************************************************************************
*  Program  lessson_5.py                                                   *
*  Author   Baba                                                           *
*  Date     March 16, 2021                                                 *
*  Source   Realpython https://realpython.com/python-sql-libraries/#sqlite *
*  Description:                                                            *
*  This program is used to introduce Geniuses to using a                   *
*  database Structured Query Language (SQL).  The program                  *
*  imports the sqlite3 module which allows you to create                   *
*  and interact with an SQL Database                                       *
*                                                                          *
*  - The create_connection function is passed the                          *
*    path of the SQLite database file then it connects                     *
*    the app to an exixting SQLite3 database named hgp_pods                *
*    or if it;s not present it creates the database file                   *
*                                                                          *
*  - The execute_query function is passed the path and the                 *
*    query to implement; create_staff_member_table query and               *
*    add_staff_member query                                                *
*                                                                          *
*  - The execute_read function is passed the path and                      *
*    the display_staff_member query                                        *
****************************************************************************

'''

import sqlite3
from sqlite3 import Error

############### Function Definitions *******************
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


###################  Connect/Create to the Sqlite3 Database File *********************
connection = create_connection("oak8_pods.sqlite5")


##########################  Create Pod table variable query ################
create_Pod_member_table_query = """
CREATE TABLE IF NOT EXISTS Pod (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
##########################  Create leader table variable query ################
create_leader_pod_table_query = """
CREATE TABLE IF NOT EXISTS leader (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
#################### Executive query to create Pod table #################
execute_query(connection, create_Pod_member_table_query) 
#################### Executive query to create leader table #################
execute_query(connection, create_leader_pod_table_query) 

################# Create insert query to add Pod members to Pod table #######
add_Pod_members_query = """
INSERT INTO
  Pod (name,cell,position)
VALUES
  ('Maurice','510.424.7789','Pod Member'),
  ('Milan','510.816.3232', 'Pod Member'),
  ('Zyion','510.480.5785','Pod Member'),
  ('Hyab','510.612.3737','Pod Member');
"""
################# Create insert query to add pod leader to Pod table #######
add_leader_pod_query = """
INSERT INTO
  leader (name,cell,position)
VALUES
  ('Aris','510.229.6359','Pod Leader'),
  ('Richard','510.228.5623','Pod Leader'),
  ('Jacore','845.200.6250','Pod Leader'),
  ('Gabriel','510.326.5834','Pod Leader');
"""
####################  Execute insert Pod members query ##################
execute_query(connection, add_Pod_members_query)
####################  Execute insert leader pod query ##################
execute_query(connection, add_leader_pod_query)
########################### Display Pod_member Query ##################### 
display_Pod_query = "SELECT * from Pod"
Pod = execute_read_query(connection, display_Pod_query)

display_leader_query = "SELECT * from leader"
leader = execute_read_query(connection, display_leader_query)

for user in Pod:
  print(user)

execute_query(connection,'drop table Pod')



for user in leader:
  print(user)
execute_query(connection,'drop table leader')


