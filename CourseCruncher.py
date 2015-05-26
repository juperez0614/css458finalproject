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
                exp.remove(course)
                found_exp = True
        
    def print_abstract(self):
        for course in self.abstract_courses:
            print course.name
    
    def print_expertise(self):
        for exp in self.expertises:
            print exp.expertise
        
def openData():
    #data = open(os.getcwd() + '/courses.txt', 'r')
    data = open('/Users/Will/Downloads/courses.txt', 'r')
    individual_lines = data.readlines()
    cruncher = CourseCruncher()
    for line in individual_lines:
        course = Course(line.split(","))
        cruncher.add(course)
    return cruncher 
