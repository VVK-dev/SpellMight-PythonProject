import os
tutpath=os.path.join(os.path.dirname(__file__), "Tutorial.txt")
#Here, we get the directory in which this file is stored and then join it with "Tutorial.txt" to get the path of
#the tutorial text file. This has been done because the game modules will be stored in different files on different
#systems (this comment has been written using only # and not multi-line comments or docstrings as red stands out more
#than green).

def Tutorial():
    with open(tutpath,'r') as tut:
    #.strip() is used here to remove all trailing and leading whitespaces
        print((tut.readline()).strip())
        print(" ")
        print(input("Press Enter to continue..."))
        print(" ")
        for tutgps in range(2,11):
            print((tut.readline()).strip())
        print(" ")
        print(input("Press Enter to continue..."))
        print(" ")
        for tutgm1 in range(11,23):
            print((tut.readline()).strip())
        print(" ")
        print(input("Press Enter to continue..."))
        print(" ")
        for tutgm2 in range(23,43):
            print((tut.readline()).strip())
        print(" ")
        print(input("Press Enter to continue..."))
        print(" ")
        for tutend in range(43,46):
            print((tut.readline()).strip())
        print(" ")
        print(input("Press Enter to return to the Main Menu..."))
        return
