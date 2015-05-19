"""This defines a teacher object"""
class Teacher(object):
    def __init__(self, vals):
        self.name = vals[0].value
        self.fulltime = vals[1].value
        self.classes = vals[2].value
        self.stud_adv = vals[3].value
        self.exp = []
        self.exp.append(vals[4].value)
        self.exp.append(vals[5].value)
        self.exp.append(vals[6].value)
        self.satisfaction = 0
        self.courses = []
    def add_course(self, course):
        self.courses.append(course)
        self.classes = self.classes - 1
        
    