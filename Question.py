import random
import numpy as np

##############
#            #
# Question   #
#            #
##############

# Question Object
# is in the form [_] where _ is the level chosen
# either at random between two indexes, lev_low and lev_high if they are specified
# else at random between 1 and 10 
class Question:

    num_feat = 1 # Question Features = level only for now
    
    # Must initialize a Question with (low_lev range, high_lev range)
    # Returns a question in the form [1,2,3,4,5,6,1,2,3,4,5,.....,2,3]
    # cooresponding to a list of 'Questions'
    def __init__(self, lev_low = None, lev_high= None):

        self.question = [0] * Question.num_feat
        self.question[0] = self.get_Level(lev_low, lev_high)
        
        ### NOT YET USED ####
        self.result = self.get_Result()
    
    # Return a Question Level between lev_low and lev_high
    # Input: low_lev; D:{x| 1 < x < high_lev}
    #        high_lev; D:{x| low_lev < x < 10}
    # Output: A random integer between lev_low and lev_high  
    def get_Level(self, lev_low, lev_high):
        
        if( (lev_high <= 10) and (lev_low >=0)):
            return random.randint(lev_low, lev_high)
            
        else:
            return random.randint(1,10)

############### HOW WE DETERMINE RESULT NEEDS TO BE DONE STILL ################
    def get_Result(self):
        return 0

# Iteration, String and Representation Functions
# Defined for testing (printing and iterating) purposes
    def __repr__(self):
        return ''.join(str(e) for e in self.question)
    
    def __iter__(self):
    	return self.question
    
    def __str__(self):
        return ''.join(str(e) for e in self.question)


        
        
        
        
    