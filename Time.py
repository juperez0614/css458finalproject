"""The time object stores the following
    +- quarter
    +- day(s)
    +- start time
    +- end time
    
    I thought it was useful to include all of the these things because they are 
    all necessary for comparison and we want all the comparison to be done 
    within the time objects.
    
The compare to method is called 'has_conflict_with'.. refer to that method 
comment for more info"""

class Time(object):
    def __init__(self, day, time, quarter):
        """Pre: Day (string), time(String), quarter (String), pass these in 
        directly from the excel sheet"""
        self.quarter
        self.day = day
        self.time = self.generate_time(time)
        self.start = time[0]
        self.end = time[1]
     
           
    def generate_time(self, time):
        """This converts the string time into a start and end value"""
        start = 0
        end = 0
        split_dash = time.split("-")
        if len(split_dash) == 1:
            split_col = split_dash[0].split(":")  
            #print (int(split_col[0]))
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
            #print (split_col1)
            #print (split_col2)
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

        
    

