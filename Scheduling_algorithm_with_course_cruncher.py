import numpy as np
import CourseCruncher
import Teacher

    
def sim():
    cruncher = CourseCruncher.openData()
    teachers = Teacher.openData()
    for j in range(0, 4):
        '''max of two classes per quarter
            make a quarter list and traverse the list
            do a for loop twice for each quarter
        '''
        for teacher in teachers:
            possible_courses = cruncher.get_expertise(teacher.exp[0])
            quarters = cruncher.get_sorted_by_quarter(possible_courses)
            '''brings back list of actual courses [Expertise courses]
            need to split a subset by expertise
            '''
            R.shuffle(quarters[j]) 
            course_added = False
            for i in range(3):
                for course in quarters[j]:
                    if not course_added and not teacher.exp[i] == "": 
                        if len(teacher.courses) == 0:
                                teacher.add(course)
                                    #change teacher add to add to the correct quarter by adding argument for quarter

                                cruncher.remove(course)
                                course_added = True
                                break
                        else:
                            for teachers_course in teacher.courses:
                                if not course_added and not teachers_course.has_conflict_with(course):
                                    teacher.add(course)
                                    cruncher.remove(course)
                                    course_added = True
                                    break
    summerClassesLeft = len(quarters[0])
    autumnClassesLeft = len(quarters[1])
    fallClassesLeft = len(quarters[2])
    winterClassesLeft = len(quarters[3])
    print (summerClassesLeft, autumnClassesLeft, fallClassesLeft, winterClassesLeft)
        
for i in range (10): #years
    print("year: " ,i)
    sim()
    