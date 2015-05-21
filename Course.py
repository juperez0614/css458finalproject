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
    
    def openData(self):
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
        return courses
        #courses.append(Course(line.split("\t")))
        #print (line.split("\t")) 