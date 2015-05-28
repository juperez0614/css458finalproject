import numpy.random as R
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
    def add(self, course):
        self.courses.append(course)
        if 'Lab' in course.title:
            self.classes -= 0.5
        else:
            self.classes = self.classes - 1
    def yearly_sal(self):
        if self.fulltime:
            return 50000
        else:
            return 1000 * len(self.courses)

teachers = []
data2 = open('/Users/Will/Desktop/faculty7.txt', 'r')
individual_lines2 = data2.readlines()[4:]
for line in individual_lines2:
    array = line.split("\t")
    teachers.append(Teacher(array))

class Expertise(object):
    def __init__(self, expertise, course):
        self.expertise = expertise
        self.abstract_courses = [AbstractCourse(course)]
    
    def add(self, course):
        found_abstract = False
        for ab_course in self.abstract_courses:
                if ab_course.name in course.name and not found_abstract:
                    ab_course.add(course)
                    found_abstract = True
        if not found_abstract:
            self.abstract_courses.append(AbstractCourse(course))
    
    def remove(self, course):
        target_title = course.title
        found_abstract = False
        for ab_course in self.abstract_courses:
            if target_title in ab_course.name and ab_course.name in target_title and not found_abstract:
                ab_course.remove(course)




class Time(object):
    def __init__(self, day, time, quarter):
        """Pre: Day (string), time(String), quarter (String), pass these in 
        directly from the excel sheet"""
        self.quarter = quarter
        self.day = day
        self.time = self.generate_time(time)
        self.start = self.time[0]
        self.end = self.time[1]
     
           
    def generate_time(self, time):
        """This converts the string time into a start and end value"""
        start = 0
        end = 0
        split_dash = time.split("-")
        if len(split_dash) == 1:
            split_col = split_dash[0].split(":")  
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
        return [start, end]
    
    def has_conflict_with(self, other):
        """Pre : Another time object is passed
        
        Post : True is returned if there is no scheduling conflict with the 
        time of the course passed and the time of the course this method was 
        called on. Fale is returned otherwise"""
        if self.quarter == other.quarter and (self.day in other.day or other.day in self.day):
            if self.start > other.end or self.end < other.start:
                return True
            else:
                return False
        else:
            return True                 
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
        #print (values[2])
        #print (values[1])
        #print (values[4])
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
        """
        return self.time.has_conflict_with(other.time)
    
    def openData():
        data = open(os.getcwd() + '/courses.txt', 'r')
        individual_lines = data.readlines()
        cruncher = CourseCruncher()
        for line in individual_lines:
            course = Course(line.split("\t")) 
            cruncher.add(course)
        return cruncher
 
class CourseCruncher(object):
    def __init__(self):
        self.expertises = [] 
        self.abstract_courses = []
        self.courses = []
        self.expertise_types = []
    
    def add(self, course):
        if len(self.expertises) == 0:
            self.expertises.append(Expertise(course.expertise, course))
            self.expertise_types.append(course.expertise)
        found_expertise = False
        for expertise in self.expertises:
            if expertise.expertise == course.expertise and not found_expertise:
                expertise.add(course) 
                found_expertise = True
        if not found_expertise:
            self.expertises.append(Expertise(course.expertise, course))
            self.expertise_types.append(course.expertise)
        found_abstract = False
        for ab_course in self.abstract_courses:
                if ab_course.name in course.name and not found_abstract:
                    ab_course.add(course)
                    found_abstract = True
        if not found_abstract:
            self.abstract_courses.append(AbstractCourse(course))
        self.courses.append(course)
             
    def get_abstract_counts(self): 
        """Returns all counts of individual courses in abstract courses and 
        the names of the abstract courses as (counts, names)"""
        course_names = []
        counts = []
        for expertise in self.expertises:
            for ab_course in expertise.abstract_courses:
                course_names.append(ab_course.name)
                counts.append(len(ab_course.ind_courses))
        return counts, course_names
        
    def get_expertise(self, name):
        """Gives all individual (NOt Abstract) courses that have this expertise"""
        for expertise in self.expertises:
            if name in expertise.expertise:
                temp_courses = []
                for ab_course in expertise.abstract_courses:
                    for course in ab_course.ind_courses:
                        temp_courses.append(course)
                return temp_courses  
    
    def remove(self, course): 
        target_exp = course.expertise
        found_exp = False
        for exp in self.expertises:
            if target_exp in exp.expertise and not found_exp:
                #print ('I think ' + target_exp + ' is ' + exp.expertise)
                exp.remove(course)
                found_exp = True
        
    def print_abstract(self):
        for course in self.abstract_courses:
            print course.name
    
    def print_expertise(self):
        for exp in self.expertises:
            print exp.expertise 
            
    def get_quarter(self, quarter):
        temp_courses = []
        for expertise in self.expertises:
            for abstract_course in expertise.abstract_courses:
                for ind_course in abstract_course.ind_courses:
                    if quarter in ind_course.time.quarter:
                        temp_courses.append(ind_course)
        return temp_courses
        
    def get_sorted_by_quarter(self):
        quarters = []
        quarters.append(self.get_quarter("Summer"))
        quarters.append(self.get_quarter("Autumn"))
        quarters.append(self.get_quarter("Winter"))
        quarters.append(self.get_quarter("Spring"))
        return quarters                                                                                      

def openData():
    #data = open(os.getcwd() + '/courses.txt', 'r')
    data = open('/Users/Will/Desktop/courses2.txt', 'r')
    individual_lines = data.readlines()
    cruncher = CourseCruncher()
    for line in individual_lines:
        course = Course(line.split("\t")) 
        cruncher.add(course)
    return cruncher 

cruncher = openData()
"""for c in cruncher.courses:
    print c.title"""
summer = cruncher.get_quarter("Summer")
for course in summer:
    print course.title
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
                          
"""for t in teachers:
    print t.name  
    for c in t.courses:
        print c.name"""
