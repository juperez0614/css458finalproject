from Teacher import Teacher
from Course import Course
from Expertise import Expertise
import os

def TestAbstractCourse(abstractCourseString):
    pass

def TestCourse(courseString):
    print "Testing Course class..."
    
    courseStringTokens = courseString.split("\t")
    testCourse = Course(courseStringTokens)
    conflictCourse = Course(courseStringTokens)
    
    try:
        #assert testCourse.has_conflict_with(conflictCourse)
        pass
    except AssertionError:
        print "Conflict error"
        
    print "Test finished"
    
def TestExpertise():
    pass

def TestTeacher(teacherString):
    print "Testing Teacher class... "
    teacherStringTokens = teacherString.split("\t")
    testTeacher = Teacher(teacherStringTokens)
    
    try:
        assert testTeacher.name == teacherStringTokens[0]
    except AssertionError:
        print "Name error"
        
    try:
        if (testTeacher.fulltime):
            assert teacherStringTokens[1] == 'Y'
        else:
            assert teacherStringTokens[1] == 'N'
    except AssertionError:
        print "Fulltime error"
        
    try:
        assert testTeacher.classes == int(teacherStringTokens[2])
    except AssertionError:
        print "Classes error"
        
    try:
        assert testTeacher.stud_adv == int(teacherStringTokens[3])
    except AssertionError:
        print "Advisor error"
        
    try:
        assert (testTeacher.exp == teacherStringTokens[4:])
    except AssertionError:
        print "Expertise error"
        
    try:
        testTeacher.addClass(Course("332	1:15-5:15	F	90	Winter	Programming"))
    except:
        print "Add class error"
        
    print "Test finished"
    
TestCourse("332	1:15-5:15	F	90	Winter	Programming")
TestTeacher("Carnesale	Y	5	1	Programming	Software Engineering	Operating Systems")