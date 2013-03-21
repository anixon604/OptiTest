# Student Class
class Student(object):
    #define class to simulate a simple calculator
    def __init__ (self, name, age, level):
        #initialize properties
        self.name = name
        self.age = age
        self.abilityLevel = level
        self.testResults = []
