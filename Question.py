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
    
    # Question Features = level only for now
    num_feat = 1
    
    def __init__(self, lev_low = None, lev_high= None):
        
        # initialize list of length num_feat all to 0 (ie [0,0,0,0....0])
        self.question = [0] * Question.num_feat
        
        # assign a random level
        # only one feature (level) at question[0] for now
        self.question[0] = self.get_Level(lev_low, lev_high)
        print self.question[0]
    
        self.result = self.get_Result()
    
    def __repr__(self):
        return ''.join(str(e) for e in self.question)
    
    def __iter__(self):
    	return self.question
    
    def __str__(self):
        return ''.join(str(e) for e in self.question)
    
    def get_Level(self, lev_low, lev_high):
        if( (lev_high <= 10) and (lev_low >=0)):
            return random.randint(lev_low, lev_high)
            
        else:
            return random.randint(1,10)

############### HOW WE DETERMINE RESULT NEEDS TO BE DONE STILL (must ################
    def get_Result(self):
        return 0

        
        
        
        
    