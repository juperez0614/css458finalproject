import os
#from CourseCruncher import CourseCruncher
from Expertise import Expertise
from Time import Time

"""This is the individual course object, ie: a specific course. It
stores the following
    +- title (509, 161, 162, 360, etc), string * 'L' is added to end
    if the course is a lab
    +- section (A, B etc) , string
    +- name = [title, section]
    +- expertise - string   
    +- time - a Time Object
    
*** When comparing time conflicts between courses YOU DO NOT have to
call any of the time object methods...You can instead call a method
of this class 'has_conflict_with' which takes another course object
as a parameter. In other words, the time objects are only used 
inside the Course Objects."""
class Course(object):
    def __init__(self, values):
        self.name = self.deconstruct_name(values[0])
        self.title = self.name[0]
        self.section = self.name[1]
        self.time = Time(values[2], values[1], values[4])
        self.capacity = values[3]
        self.expertise = values[5]
     
    def deconstruct_name(self, name):
        """Pre :  A name stirng read from the excel data is passed
        Post :  A list with [title, Section] is returned""" 
        if "205/40" in name:
            return [name, None]
        else:
            if len(name) == 3:
                return [name, None]
            elif len(name) == 4:
                return [name[0:3], name[3]]
            elif "SKL" in name:
                if len(name) == 7:
                    return [name[-4:-1] + "Lab", name[-1]]
                else:
                    return [name[-3:] + "Lab", None]
            elif "BCUSP" in name:
                if len(name)== 9:
                    return [name[-4:], None]
                else:
                    return [name[-5:-1], name[-1]]
            else:   
                return  [name[-5:-1], name[-1]] 


    def has_conflict_with(self, other):
        """Uses time objects to see if courses have time conflicts
        if there is a conflict true
        false if no conflict
        """
        return self.time.has_conflict_with(other.time)
    
"""def openData():
    data = open(os.getcwd() + '/courses.txt', 'r')
    individual_lines = data.readlines()
    cruncher = CourseCruncher()
    for line in individual_lines:
        course = Course(line.split("\t")) 
        cruncher.add(course)
    return cruncher"""
