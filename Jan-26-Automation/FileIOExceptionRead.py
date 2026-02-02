def main():
    try:

        fobj = open("Hello.txt", "r")
        print("File gets Successfully opened")

        Data = fobj.read()

        print("Data from File is :", Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application ")
    

if __name__ == "__main__":
    main()