#This file enables developers to modify, create and delete cards in the game
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", passwd="root", database="xii_project")
mycursor=mydb.cursor()

def devcheck():
#This function checks if the user is a developer and has the authority to access the contents of this file
    while True:
        passwd=input("\nPlease enter the password for verification of authority or enter cancel to return\
to the Main Menu:\n==> ")
        if passwd=="root@123":
            print("\nDevCheck passed. Welcome.\n")
            return 1
#If the password is correct, they are allowed in and the function returns 1
        elif passwd.lower()=="cancel":
            return -1
        else:
            print("DevCheck failed. Please try again.")
#If the password they have entered is wrong, the function will loop again


def create():
#This function is used to create a card
    card=[]
    cID=int(input("Please enter the Card's ID number: "))
#This is the card's ID
    card.append(cID)
    print("Your card so far is: ",card)
    cname=input("Please enter the card's name: ")
#This is the name of the card
    if "'" in cname:
        cnamespl=cname.split("'")
        cname=cnamespl[0]+"\\'"+cnamespl[1]
#If the card has a ' in the name, a backslash is appended to it so that it won't raise an error in mysql
    card.append(cname)
    print("Your card so far is: ",card)
    cdmg=int(input("Please enter the amount of damage you want the card to deal: "))
#This is damage value of the card
    card.append(cdmg)
    print("Your card so far is: ",card)
    cheal=int(input("Please enter the amount of health you want this card to replenish: "))
#This is the heal of the card
    card.append(cheal)
    print("Your card so far is: ",card)
    cburn=int(input("Please enter the amount of rounds you want this card to burn the enemy for: "))
#This is the burn value of the card
    card.append(cburn)
    print("Your card so far is: ",card)
    cpoison=int(input("Please enter the amount of rounds you want the card to posion the enemy for: "))
#This is the posion value of the card
    card.append(cpoison)
    print("Your card so far is: ",card)
    cbuff=int(input("Please enter the amount of turns you want this card to buff the user for: "))
#This is the buff value of the card
    card.append(cbuff)
    print("Your card so far is: ",card)
    cmark=int(input("Please enter the amount of turns you want this card to mark the enemy for: "))
#This is the mark value of the card
    card.append(cmark)
    print("Your card so far is: ",card)
    cstamina=int(input("Please enter the stamina it costs to play the card: "))
#This is the stamina value of the card
    card.append(cstamina)
    tcard=tuple(card)
#We convert the card into a tuple here to insert it into the cards table withput any errors
    print("Your card so far is: ",tcard)
    opt=input("Are you sure you want to put this card into the game? ")
    if (opt=="y")or(opt=="Y")or(opt=="yes")or(opt=="Yes"):
#This clause checks whether the user wants to commit to the decision or not
        try:
            sql="insert into cards values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"    
            mycursor.execute(sql,tcard)
            mydb.commit()
            print("Card added and viewable via the View Cards option in the Main Menu.")
            print("Returning to the cards menu...")
            return
        except mysql.connector.errors.IntegrityError:
#If the user has entered a card with a name that already exists, they are taken back to the card menu
            print("That card already exists.")
            print("Returning to the cards menu...")
            return
    else:
        print("Returning to the cards menu...")
        return



def update():
#This function is used to update the information of a card
    while True:
        cID=input("\nPlease enter the ID of the card you want to modify or cancel to return to the Cards Menu: ")
        if cID.lower()=="cancel":
            print("Returning to the Cards Menu...")
            return
        else:
#This part checks whether or not there is a card in the table with the given ID
            sql1="select * from Cards"
            mycursor.execute(sql1)
            cardlist=mycursor.fetchall()
            newcard=0
            for card in cardlist:
                if str(card[0])==cID:
#If there is then it confirms that the user wants to update the information of that card
                    print(card)
                    ch=input("Are you sure you want to modify this card? ")
                    if (ch=="y")or(ch=="Y")or(ch=="Yes")or(ch=="yes"):
                        while True:
                            try:
                                opt=int(input("\nPlease enter the number corresponding to the stat\
 you want to change:\n\
1)CardID\n\
2)Name\n\
3)Damage\n\
4)Heal\n\
5)Burn\n\
6)Poison\n\
7)Buff\n\
8)Mark\n\
9)Stamina\n\
10)Choose a new card to modify\n\
11)Return to the Cards Menu\n==>"))

                                if opt==1:
                                #This clause updates the CardID of the card
                                    while True:
                                        try:
                                            ID=input("Please enter a new ID value: ")
                                            sql1="update Cards set CardID="+ID+" where CardID="+cID
                                            mycursor.execute(sql1)
                                            mydb.commit()
                                            sql2="select * from cards where CardID="+cID
                                            mycursor.execute(sql2)
                                            rec=mycursor.fetchone()
                                            print("The card is now: ",rec)
                                            break
                                        except mysql.connector.errors.ProgrammingError:
                                            print("Invalid input.")    
                                    print("Card updated and viewable via the View Cards option in the Main Menu.")
                                elif opt==2:
                                #This clause updates the name of the card
                                    nm=input("Please enter a new name: ")
                                    if "'" in nm:
                                        nmspl=nm.split("'")
                                        nm=nmspl[0]+"\\'"+nmspl[1]
                                    sql1="update Cards set Name='"+nm+"' where CardID="+cID
                                    mycursor.execute(sql1)
                                    mydb.commit()
                                    sql2="select * from cards where CardID="+cID
                                    mycursor.execute(sql2)
                                    rec=mycursor.fetchone()
                                    print("The card is now: ",rec)
                                    print("Card updated and viewable via the View Cards option in the Main Menu.")
                                elif opt==3:
                                #This clause updates the damage value of the card
                                    while True:
                                        try:
                                            dmg=input("Please enter a new damage value: ")
                                            sql1="update Cards set Damage="+dmg+" where CardID="+cID
                                            mycursor.execute(sql1)
                                            mydb.commit()
                                            sql2="select * from cards where CardID="+cID
                                            mycursor.execute(sql2)
                                            rec=mycursor.fetchone()
                                            print("The card is now: ",rec)
                                            break
                                        except mysql.connector.errors.ProgrammingError:
                                            print("Invalid input.")
                                    print("Card updated and viewable via the View Cards option in the Main Menu.")
                                elif opt==4:
                                #This clause updates the heal value of the card
                                    while True:
                                        try:
                                            heal=input("Please enter a new heal value: ")                               
                                            sql1="update Cards set Heal="+heal+" where CardID="+cID
                                            mycursor.execute(sql1)
                                            mydb.commit()
                                            sql2="select * from cards where CardID="+cID
                                            mycursor.execute(sql2)
                                            rec=mycursor.fetchone()
                                            print("The card is now: ",rec)
                                            break
                                        except mysql.connector.errors.ProgrammingError:
                                            print("Invalid input.")
                                    print("Card updated and viewable via the View Cards option in the Main Menu.")
                                elif opt==5:
                                #This clause updates the burn value of the card
                                    while True:
                                        try:
                                            burn=input("Please enter a new burn value: ")
                                            sql1="update Cards set Burn="+burn+" where CardID="+cID
                                            mycursor.execute(sql1)
                                            mydb.commit()
                                            sql2="select * from cards where CardID="+cID
                                            mycursor.execute(sql2)
                                            rec=mycursor.fetchone()
                                            print("The card is now: ",rec)
                                            break
                                        except mysql.connector.errors.ProgrammingError:
                                            print("Invalid input.")
                                    print("Card updated and viewable via the View Cards option in the Main Menu.")
                                elif opt==6:
                                #This cluase updates the poison value of the card
                                    while True:
                                        try:
                                            poison=input("Please enter a new posion value: ")
                                            sql1="update Cards set Poison="+poison+" where CardID="+cID
                                            mycursor.execute(sql1)
                                            mydb.commit()
                                            sql2="select * from cards where CardID="+cID
                                            mycursor.execute(sql2)
                                            rec=mycursor.fetchone()
                                            print("The card is now: ",rec)
                                            break
                                        except mysql.connector.errors.ProgrammingError:
                                            print("Invalid input.")
                                    print("Card updated and viewable via the View Cards option in the Main Menu.")
                                elif opt==7:
                                #This clause updates the buff value of the card
                                    while True:
                                        try:
                                            buff=input("Please enter a new buff value: ")
                                            sql1="update Cards set Buff="+buff+" where CardID="+cID
                                            mycursor.execute(sql1)
                                            mydb.commit()
                                            sql2="select * from cards where CardID="+cID
                                            mycursor.execute(sql2)
                                            rec=mycursor.fetchone()
                                            print("The card is now: ",rec)
                                            break
                                        except mysql.connector.errors.ProgrammingError:
                                            print("Invalid input.")
                                    print("Card updated and viewable via the View Cards option in the Main Menu.")
                                elif opt==8:
                                #This clause updates the mark value of the card
                                    while True:
                                        try:
                                            mark=input("Please enter a new mark value: ")
                                            sql1="update Cards set Mark="+mark+" where CardID="+cID
                                            mycursor.execute(sql1)
                                            mydb.commit()
                                            sql2="select * from cards where CardID="+cID
                                            mycursor.execute(sql2)
                                            rec=mycursor.fetchone()
                                            print("The card is now: ",rec)
                                            break
                                        except mysql.connector.errors.ProgrammingError:
                                            print("Invalid input.")
                                    print("Card updated and viewable via the View Cards option in the Main Menu.")
                                elif opt==9:
                                #This clause updates the stamina value of the card
                                    while True:
                                        try:
                                            stamina=input("Please enter a new stamina value: ")
                                            sql1="update Cards set stamina="+stamina+" where CardID="+cID
                                            mycursor.execute(sql1)
                                            mydb.commit()
                                            sql2="select * from cards where CardID="+cID
                                            mycursor.execute(sql2)
                                            rec=mycursor.fetchone()
                                            print("The card is now: ",rec)
                                            break
                                        except mysql.connector.errors.ProgrammingError:
                                            print("Invalid input.")
                                    print("Card updated and viewable via the View Cards option in the Main Menu.")
                                elif opt==10:
                                #If the user wants to change another card, the newcard variable is incremented by 1
                                    newcard+=1    
                                    break
                                elif opt==11:
                                #This ends the function and returns to the Cards Menu
                                    print("Returning to the Cards Menu...")
                                    return
                                else:
                                    print("Invalid Input. Please try again.")
                            except ValueError:
                                print("Invalid Input. Please try again.")
                    else:
                        newcard+=1
            else:
                if newcard==1:
                #If the user wishes to modify another card then this function reloops
                    pass
                elif newcard==-1:
        #If the user wishes to exit the function then the function is closed and the user returns to the Cards Menu
                    return
                else:
            #If the name entered by the use doesn't match that of any in the table, the following message is displayed
                    print("That card does not exist. Please try again.")
    

def delete():
#This function allows the user to delete a card
    while True:
        delete=0
        ch1=input("Please enter the ID of the card you want to delete or cancel to return to the Cards Menu: ")
        if ch1.lower()=="cancel":
            return
        else:
            sql1="select * from Cards"
            mycursor.execute(sql1)
            cardlist=mycursor.fetchall()
            for card in cardlist:
                if ch1==str(card[0]):
                    delete+=1
                    sql2="select * from Cards where CardID="+str(card[0])
                    mycursor.execute(sql2)
                    print(mycursor.fetchall())
                    ch2=input("Are you sure you want to delete this card? ")
                    if ch2=="y" or ch2=="Y" or ch2=="Yes" or ch2=="yes":
                        sql3="delete from Cards where CardID="+str(card[0])
                        mycursor.execute(sql3)
                        print("Card Deleted.")
                        mydb.commit()
                        ch3=input("Would you like to delete another card?")
                        if ch3.lower()=="y" or ch3.lower()=="yes":
                            break
                        else:
                            return
                    else:
                        break
            else:
                if delete==0:
#the use of the delete variable is to prevent this string from printing if the user wishes to delete another card
                    print("That Card does not exist. Please try again.")
                    


def Cards_Menu():
#This is the Cards Menu. This function allows users to acces the other parts of this program if they pass the DevCheck
    out=devcheck()
    if out==1:
        while True:
            print("\n=================CARDS MENU===============")
            ch=input("\nPlease enter the corresponding number to your choice:\n\
1)Create a new card\n\
2)Update an existing card\n\
3)Delete a card\n\
4)Exit to the Main Menu\n\
==> ")
            if ch=="1":
                    create()
            elif ch=="2":
                    update()
            elif ch=="3":
                    delete()
            elif ch=="4":
                print("Exiting...")
                return
            else:
                print("Invalid Input. Please try again.\n")
    else:       
        return
