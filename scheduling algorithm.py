"""This module will schedule teachers to classes. It reads text fule verisons of
the excel files provided by Prof Lin"""

import numpy as N
import numpy.random as R  
    
"""This defines a course object""" 
class Course(object):
    def __init__(self, vals, quarter):
        self.name = vals[0]
        self.time = self.time_fix(vals[1])
        self.days = str(vals[2])
        self.instructor = None
        self.cap = vals[3]
        self.quarter = quarter
    
    def time_fix(self, time):
        #- We will need to figure out the start and end time of the class is
        start = 0
        end = 0
        split_dash = time.split("-")
        if len(split_dash) == 1:
            split_col = split_dash[0].split(":")  
            #print (int(split_col[0]))
            if split_col[0] == "":
                start = 0.0
            else:
                start = int(split_col[0]) + int(split_col[1])/60.0
                end = start + 2.0
                if start < 8:
                    start = start + 12.0
                    end = end + 12.0
                elif end < start:
                    end = end + 12.0
        else:
            split_d1 = split_dash[0]
            split_d2 = split_dash[1]
            split_col1 = split_d1.split(":")
            split_col2 = split_d2.split(":")
            #print (split_col1)
            #print (split_col2)
            if split_col1[0] == "":
                start = 0.00
            elif len(split_col1) == 2:
                start = int(split_col1[0]) + float(split_col1[1])/60.0
            else:
                start = int(split_col1[0])  
            if split_col2[0] == "":
                end = 0.00 
            elif len(split_col2) == 2:
                end = int(split_col2[0]) +  float(split_col2[1])/60.0
            else:
                end = int(split_col2[0])
                if start < 8:
                    start = start + 12.0
                    end = end + 12.0
                elif end < start:
                    end = end + 12.0
        start = round(start, 2)
        end = round(end, 2)
        return [start, end]

"""This defines a teacher object"""
class Teacher(object):
    def __init__(self, vals):
        self.name = vals[0]
        if vals[1] == "Y":
            self.fulltime = True
        else:
            self.fulltime = False
        self.classes = float(vals[2])
        self.stud_adv = float(vals[3])
        self.exp = [] 
        self.exp.append(vals[4])
        self.exp.append(vals[5]) 
        self.exp.append(vals[6])
        self.totalexp = self.exp[0] + "," + self.exp[1] + "," + self.exp[2]
        self.satisfaction = 100
        
        self.summer = []
        self.fall = []
        self.winter = []
        self.spring = []
        self.courses = []
    def addClass(self, course):
        self.courses.append(course)
        self.classes = self.classes - 1
        
def check_exp(cname, teacher):
    if cname == '301' and "Writing" in teacher.totalexp:
        return True
    elif cname == '360' and "Software Engineering" in teacher.totalexp:
        return True
    elif cname == '430' and "Operating Systems" in teacher.totalexp:
        return True
    elif cname == '421' or cname == '422' or cname == '427' or cname == '428' and "Hardware" in teacher.totalexp:
        return True
    elif not (cname == '430' and cname == '301' and cname == '360' and cname == '421' and cname == '422' and cname == '427' and cname == '428'):
        return True
    else:
        return False
        

def run_schedule(): 
    courses = []
    data = open('/Users/Will/Desktop/courses7.txt', 'r')
    individual_lines = data.readlines()[8:]
    for line in individual_lines:
        array = N.array(line.split("\t")) 
        if len(array) >= 4 and not array[0] == "":
            courses.append(Course(array[0:4], 'Summer'))
        if len(array) >= 9 and not array[5] == "":
            courses.append(Course(array[5:9], 'Fall'))
        if len(array) >= 14 and not array[10] == "":
            courses.append(Course(array[10:14], 'Winter'))  
        if len(array) >= 17 and not array[15] == "":
            courses.append(Course(array[15:19], 'Spring'))
        #courses.append(Course(line.split("\t")))
        #print (line.split("\t")) 
    
    teachers = []
    data2 = open('/Users/Will/Desktop/faculty7.txt', 'r')
    individual_lines2 = data2.readlines()[4:]
    for line in individual_lines2:
        array = line.split("\t")
        teachers.append(Teacher(array))
    R.shuffle(teachers)
    #qs = [summer, fall, winter, spring]
    #R.shuffle(qs)
    R.shuffle(courses)   
       
    #-First round, everyone picks up to 4 classes
    for t in teachers:
        for i in range(0, 4):
            if t.classes >= 1 and len(courses) >= 1:
                t.courses.append(courses[0])
                t.classes -= 1
                courses.pop(0)
    #print len(courses)
            
    #- Second round, everyone pick another class
    for t in teachers:
        #t = teachers[i] 
        for num in range(0, 4):
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
    """for t in teachers:
        print t.name 
        for c in t.courses: 
            #print c.time
            #print c.days
            #print c.quarter
            print t.classes"""   
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
        """
print len(fall)
print len(summer)
print len(winter)
print len(spring)
"""
 
out = open('/Users/Will/Desktop/schedule.txt', 'w')
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