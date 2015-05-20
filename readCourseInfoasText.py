import numpy as N
import numpy.random as R
    
"""This defines a course object"""
class Course(object):
    def __init__(self, vals):
        self.name = vals[0]
        self.time = self.time_fix(vals[1])
        self.days = str(vals[2])
        self.instructor = None
        self.cap = vals[3]
    
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
                start = int(split_col1[0]) + int(split_col1[0])/60.0
            else:
                start = int(split_col1[0])  
            if split_col2[0] == "":
                end = 0.00 
            elif len(split_col2) == 2:
                end = int(split_col2[0]) +  int(split_col2[0])/60.0
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

             
    
fall = []
winter = []
spring = [] 
summer = []
data = open('/Users/Will/Desktop/courses7.txt', 'r')
individual_lines = data.readlines()[8:]
for line in individual_lines:
    array = N.array(line.split("\t")) 
    print len(array)
    if len(array) >= 4 and not array[0] == "":
        summer.append(Course(array[0:4]))
    if len(array) >= 9 and not array[5] == "":
        fall.append(Course(array[5:9]))
    if len(array) >= 14 and not array[10] == "":
        winter.append(Course(array[10:14])) 
    if len(array) >= 17 and not array[15] == "":
        spring.append(Course(array[15:19]))
    #courses.append(Course(line.split("\t")))
    #print (line.split("\t")) 
for course in fall:
    print course.time 

print len(summer)         
print (len(fall))
print len(winter)
print len(spring)