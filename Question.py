import random
import numpy as np

##############
#            #
# Question   #
#            #
##############
class Question:
    
    # Question Features = level only for now
    num_feat = 1
    
    def __init__(self, q_num):
        
        # initialize list of length num_feat to 0 
        self.question = [0] * Question.num_feat
        
        # assign a random level
        # only one feature (level) at question[0] for now
        self.question[0] = random.randint(1,10)
    
    def __repr__(self):
        return ''.join(str(e) for e in self.question)
    
    def __iter__(self):
    	return self.question
    
    def __str__(self):
        return ''.join(str(e) for e in self.question)

        
        
        
        
    