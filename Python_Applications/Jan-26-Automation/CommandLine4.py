#python3 Commandline4.py 11 10 
import sys


def main():
    # No1 = int(sys.argv[1])
    # No2 = int(sys.argv[2])
    sum = 0
    print("Command Line Arguments are : ")
    for i in range(1,len(sys.argv)):
        sum = sum + int(sys.argv[i])
    #     No1 = int(sys.argv[1])
    #     No2 = int(sys.argv[2])     
    # print(No1 + No2)
    print(sum)


if __name__ == "__main__":
    main()

