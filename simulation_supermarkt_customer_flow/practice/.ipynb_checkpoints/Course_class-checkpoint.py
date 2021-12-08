
class Course():
    def __init__(self,courseId, courseTitle, courseGrade):
        self.courseId = courseId
        self.courseTitle = courseTitle
        self.courseGrade = courseGrade
        
    # setters 
    
    def setCourseId(self, courseId):
        self.courseId = courseId
    
    def setCourseTitle(self, courseTitle):
        self.courseTitle = courseTitle
        
    def setCourseGrade(self, courseGrade):
        self.courseGrade = courseGrade
    
    # getters
    def getCourseId(self):
        return self.courseId
    
    def getCourseTitle(self):
        return self.courseTitle
    
    def getCourseGrade(self):
        return self.courseGrade
    