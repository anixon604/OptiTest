# Utility file ResultTable.py

# import and create connections to database
import sqlite3


# create table entries for each student
# param: an array of Students, number of levels in test
# output: ex. (2 students, 3 levels)
# id1 | 1 | 0
# id1 | 2 | 0
# id1 | 3 | 0
# id2 | 1 | 0
# id2 | 2 | 0
# id2 | 3 | 0
#
def createResultEntries(students, levels):
    conn = sqlite3.connect("testResults.db") # or use :memory: to put it in RAM
    cursor = conn.cursor()
    # delete previous entries before initial creation
    cursor.execute("DROP TABLE IF EXISTS testResults")
    cursor.execute("CREATE TABLE testResults(studentID INT, level INT, numCorrect INT, total INT)")
    for i in students:
        for j in range(1,levels+1):
            # insert row for each Student/Level combination
            inValues = [(str(i.studentID),str(j))]
            cursor.executemany("INSERT INTO testResults VALUES(?,?,0,0)", inValues)

    # commit and close
    conn.commit()
    conn.close()

# updates counts on resultTable
# param: Student student, integer level, Bool correct
def updateCount(student, level, correct):
    conn = sqlite3.connect("testResults.db") # or use :memory: to put it in RAM
    cursor = conn.cursor()
    inValues = [str(student.studentID),str(level)] # place studentID and Level in list
    # select statement from list
    cursor.execute("SELECT * FROM testResults WHERE studentID =? AND level = ?", inValues)
    
    record = cursor.fetchone() # fetch first instance of result
    newCount = record[2] + correct # increment count on this result
    totCount = record[3] + 1
    inValues = [newCount,totCount,str(student.studentID),str(level)]
    # update row with new increment count
    cursor.execute("UPDATE testResults SET numCorrect= ? AND total= ? WHERE studentID = ? AND level = ?", inValues)
    
    # commit and close
    conn.commit()
    conn.close()

# get a count of correct responses by a student for a specified level
# param: Student student, integer level
# returns: integer count
def getSuccessCountForLevel(student,level):
    conn = sqlite3.connect("testResults.db") # or use :memory: to put it in RAM
    cursor = conn.cursor()
    inValues = [str(student.studentID),str(level)] # place studentID and Level in list
    # select statement from list
    cursor.execute("SELECT * FROM testResults WHERE studentID =? AND level = ?", inValues)
    record = cursor.fetchone() # fetch first instance of result
    return record[2]
