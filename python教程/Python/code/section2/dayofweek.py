import time
def dayOfWeek(DayNum=-1):
        days = ['Monday','Tuesday',
                'Wednesday','Thursday', 
                'Friday', 'Saturday', 'Sunday']
        if DayNum == -1:
            theTime = time.localtime(time.time())
            DayNum = theTime[6]
        return days[DayNum]
    	   
if __name__ == "__main__":
        print "Today is: %s" % dayOfWeek()
        print "The 3rd day is: %s" % dayOfWeek(2)
