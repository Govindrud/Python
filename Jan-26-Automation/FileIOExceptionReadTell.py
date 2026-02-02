def main():
    try:

        fobj = open("Hello.txt", "r")
        print("File gets Successfully opened")

        print("Current offset is  :", fobj.tell())

        Data = fobj.read(6)

        print("Data from file is :", Data)

        print("Current offset is  :", fobj.tell())

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application ")
        
    

if __name__ == "__main__":
    main()