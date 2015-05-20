def sim(courses, teachers):
    core = []
    electives = []
    isBooked = False
    for course in courses:
        if course.elecCore == True:
            core.append(course)
        else:
            electives.append(course)
    
    counter = 0
    while (len(core) > 0):
        for course in core:
            for teacher in teachers:
                for i in range(3):
                    if teacher.expertise[i] == course.expertise:
                        isBooked = False
                        for schCourse in teacher.schedule:
                            if schCourse.timeOfday == course.timeOfday:
                                isBooked = True;
                        if(isBooked == False):
                            teacher.schedule.append(course)
                            core.remove(course)
                            teacher.numOfHours = teacher.numOfHours - course.numOfHours 
    
    while (len(electives) > 0):
        for course in electives:
            for teacher in teachers:
                for i in range(3):
                    if teacher.expertise[i] == course.expertise:
                        isBooked = False
                        for schCourse in teacher.schedule:
                            if schCourse.timeOfday == course.timeOfday:
                                isBooked = True;
                        if(isBooked == False):
                            teacher.schedule.append(course)
                            electives.remove(course)
                            teacher.numOfHours = teacher.numOfHours - course.numOfHours 