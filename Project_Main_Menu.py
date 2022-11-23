#Main Menu
import Project_Setup
print("Loading...")
import os
import Project_Cards
import Project_Cards_Modify
import Project_Match
import Project_Tutorial
import sys

def MENU():
    try:
        while True:
            print("\n===================================================WELCOME TO SPELLMIGHT=============================================") 
            print(" 1. PLAY A MATCH ")
            print(" 2. TUTORIAL ")
            print(" 3. VIEW THE CARDS ")
            print(" 4. CARD MODIFICATION ")
            print(" 5. MANUAL SETUP")
            print(" 6. QUIT ")
            Choice=input("Enter your choice [1/2/3/4/5/6] : ")
            if Choice=='5':
                print("\nWARNING:THIS WILL RESET ALL CHANGES MADE TO ANY CARDS AND RETURN THEM TO THEIR DEFAULT STATE.")
                option=input("DO YOU STILL WANT TO PROCEED? ")
                if option.lower()=="yes" or option.lower()=="y":
                    print("Setting up...")
                    Project_Setup.createdb()
                    Project_Setup.insert()
                    Project_Setup.setup()
                    print("Setup complete!")
                else:
                    continue
            elif Choice=='6':
                option=input("ARE YOU SURE YOU WANT TO QUIT? ")
                if option.lower()=="y" or option.lower()=="yes":
                    sys.exit()
                else:
                    print("Returning to the Main Menu...")
                    pass
            else:
                check=0
                checkpath=os.path.join(os.path.dirname(__file__), "DONOTDELETE.txt")
                #checkpath is the result of joining the directory of this file, i.e. the Main Menu file,
                #and the name of the text file required for proper functioning of the program, DONOTDELETE.txt 
                try:
                    with open("DONOTDELETE.txt",'w') as f:
                        check=1
                except FileNotFoundError:
                    print("\nPlease setup the program by choosing option 5.")
                if check==1:
                    if Choice=='1':        
                        print("")
                        Project_Match.Match()
                    elif Choice=='2':
                        print("")
                        Project_Tutorial.Tutorial()
                    elif Choice=='3':
                        print("")
                        Project_Cards.View_Cards()
                        input("\nPlease press enter to return to the Main Menu\n")
                    elif Choice=='4':
                        Project_Cards_Modify.Cards_Menu()
                    else:
                        print("INVALID COMMAND!\n")
    except:
        print("An Error has occured. Please try resetting the program by choosing option 5 in the Main Menu.")

MENU()

            
