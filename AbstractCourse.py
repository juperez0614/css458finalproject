class AbstractCourse(object):
    def __init__(self, course):
        self.name = course.title
        self.ind_courses = [course]
    
    def add(self, course):
        self.ind_courses.append(course)
