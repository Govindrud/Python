#python3 Commandline4.py 11 10 
import sys


def main():

    if(len(sys.argv) < 3  or len(sys.argv) > 3):
        print("Invalid Number of Argument ")

    else:
        No1 = int(sys.argv[1])
        No2 = int(sys.argv[2])
        print(No1 + No2)

if __name__ == "__main__":
    main()

#py.pi.org = Module information