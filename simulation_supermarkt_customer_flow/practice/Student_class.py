from Course_class import Course

class Student:
    def __init__(self, sId, sName, sGrade, cID, cTitle,cGrade):
        self.StudentId = sId
        self.name = sName
        self.grade = sGrade
        self.course = Course(cID, cTitle,cGrade) 
        '''
        compose the course class here. In order to get the data from the class
        we need to create method
        '''  
    
    #setters to set data
    
    def setStudentId(self, studentId):
        self.studentId = studentId
    
    def setName(self, name):
        self.name = name
    
    def setGrade(self, grade):
        self.grade = grade

    # setter for course

    def setCourse(self,course):
        self.course = course

    #getters to get data
    
    def getStudentID(self):
        return self.StudentId
    
    def getName(self):
        return self.name

    def getGrade(self):
        return self.grade

    # getter for course

    def getCourse(self):
        return self.course