import time
import datetime

import schedule

def fun():
    print("Inside fun at :" , datetime.datetime.now())

def main():
    schedule.every(20).seconds.do(fun)
    fun()
    print("Inside Marvellous Automation Script at :",datetime.datetime.now())


if __name__ == "__main__":
    main()