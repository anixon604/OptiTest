# Student Class
class Student(object):
    #define class to simulate a simple calculator
    def __init__ (self, name, age, level):
        #initialize properties
        self.name = name
        self.age = age
        self.abilityLevel = level
        self.testResults = []
    def getStundentLevel(self):
        #put AI here to return converge level of student based on tests
        return 0
    def probAnsFunc(self):
        #utilizes self.abilityLevel to return Prob function of the brain
        return 0