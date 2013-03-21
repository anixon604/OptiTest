import random
import numpy as np
from Question import Question

##############
#            #
# List of    #
# Questions  # 
#            #
##############
class QuestionList:
    #Global/Class Vars for each instance
    # 30 Questions per Question List for now 
    
    #def __init__(self, num_q):
    #   self.questions = self.get_Questions(num_q, 1, 10)
    
    def __init__(self, num_q, low_lev, high_lev):
        self.questions = self.get_Questions(num_q, low_lev, high_lev)
    
    # returns a question with all necessary
    # parameters (level)
    def get_Questions(self, num_q, low_lev, high_lev):
        
        
        # create 1D array size [0,0,0,...0] n = 30 feature initialized to zeros 
        questions = np.zeros(num_q)
        
        for i in range(num_q):
            questions[i]= Question(low_lev, high_lev)
    
        print questions
        return questions 

            #def get_CalculatedQuestions(self):
            #return 0

    def get_Question(self, ques_number):
        return questions[ques_number + 1]

# Test run
listOfQ = QuestionList(30,1,10)

        
        
        
        
    