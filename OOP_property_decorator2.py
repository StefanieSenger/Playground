
# Using a property to (indirectly) access data in an object

class Student():

    def __init__(self, name, startingGrade=0):
        self.__name = name
        self.grade = startingGrade # Using the property to set the grade indirectly
        # self.__grade = startingGrade would set the attribute directly and
        # bypass the property setter method

    @property
    def grade(self):
        return self.__grade # self.__grade is defined by the property setter method

    @grade.setter
    def grade(self, newGrade): # called first time during __init__
        try:
            newGrade = int(newGrade)
        except (TypeError, ValueError) as e:
            raise type(e)('New grade: ' + str(newGrade) + ', is an invalid type.')
        if (newGrade < 0) or (newGrade > 100):
            raise ValueError('New grade: ' + str(newGrade) + ', must be between 0 and 100.')
        self.__grade = newGrade

student = Student('bla')
print(student.grade)
student.grade = 99
print(student.grade)
print()

# During __init__ python looks at both these __dict__ special methods
print(student.__dict__)
print(Student.__dict__) # finds that `grade` is a property
