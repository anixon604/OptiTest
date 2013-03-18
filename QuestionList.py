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
    num_q = 30
    
    def __init__(self):
         self.questions = self.get_Questions()
    # returns a question with all necessary
    # parameters (level)
    def get_Questions(self):
        
        
        # create 1D array size [0,0,0,...0] n = 30 feature initialized to zeros 
        questions = np.zeros(QuestionList.num_q)
        
        for i in range(QuestionList.num_q):
            questions[i]= Question()
    
        print questions

# Test run
listOfQ = QuestionList()

        
        
        
        
    