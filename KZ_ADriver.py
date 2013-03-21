from Student import * #get classes Student
from Test import * #get classes Test
import random

#
class ADrive: 
# Create an array of students with varying ability levels
	def __init__(self,num_s):
		self.students = self.gen_students(num_s)    


	def gen_students(num_s):

		students = [0]*0
	
		for i in range(num_s):
			id = random.randint(1,10)
			age = random.randint(15,25)
			students[i] = Student(i, id,age, none)
			print(i)
		return students
			
	def get_student(self, stu_num):
		return students[stu_number + 1]



# Instantiate a TEST object with an array of Students



