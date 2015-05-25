class CourseCruncher(object):
    def __init__(self):
        self.expertises = [] 
        self.abstract_courses = []
        self.courses = []
    
    def add(self, course):
        if len(self.expertises) == 0:
            self.expertises.append(Expertise(course.expertise, course))
        found_expertise = False
        for expertise in self.expertises:
            if expertise.expertise == course.expertise and not found_expertise:
                expertise.add(course)
        if not found_expertise:
            self.expertises.append(Expertise(course.expertise, course))
        found_abstract = False
        for ab_course in self.abstract_courses:
                if ab_course.name == course.name and not found_abstract:
                    ab_course.add(course)
                    found_abstract = True
        if not found_abstract:
            self.abstract_courses.append(AbstractCourse(course))
        self.courses.append(course)
             
    def get_abstract(self): 
        return self.abstract_courses
    
    def get_expertise(self):
        return self.expertise
        
    def print_abstract(self):
        for course in self.abstract_courses:
            print course.name
    
    def print_expertise(self):
        for exp in self.expertises:
            print exp.expertise
