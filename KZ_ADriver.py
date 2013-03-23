from Student import * #get classes Student
from Test import * #get classes Test
import random

#
class ADrive: 
# Create an array of students with varying ability levels
    def __init__(self,num_s):
        students = self.gen_students(num_s)
        newTest = Test(500, students)
        newTest.start()
        newTest.printResult()

    def gen_students(self, num_s):

        students = [0]*num_s
	
        for i in range(num_s):
            age = random.randint(15,25)
            level = random.randint(1,10)
            students[i] = Student(i, age, level)
			#print(i)
        return students
			
    def get_student(self, stu_num):
        return students[stu_num]

tester = ADrive(10)
raw_input(">>hit Enter")


# Instantiate a TEST object with an array of Students



