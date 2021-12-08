from Student_class import Student
from Course_class import Course

def printInfo(student):

    print('Student Id',student.getStudentID())
    print('Student Name',student.getName())
    print('Student Grade',student.getGrade())
    print('Course Id',student.getCourse().getCourseId())
    print('Course Title',student.getCourse().getCourseTitle())
    print('Course Geade', student.getCourse().getCourseGrade())


def main():
    student = Student(1444,'Jack','Freshman','python','python30','A')
    printInfo(student)

    course = Course('JV202','Java 1','B+')
    student.setCourse(course)
    printInfo(student)

main()
