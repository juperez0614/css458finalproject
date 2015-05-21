"""This module will schedule teachers to classes. It reads text file verisons of
the excel files provided by Prof Lin"""

import numpy as N
import numpy.random as R  
import os
import Course 
import Teacher 

"""checks if a instructor has the necessary credentials"""        
def check_exp(cname, teacher):
    if (cname == '301') and "Writing" in teacher.totalexp:
        return True
    elif (cname == '360') and "Software Engineering" in teacher.totalexp:
        return True
    elif (cname == '430') and "Operating Systems" in teacher.totalexp:
        return True
    elif (cname == '421' or cname == '422' or cname == '427' or cname == '428') and "Hardware" in teacher.totalexp:
        return True
    elif (cname == '450' or cname == '451' or cname == '455' or cname == '487'or cname == '552' or cname == '587') and "Graphics" in teacher.totalexp:
        return True
    elif not (cname == '430' or cname == '301' or cname == '360' or cname == '421' or cname == '422' or cname == '427' or cname == '428' or cname == '450' or cname == '451' or cname == '455' or cname == '487'and cname == '552' and cname == '587'):
        return True
    else:
        return False
        

def run_schedule(): 
    courses = []
    data = open(os.getcwd() + '/courses7.txt', 'r')
    individual_lines = data.readlines()[8:]
    for line in individual_lines:
        array = N.array(line.split("\t")) 
        if len(array) >= 4 and not array[0] == "":
            courses.append(Course.Course(array[0:4], 'Summer'))
        if len(array) >= 9 and not array[5] == "":
            courses.append(Course.Course(array[5:9], 'Fall'))
        if len(array) >= 14 and not array[10] == "":
            courses.append(Course.Course(array[10:14], 'Winter'))  
        if len(array) >= 17 and not array[15] == "":
            courses.append(Course.Course(array[15:19], 'Spring'))
        #courses.append(Course(line.split("\t")))
        #print (line.split("\t")) 
    
    teachers = []
    data2 = open(os.getcwd() +'/faculty7.txt', 'r')
    individual_lines2 = data2.readlines()[4:]
    for line in individual_lines2:
        array = line.split("\t")
        teachers.append(Teacher.Teacher(array))
    R.shuffle(teachers)
    #qs = [summer, fall, winter, spring]
    #R.shuffle(qs)
    R.shuffle(courses)   
       
    #-First round, everyone picks up to 4 classes
    for t in teachers:
        for i in range(0, 1):
            if t.classes >= 1 and len(courses) >= 1:
                t.courses.append(courses[0])
                t.classes -= 1
                courses.pop(0)
    #print len(courses)
            
    #- Second round, everyone pick another class
    for t in teachers:
        #t = teachers[i] 
        for num in range(0, 7):
            if len(courses) > 0 and t.classes >= 1:
                #- for each course in summer, compare its time to each time in the prof's classes
                i = 0
                added = False 
                while i < len(courses) and not added:
                    c = courses[i]
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
for t in teachers:   
    for c in t.courses:  
        if c.quarter == 'Summer':
            out.write(c.name + "\t" + str(c.time) + "\t" + c.days + "\t" + t.name + "\n")
for u in summer:
    out.write(c.name + "\t" + str(c.time) + "\t" + u.days + "\t" + "Unassigned" + "\n")
out.write("\n")
out.write('Fall Quarter \n')
for t in teachers: 
    for c in t.courses:
        if c.quarter == 'Fall':
            out.write(c.name + "\t" + str(c.time) + "\t" + c.days + "\t" + t.name + "\n")
for u in fall:  
    out.write(c.name + "\t" + str(c.time) + "\t" + u.days + "\t" + "Unassigned" + "\n")       
out.write("\n")
out.write('Winter Quarter \n')
for t in teachers: 
    for c in t.courses:
        if c.quarter == 'Winter':
            out.write(c.name + "\t" + str(c.time) + "\t" + c.days + "\t" + t.name + "\n")
for u in winter:
    out.write(c.name + "\t" + str(c.time) + "\t" + u.days + "\t" + "Unassigned" + "\n")    
out.write("\n")
out.write('Spring Quarter \n') 
for t in teachers:
    for c in t.courses:
        if c.quarter == 'Spring':
            out.write(c.name + "\t" + str(c.time) + "\t" + c.days + "\t" + t.name + "\n")
for u in spring:
    out.write(c.name + "\t" + str(c.time) + "\t" + u.days + "\t" + "Unassigned" + "\n")
             
out.close()  