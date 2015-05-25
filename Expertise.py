class Expertise(object):
    def __init__(self, expertise, course):
        self.expertise = expertise
        self.abstract_courses = [AbstractCourse(course)]
    
    def add(self, course):
        found_abstract = False
        for ab_course in self.abstract_courses:
                if ab_course.name == course.name and not found_abstract:
                    ab_course.add(course)
                    found_abstract = True
        if not found_abstract:
            self.abstract_courses.append(AbstractCourse(course))