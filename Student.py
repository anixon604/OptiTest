# Student Class
class Student(object):
    #define class to simulate a simple calculator
    def __init__ (self, id, age, level):
        #initialize properties
        self.studentID = id
        self.age = age
        self.abilityLevel = level
        self.testResults = []
