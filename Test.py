import numpy as np
import random as rand
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
	
    #This function takes care of everything. Just go TEST_INSTANCE_NAME.start() to start the testing process
    #It iterates through a list of students,
    #calling the testStudent function for each student	
    def start(self):
        for i in range(len(self.students)):
            self.testStudent(self.qList, self.students[i])
            print("Student #"+str(i)+":  ")
        print("Test Finished")
    
	#This is a function to test ONE student with the given QuestionList
    def testStudent(self, qList, student):
        prob = self.probDistribution(student)
        print prob
        for i in range(len(self.qList)):
            self.askQuestion(student, prob, qList[i])

    #This is a function to test ONE student with ONE question from QuestionList
	#In this function, result is updated.
	#Whether the student gets it right or wrong depends on the random variable
	#corr compared against the probability distribution function of the given student.
    def askQuestion(self, student, prob, question):
        corr = rand.random()
        if corr < prob[question.question[0]-1]:
            print("Student "+str(student)+"  answers Question level "+str(question)+" and is CORRECT")
        else:
            print("Student "+str(student)+"  answers Question level "+str(question)+" and is WRONG")

	#Will return results for use
    def getResult(self):
	    return 0
    
	#function to generate a probability distribution function
    def probDistribution(self,level):
        prob0 = 1
        prob = np.zeros(10)
        for i in range(level):
            prob[i] = 1
        for i in range(level,10):
            prob[i] = prob0 - 0.1
            prob0 = prob0 - 0.1
        return prob
	
newTest = Test(20,[1,2,3,4,5,6,7,8,9,10])
newTest.start()
raw_input("Test successful")
