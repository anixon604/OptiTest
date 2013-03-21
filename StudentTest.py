# Tester class for Student
from Student import * #get classes Student
myStudent = Student("bob",20,11) # create a student object
print(myStudent.name)
print(myStudent.age)
print(myStudent.abilityLevel)
probOfAnswer = myStudent.probAnsFunc(12)
print("myStudent will correctly answer with prob")
print(probOfAnswer)