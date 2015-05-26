def openData():
    data = open(os.getcwd() + '/courses.txt', 'r')
    individual_lines = data.readlines()
    cruncher = CourseCruncher()
    for line in individual_lines:
        course = Course(line.split("\t")) 
        cruncher.add(course)
    return cruncher 
