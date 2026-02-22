import time
import datetime
import schedule

#import schedule


def fun():
    print("Inside fun at :" , datetime.datetime.now())

def gun():
    print("Inside gun at :" , datetime.datetime.now())

def main():
    #schedule.every(20).seconds.do(fun)
    schedule.every(1).minute.do(fun)
    schedule.every(1).hour.do(fun)
    
    while (True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()