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
