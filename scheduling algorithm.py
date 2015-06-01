"""This module will schedule teachers to classes. It reads text file verisons of
the excel files provided by Prof Lin"""

import numpy as N
import numpy.random as R  
import os
import CourseCruncher
import Course 
import Teacher 
import AbstractCourse


    #courses.append(Course(line.split("\t")))
    #print (line.split("\t")) 
teachers = Teacher.openData()
cruncher = CourseCruncher.openData()
print (cruncher)
"""for c in cruncher.courses:
    print c.title"""
summer = cruncher.get_quarter("Summer")
for course in summer:
    print (course.title)
"""softE = cruncher.get_expertise("Software Engineering")
for course in softE:
    print course.title"""

for i in range(0, 8):
    for teacher in teachers:
        possible_courses = cruncher.get_expertise(teacher.exp[0])
        R.shuffle(possible_courses)
        course_added = False
        for course in possible_courses:
            if not course_added:
                if len(teacher.courses) == 0:
                        teacher.add(course)
                        cruncher.remove(course)
                        course_added = True
                else:
                    for teachers_course in teacher.courses:
                        if not course_added and not teachers_course.has_conflict_with(course):
                            teacher.add(course)
                            cruncher.remove(course)
                            course_added = True
        if not course_added and not teacher.exp[1] == "":
            possible_courses = cruncher.get_expertise(teacher.exp[1])
            R.shuffle(possible_courses)
            for course in possible_courses:
                if len(teacher.courses) == 0:
                        teacher.add(course)
                        cruncher.remove(course)
                        course_added= True
                else:
                    for teachers_course in teacher.courses:
                        if not course_added and not teachers_course.has_conflict_with(course):
                            teacher.add(course)
                            cruncher.remove(course)
                            course_added = True
        if not course_added and not teacher.exp[2] == "":
            possible_courses = cruncher.get_expertise(teacher.exp[2])
            R.shuffle(possible_courses)
            for course in possible_courses:
                if len(teacher.courses) == 0:
                        teacher.add(course)
                        cruncher.remove(course)
                        course_added = True
                else:
                    for teachers_course in teacher.courses:
                        if not course_added and not teachers_course.has_conflict_with(course):
                            teacher.add(course)
                            cruncher.remove(course)
                            course_added = True
                          
for t in teachers:
    print (t.name)  
    for c in t.courses:
        print (c.name)

'''
Teachers Retiring/ quiting
Random population growth (1% - 20%) Normal Distribution
Teacher Class Rejection Rate (1% - 10%)
keeping timeslots together

def run_schedule(): 

    courses = []
    teachers = []
    courses = Course.openData()
    teachers = Teacher.openData()
    print("The number of course: ",len(courses.courses))
    print("The number of teachers: ",len(teachers))
    
    R.shuffle(teachers)
    #qs = [summer, fall, winter, spring]
    #R.shuffle(qs)
    R.shuffle(courses.courses)   
       
    #-First round, everyone picks up to 4 classes
    for t in teachers:
        for i in range(0, 1):
            if t.classes >= 1 and len(courses.courses) >= 1:
                t.courses.append(courses.courses[0])
                t.classes -= 1
                courses.courses.pop(0)
    #print len(courses)
            
    #- Second round, everyone pick another class
    for t in teachers:
        #t = teachers[i] 
        for num in range(0, 7):
            if len(courses.courses) > 0 and t.classes >= 1:
                #- for each course in summer, compare its time to each time in the prof's classes
                i = 0
                added = False 
                while i < len(courses.courses) and not added:
                    c = courses.courses[i]
                    ctime = c.time
                    cdays = c.days
                    cq = c.quarter
                    cname = c.name[0:3]
                    counter = 0
                    while counter < len(t.courses) and not added:
                        ttime = t.courses[counter].time
                        tdays = t.courses[counter].days
                        tq = t.courses[counter].quarter
                        goodtogo = check_exp(cname, t)
                        if goodtogo and (tdays == cdays and tq == cq and (ttime[0] > ctime[1] or ttime[1] < ctime[0])) or not tdays == cdays or not cq == tq:
                            added = True
                            t.courses.append(c)
                            courses.pop(i)
                            t.classes -= 1
                        counter += 1
                    i += 1   
    return [teachers, courses]  
data = run_schedule()
coursesFull = openCourseData()
teachersFull = openTeacherData()
courses = data[1]
teachers = data[0]
fall = []
summer = []
winter = []
spring = []    
for c in courses:
    if c.quarter == 'Fall':
        fall.append(c)
    elif c.quarter == 'Summer':
        summer.append(c)
    elif c.quarter == 'Winter':
        winter.append(c)
    else:
        spring.append(c)
 
"""Write schedule to text file which can be converted to excel""" 
out = open(os.getcwd() +'/schedule.txt', 'w')
out.write('Summer Quarter \n') 
count = 0;
for course in courses:
    count += 1
    #print (course.name , course.quarter)
countSummer = 0

"""for course in summer:
    countSummer +=1
    print (course.name, course.quarter)
print (count, countSummer)"""
print("Number of unassigned classes: ", len(courses))
print("Needed Full Time Employees: ", int(len(courses)/8))
print("Total Cost of Year: ", (int(len(courses)/8)) * 90000)
print("Total Projected Revenue of Year: ", int(len(coursesFull)) * 5 * 358.00 * 30) #2/3 class full of students
print ("Total Possible Profit: ", (int(len(coursesFull)) * 5 * 358.00 * 30) - ((int(len(courses)/8)) * 90000))


for t in teachers:   
    for c in t.courses:  
        if c.quarter == 'Summer':
            out.write(c.name + "\t" + str(c.time) + "\t" + c.days + "\t" + t.name + "\n")
for u in summer:
    out.write(u.name + "\t" + str(u.time) + "\t" + u.days + "\t" + "Unassigned" + "\n")
out.write("\n")
out.write('Fall Quarter \n')
for t in teachers: 
    for c in t.courses:
        if c.quarter == 'Fall':
            out.write(c.name + "\t" + str(c.time) + "\t" + c.days + "\t" + t.name + "\n")
for u in fall:  
    out.write(u.name + "\t" + str(u.time) + "\t" + u.days + "\t" + "Unassigned" + "\n")       
out.write("\n")
out.write('Winter Quarter \n')
for t in teachers: 
    for c in t.courses:
        if c.quarter == 'Winter':
            out.write(c.name + "\t" + str(c.time) + "\t" + c.days + "\t" + t.name + "\n")
for u in winter:
    out.write(u.name + "\t" + str(u.time) + "\t" + u.days + "\t" + "Unassigned" + "\n")    
out.write("\n")
out.write('Spring Quarter \n') 
for t in teachers:
    for c in t.courses:
        if c.quarter == 'Spring':
            out.write(c.name + "\t" + str(c.time) + "\t" + c.days + "\t" + t.name + "\n")
for u in spring:
    out.write(u.name + "\t" + str(u.time) + "\t" + u.days + "\t" + "Unassigned" + "\n")
             
out.close() 
''' 