# Student Class
import math
import sqlite3
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
    def probAnsFunc(self, qDifficulty):
        #utilizes self.abilityLevel to return Prob function of the brain
        # Rasch function Pr{ Xni = 1 } = (e^(Bn-qi))/(1+e^(Bn-qi))
        self.prSuccess = math.e ** (self.abilityLevel - qDifficulty) # numerator
        self.prSuccess = self.prSuccess / (1 + math.e ** (self.abilityLevel - qDifficulty)) # divide by denominator of function
        return self.prSuccess