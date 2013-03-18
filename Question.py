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
    
    def __init__(self):
        self.question = np.zeros(Question.num_feat)
        self.question = self.get_Features()

    def get_Features(self):
        
        #generate level as [level]
        self.question[0] = random.randint(1,10)
        
        
        
        
    