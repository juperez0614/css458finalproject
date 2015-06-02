import numpy as np
import numpy.random as R
import CourseCruncher
import Course
import Teacher
from AbstractCourse import AbstractCourse

##################################################

baseFilePath = "E:/Github/css458finalproject"
yearsToRunSim = 10

##################################################

class simDriver(object):
    ssTeachersFull = []
    ssTeachersPart = []
    ssYrsSplitByQtrsClassesLeft = []
    ssYrsClassesLeft = []
    ssCost = []
    ssRevenue = []
    
    #electivetoCore = 1
    popStart = 30
    popgroRate = .1
    startDriver = None
    startcourses = []
    startteachers = []
    coursesByQuarter = []
    
    def __init__(self):
        self.startDriver = CourseCruncher.openData(baseFilePath)
        self.startcourses = self.startDriver.courses
        self.startteachers = Teacher.openData(baseFilePath)
        self.popStart = self.popStart * len(self.startcourses)
        
    def coursesByQuarterYear(self):
        self.coursesByQuarter.append(self.coursesByQuarterSingle("Summer"))
        #print(len(self.coursesByQuarterSingle("Summer")))
        self.coursesByQuarter.append(self.coursesByQuarterSingle("Autumn"))
        self.coursesByQuarter.append(self.coursesByQuarterSingle("Winter"))
        self.coursesByQuarter.append(self.coursesByQuarterSingle("Spring"))
        
    def coursesByQuarterSingle(self, quarter):
        quarterList = []
        for course in self.startcourses:
            if course.time.quarter == quarter:
                quarterList.append(course)
        return quarterList
         
    def checkExpertise(self, course, teacher):
        for expert in teacher.exp:
            print(expert, course.expertise)
            if expert == course.expertise:
                return True
        return False
    
    def conductPromotion(self):
        for teacher in self.startteachers:
            if teacher.fulltime == False:
                if teacher.coursesTaught > 12:
                    teacher.fulltime = True
                    teacher.classes 
    
    def findLessCourse(self):
        min = len(self.startDriver.abstract_courses[0].ind_courses)
        minName = self.startDriver.abstract_courses[0].name
        for abstract in self.startDriver.abstract_courses:
            if len(abstract.ind_courses) < min:
                min = len(abstract.ind_courses)
                minName = abstract.name
                minExp = abstract.ind_courses[0].expertise
        return minName, minExp
    
    
    def findQuarter(self):
        quarters = ["Summer","Autumn","Winter","Spring"]
        R.shuffle(quarters)
        return quarters[0] 
    
    def findDay(self):
        days = ["MW","TTh","F"]
        R.shuffle(days)
        return days[0]
    
    def findTimeSlot(self):
        times = ["8:00","10:00","12:00","2:00","4:00","6:00"]
        R.shuffle(times)
        return times[0]
    
    def addCourses(self):
        self.popStart = self.popStart + (self.popStart * 0.1)
        count = self.popStart/30 - len(self.startcourses)
        for i in range(int(count)):
            nameExp = self.findLessCourse()
            vals = []
            vals.append(nameExp[0]) #name
            vals.append(self.findTimeSlot())
            vals.append(self.findDay())
            vals.append(45)
            vals.append(self.findQuarter())
            vals.append(nameExp[1])
            course = Course.Course(vals)
            self.startDriver.add(course)
            self.startcourses.append(course)
      
    def sim(self):
        self.addCourses()    
        #reset beginnning of the year
        for teacher in self.startteachers:
            if teacher.fulltime == True:
                teacher.classes = 8
            else:
                teacher.classes = 4
            teacher.courses[:] = []
        print("amount of classes: ",len(self.startcourses))
        for course in self.startcourses:
            course.isAdded = False
            
        self.coursesByQuarterYear()
        #conduct increase according to year and population start and growth
        #seperate courses by quarter
        count = 0
        for teacher in self.startteachers:
            for quarter in self.coursesByQuarter:
                teacher.classQuarterCounter = 2
                R.shuffle(quarter)
                for course in quarter:
                    if course.isAdded == False:
                        count = count + 1
                        for expertise in teacher.exp:
                            if expertise in course.expertise and course.isAdded == False:
                                if teacher.classes > 0 and teacher.classQuarterCounter > 0:
                                    teacher.addClass(course)
                                    #print(teacher.name, course.name)
                                    course.isAdded = True
                                    quarter.remove(course)
                                    #print(len(quarter))
                                    break
        #print("round two...")                
        for teacher in self.startteachers:
            for quarter in self.coursesByQuarter:
                teacher.classQuarterCounter = 2
                R.shuffle(quarter)
                for course in quarter:
                    if course.isAdded == False:
                        count = count + 1
                        if course.isAdded == False:
                            if teacher.classes > 0 and teacher.classQuarterCounter > 0:
                                teacher.addClass(course)
                                #print(teacher.name, course.name)
                                course.isAdded = True
                                quarter.remove(course)
                                #print(len(quarter))
                                break
        
        self.ssYrsSplitByQtrsClassesLeft.append([len(self.coursesByQuarter[0]), len(self.coursesByQuarter[1]), len(self.coursesByQuarter[2]), len(self.coursesByQuarter[3])])
        sumOfClasses = len(self.coursesByQuarter[0]) + len(self.coursesByQuarter[1]) + len(self.coursesByQuarter[2]) + len(self.coursesByQuarter[3])
        self.ssYrsClassesLeft.append(sumOfClasses)
        
        
        for i in range (int(sumOfClasses/4)):
            vals = []
            vals.append( "Temp" + i.__str__())
            vals.append("Y")
            vals.append(4)
            vals.append(0)
            vals.append("")
            vals.append("")
            vals.append("")        
            self.startteachers.append(Teacher.Teacher(vals))
        
        for teacher in self.startteachers:
            for quarter in self.coursesByQuarter:
                teacher.classQuarterCounter = 2
                R.shuffle(quarter)
                for course in quarter:
                    if course.isAdded == False:
                        count = count + 1
                        if course.isAdded == False:
                            if teacher.classes > 0 and teacher.classQuarterCounter > 0:
                                teacher.addClass(course)
                                #print(teacher.name, course.name)
                                course.isAdded = True
                                quarter.remove(course)
                                #print(len(quarter))
                                break
        self.conductPromotion()
        fullTimeCount = 0
        partTimeCount = 0
        for teacher in self.startteachers:
            if teacher.fulltime == False:
                partTimeCount = partTimeCount + 1
            else:
                fullTimeCount = fullTimeCount + 1
        
        self.ssTeachersFull.append(fullTimeCount)
        self.ssTeachersPart.append(partTimeCount)
        moneyCost = 0
        
        for teacher in self.startteachers:
            moneyCost = moneyCost + teacher.yearly_sal()
        
        moneyRev = self.popStart * 15 * 358  #cost per credit
        
        self.ssCost.append(moneyCost)
        self.ssRevenue.append(moneyRev)
        

drive = simDriver()
for i in range(yearsToRunSim):            
    drive.sim()
    print (i)
    print("Cost: ", drive.ssCost[i])
    print("Profit: ", drive.ssRevenue[i] - drive.ssCost[i])
    print("FullTime ", drive.ssTeachersFull[i])
    print("PartTime ", drive.ssTeachersPart[i])
    print("Classes without teachers before new temps: ", drive.ssYrsClassesLeft[i])
    

    