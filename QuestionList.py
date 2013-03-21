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

    # Must initialize a QuestionList with (num_q, low_lev range, high_lev range)
    # Returns a list in the form [1,2,3,4,5,6,1,2,3,4,5,.....,2,3]
    # cooresponding to a list of 'Questions' 
    def __init__(self, num_q, low_lev, high_lev):
        self.questions = self.get_Questions(num_q, low_lev, high_lev)
    
    # Return a list of Questions
    # Input: num_q; D:{x| 1 < x < ques_num}
    #        low_lev; D:{x| 1 < x < high_lev}
    #        high_lev; D:{x| low_lev < x < 10}
    # Output: A list of Question objects of the form [ Ques1, Ques2, Ques3 ]
    def get_Questions(self, num_q, low_lev, high_lev):
        
        questions = [0] * 0
        for i in range(num_q):
            questions.append(Question(low_lev, high_lev))
    
        #print questions
        return questions

    # Return a specific question level
    # Input: ques_number D:{x| 1 < x < ques_num} 
    # Output: integer question value 
    def get_Question(self, ques_number):
        return questions[ques_number + 1]

    # Return a the next question level
    # Input: ques_number D:{x| 1 < x < ques_num}
    # Output: next integer question value
    def get_NextQuestion(self, ques_number):
        return questions[ques_number + 2]

# Test run
#listOfQ = QuestionList(30,1,10)

        
        
        
        
    