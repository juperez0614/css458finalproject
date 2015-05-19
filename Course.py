"""This defines a course object"""
class Course(object):
    def __init__(self, vals):
        self.name = vals[0].value
        self.time = (vals[1].value)
        self.days = str(vals[2].value)
        self.instructor = None
        self.cap = vals[3].value