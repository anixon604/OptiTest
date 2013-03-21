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
        self.getQList(num_q)

	#Standard generate QuestionList function
    def getQList(self, num_q):
        self.qList = QuestionList(num_q,1,10).questions
        print(self.qList)
	
    #generate QuestionList between min and max level function	
    def getQListBetween(self,num_q,min,max):
        self.qListRasch = QuestionList(num_q,min,max)
	
    #This function takes care of everything
    #It iterates through a list of students,
    #calling the testStudent function for each student	
    def start(self):
        for i in range(len(self.students)):
            self.testStudent(self.qList, self.students[i])
            print("Student #"+str(i)+":  ")
        print("Test Finished")
    
    def testStudent(self, qList, student):
        for i in range(len(self.qList)):
            self.askQuestion(student, qList[i])
        return 0
    def askQuestion(self, student, question):
        print("Student "+str(student)+"  answers Question level "+str(question))
    def getResult(self):
	    return 0
newTest = Test(20,[1,2,3,4,5,6,7,8,9,10])
newTest.start()
raw_input("Test successful")
