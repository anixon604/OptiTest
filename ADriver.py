from Student import * #get classes Student
from Test import * #get classes Test

#

# Create an array of students with varying ability levels
def test_Drive_Baseline():
    
    # Create 30 students 
    stud_List = gen_studentList(30)

    # Test the students
    # Create a Test( num_q, list of students)
    test1 = Test(30, stud_List)
    print test1.getResult()


# generates a list of students of length len
def gen_studentList(length):

    student[0]*0

    for i in range(length):
        
        # Student ( ID, age, level)
        student[i] = Student(i, random.randint(10, 99),random.randint(1,10))

    return student 



# Instantiate a TEST object with an array of Students



