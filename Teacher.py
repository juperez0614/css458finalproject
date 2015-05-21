"""This defines a teacher object"""
import os

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
        
        
    def yearly_sal(self):
        if self.fulltime:
            return 50000
        else:
            return 1000 * len(courses)
    
    def openData():
        teachers = []
        data2 = open(os.getcwd() +'/faculty7.txt', 'r')
        individual_lines2 = data2.readlines()[4:]
        for line in individual_lines2:
            array = line.split("\t")
            teachers.append(Teacher.Teacher(array))
        return teachers
        
    