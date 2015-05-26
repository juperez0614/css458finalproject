from AbstractCourse import AbstractCourse


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
            if target_title in ab_course.name and not found_abstract:
                ab_course.remove(course)
