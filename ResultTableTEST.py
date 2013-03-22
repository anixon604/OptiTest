from ADriver import *
from ResultTable import *

student = (Student(1,1,1),Student(2,1,1))

createResultEntries(student, 2)

oneStudent = student[0]
updateCount(oneStudent, 2, 1)
updateCount(oneStudent, 2, 1)

print(getSuccessCountForLevel(oneStudent,1))
print(getSuccessCountForLevel(oneStudent,2))