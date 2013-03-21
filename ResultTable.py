# Utility file ResultTable.py

# import and create connections to database
import sqlite3
conn = sqlite3.connect("testResults.db") # or use :memory: to put it in RAM
cursor = conn.cursor()

# create table entries for each student
# param: an array of Students, number of levels in test
def createResultEntries(students, levels):
    for i in students:
        for j in range(1,levels+1):
            cursor.execute("INSERT INTO testResults VALUES(%s, %s, 0)", (i.studentID,j))

# updates counts on resultTable
# param: Student student, integer level, Bool correct
def updateCount(student, level, correct):
    print(test)