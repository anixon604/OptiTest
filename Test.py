import numpy as np
import random as rand
from QuestionList import QuestionList
import ResultTable as rt

# Test Class
class Test:
    #num_q: Number of questions per student
    #qList: Standard question list (same for all students)
    #qListRasch: Dynamic question list that will be using the rasch model to optimize questions
    #results: Array of results per student
	#students: List of students to be tested
    students = 0
    num_q = 0
    qList = 0
    qListRasch = 0
    results = []
	
    def __init__ (self, num_q, students):	    
        #getQList gets a standard QuestionList with num_q questions
        self.num_q = num_q
        self.students = students
        self.getQList(num_q)
        self.results = [0]*len(self.students)
        #rt.createResultEntries(self.students,10)
        for i in range(len(self.students)):
            self.results[i] = [0,0,0]
            self.results[i][0] = [0]*num_q
            self.results[i][1] = [0]*num_q

	#Standard generate QuestionList function
    def getQList(self, num_q):
        self.qList = QuestionList(num_q,1,10).questions
        #print(self.qList)
	
    #generate QuestionList between min and max level function	
    def getQListBetween(self,num_q,min,max):
        self.qListRasch = QuestionList(num_q,min,max)
	
    #This function takes care of everything. Just go TEST_INSTANCE_NAME.start() to start the testing process
    #It iterates through a list of students,
    #calling the testStudent function for each student	
    def start(self):
        for i in range(len(self.students)):
            self.results[i][2] = self.testStudent(self.qList, self.students[i], i)
        #print("Test Finished")
    def start_opt(self):
        for i in range(len(self.students)):
            self.results[i][2] = self.testStudent_opt(self.students[i], i)
    
	#This is a function to test ONE student with the given QuestionList
    def testStudent(self, qList, student, index):
        #prob = self.probDistribution(student)
        scoreSum = 0
        for i in range(len(self.qList)):
            scoreSum += self.askQuestion(student, qList[i].question[0], index)
        return scoreSum

    def testStudent_opt(self, student, index):
        self.setupTable(index, 5, 5)
        scoreSum = 0
		
        explore = 0.5
        greedy = 0.8
        exp_stage = int(explore*self.num_q)
		
        for i in range(self.num_q):
            cur_estimate = self.estimateLevel(index)
            question = int(rand.random() * 10)
            if i < exp_stage:
                scoreSum += self.askQuestion(student, question, index)
            else:
                exploit = rand.random()
                if exploit < greedy:
                    scoreSum += self.askQuestion(student, int(cur_estimate), index)
                else:
                    scoreSum += self.askQuestion(student, question, index)
            
			
			

        for i in range(exp_stage, self.num_q):
            cur_estimate = self.estimateLevel(index)
            question = int(rand.random() * 10)
        return scoreSum

    def setupTable(self, index, level, num_q):
        for i in range(10):
            self.results[index][0][i] = np.round(num_q*0.95/(1+np.exp((i+1)-level-1.3333)))
            self.results[index][1][i] = num_q

    #This is a function to test ONE student with ONE question from QuestionList
	#In this function, result is updated.
	#Whether the student gets it right or wrong depends on the random variable
	#corr compared against the probability distribution function of the given student.
    def askQuestion(self, student, question, index):
	    #Fermi-Dirac Distribution function
        prob = 0.95/(1+np.exp(question-student.abilityLevel-1.3333))
        corr = rand.random()
        score = 0
        if corr < prob:
            #print("Level "+str(question)+" | O")
            self.results[index][0][question-1] += 1
            score = 1
        self.results[index][1][question-1] += 1
        #rt.updateCount(student, question, score)
        #else:
            #print("Level "+str(question)+" | X")
        return score

	#Will return results for use
    def printResult(self):
        for i in range(len(self.students)):
            print("-----------------------------")
            print("STUDENT #"+str(i)+" |")
            print("-----------------------------")
            for j in range(10):
                print("Level "+str(j)+" || "+str(self.results[i][0][j])+" / "+str(self.results[i][1][j])+" | ")
            print("-----------------------------")
            print("   Score : "+str(self.results[i][2])+" / "+str(self.num_q))
            print("   Estimated Level : "+str(self.estimateLevel(i)))
            print("   Actual Level : "+str(self.students[i].abilityLevel))
            print("-----------------------------")
            print("  ")
            print("  ")

    def printBriefResult(self):
        print("------------------------------------------------")
        print("STUDENT\t| Level \t| Estimate\t| Error")
        print("------------------------------------------------")
        for i in range(len(self.students)):
            print("  "+str(i)+"\t| "+str(self.students[i].abilityLevel)+"\t\t| "+str(self.estimateLevel(i))+"\t\t| "+str(np.abs(self.students[i].abilityLevel - self.estimateLevel(i))))


    #Student abilityLevel diagnosis
    def estimateLevel(self,sindex):
        level = (self.results[sindex][0][0]*1)/self.results[sindex][1][0]
        level += (self.results[sindex][0][1]*2)/self.results[sindex][1][1]
        level += (self.results[sindex][0][2]*3)/self.results[sindex][1][2]
        level += (self.results[sindex][0][3]*4)/self.results[sindex][1][3]
        level += (self.results[sindex][0][4]*5)/self.results[sindex][1][4]
        level += (self.results[sindex][0][5]*6)/self.results[sindex][1][5]
        level += (self.results[sindex][0][6]*7)/self.results[sindex][1][6]
        level += (self.results[sindex][0][7]*8)/self.results[sindex][1][7]
        level += (self.results[sindex][0][8]*9)/self.results[sindex][1][8]
        level += (self.results[sindex][0][9]*10)/self.results[sindex][1][9]
        level = level*10/55 + 1.5
        return level

	
#newTest = Test(500,[1,2,3,4,5,6,7,8,9,10])
#newTest.start()
#newTest.printResult()
#raw_input("Test successful")
