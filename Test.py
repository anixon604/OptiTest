import numpy as np
from QuestionList import QuestionList

# Test Class
class Test:
    #num_q: Number of questions per student
    #qList: Standard question list (same for all students)
    #qListRasch: Dynamic question list that will be using the rasch model to optimize questions
    #results: Array of results per student
	#students: List of students to be tested
    num_q = 0
    qList = 0
    qListRasch = 0
    results = 0
    students = 0
	
    def __init__ (self, num_q, students):	    
        #getQList gets a standard QuestionList with num_q questions
        self.num_q = num_q
        self.students = students
        getQList(num_q)

	#Standard generate QuestionList function
    def getQList(self, num_q):
        qList = QuestionList(num_q,1,10)
	
    #generate QuestionList between min and max level function	
    def getQListBetween(self,num_q,min,max):
        qListRasch = QuestionList(num_q,min,max)
		
    def start(self):
        for i in range(len(students))
            testStudent(self.qList, self.students[i])
        print("Testing Successful")
    
    def testStudent(qList, student)
        return 0
    	
    def askQuestion(self):
        
        return 0
    def getResult(self):
	    return 0
newTest = Test()
raw_input("Test successful")
