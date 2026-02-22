import time
import datetime

import schedules


def fun():
    print("Inside fun at :" , datetime.datetime.now())

def main():
    schedules.every(20).seconds.do(fun)
    while (True):
        schedules.run_pending()
        time.sleep(1)
    


if __name__ == "__main__":
    main()