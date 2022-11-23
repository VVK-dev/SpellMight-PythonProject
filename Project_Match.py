import random
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", passwd="root", database="xii_project")
mycursor=mydb.cursor()


def Match():
    p1=input("\nPlease enter player 1's name: ")
    p2=input("Please enter player 2's name: ")
    print("GET READY!")
    firstturn=0
    rounds=1
    p1health=100
    p2health=100
    p1burn=0
    p2burn=0
    p1poison=0
    p2poison=0
    p1mark=0
    p2mark=0
    p1buff=0
    p2buff=0
    while rounds<=15:
        #win condition
        if p1health<1:
            print(p2.upper()," WINS!")
            break
        elif p2health<1:
            print(p1.upper()," WINS!")
            break
        #this is a 2 player game, hence there are 2 turns: 1 for each player
        turns=[1,2]
        for currentturn in turns:
            #player 1's turn
            if rounds==1 and firstturn==0:
            #this block ensures that the 1st player doesn't get an advantage by always going first
                firstturn+=1
                currentturn=random.choice(turns)
            if currentturn==1:
                if p1health<1:
                    break
                elif p2health<1:
                    break
                else:
                    print("\nRound number: ",rounds,"\n")
                    print(p1.upper()+"'S TURN!")
                    stamina=10
                    sql="select Name, Damage, Heal, Burn, Poison, Buff, Mark, Stamina from cards order by rand() limit 5"
                    mycursor.execute(sql)
                    hand=mycursor.fetchall()
                    while stamina>0:
                        #these first few ifs and elifs print an [M] next to the name of the player that is marked
                        if p1mark==0 and p2mark==0:
                            print(p1+"'s health: ",p1health,"|",p2+"'s health:",p2health)
                        elif p1mark>0 and p2mark>0:
                            print(p1+"'s health: ",p1health,"[M] |",p2+"'s health:",p2health,"[M]")
                        elif p1mark>0 and p2mark==0:
                            print(p1+"'s health: ",p1health,"[M] |",p2+"'s health:",p2health)
                        elif p1mark==0 and p2mark>0:
                            print(p1+"'s health: ",p1health,"|",p2+"'s health:",p2health,"[M]")
                        handindex=[]
                        for card in hand:
                            handindex.append(hand.index(card))
                            print(hand.index(card)," : ","(",card[0],"|Damage:",card[1],"|Heal:",card[2],"|Burn:",card[3],
                                  "|Poison:",card[4],"|Buff:",card[5],"|Mark:",card[6],"|Stamina:",card[7],")")
                        if p1burn!=0:
                            p1health=p1health-2
                            print(p1,"takes 2 damage due to burn.",p1burn-1,"round(s) left")
                        if p1poison!=0:
                            p1health=p1health-1
                            print(p1,"takes 1 damage due to poison.",p1poison-1,"round(s) left")
                        if p1buff>0:
                            print(p1,"is currently buffed.",p1buff-1,"round(s) remaining.")          
                        if p1mark>0:
                            print(p1,"is currently marked.",p1mark-1,"round(s) remiaining.") 
                        print("Stamina: ",stamina)

                        ch=input("Please enter the corresponding number with the card to choose that card or p to \
pass your turn: ")
                        if ch=="p":
                            print(p1," chooses to pass their turn!")
                            break
                        else:
                        #this next while loop checks whether the value entered by the user is a legal value or not
                            while True:
                                legal1=0
                                legal2=0
                                if ch not in str(handindex):
                        #this checks whether the number entered by the user has a corresponding card
                                    pass
                                else:
                        #this part is to check whether the user has enough stamina to play the chosen card
                                    legal1+=1
                                    usedcard=hand.pop(int(ch))
                                    cardstamina=int(usedcard[7])
                                    if cardstamina>stamina:
                                        hand.insert(int(ch),usedcard)
                                        pass
                                    else:
                                        legal2+=1
                                if legal1==1 and legal2==1:
                                    break
                                else:
                                    print("Invalid input. You either don't have enough stamina to play this\
 card or you have entered an incorrect index.")
                                    ch=input("Please enter the number corresponding with the card to choose that \
card or p to pass your turn: ")
                                    if ch=="p":
                                        print(p1," chooses to pass their turn!")
                                        break

                        damage=int(usedcard[1])
                        heal=int(usedcard[2])
                        burn=int(usedcard[3])
                        poison=int(usedcard[4])
                        buff=int(usedcard[5])
                        mark=int(usedcard[6])
                        print(p1," has used: ", usedcard)
                        if damage!=0:
                            if p1buff>0:
                                damage=damage*1.15
                            if p2mark>0:
                                damage=damage*1.15
                            if p1poison>0:
                                damage=damage*0.80
                            print(p1,"deals",damage,"damage to",p2)
                            p2health=p2health-damage
                        if heal!=0:
                            if p1buff>0:
                                heal=heal*1.15
                            if p1burn>0:
                                heal=heal*0.80
                            print(p1,"heals themselves for", heal)
                            if heal+p1health>100:
                                p1health=100    
                            else:
                                p1health=p1health+heal
                        if burn!=0:
                            p2burn=burn
                            print(p1,"affllicts",p2,"with burn for the next",burn,"round(s)!")
                        if poison!=0:
                            p2posion=poison
                            print(p1,"afflicts",p2,"with a poison for the next",poison,"round(s)!")
                        if buff!=0:
                            p1buff=buff
                            print(p1,"buffs themselves for the next",buff,"round(s)!")
                        if mark!=0:
                            p2mark=mark
                            print(p1,"marks",p2,"for the next",mark,"round(s)!")
                        stamina=stamina-cardstamina
                            
                    
            else:
                #player 2's turn
                if p1health<1:
                    break
                elif p2health<1:
                    break
                else:
                    print("\nRound number: ",rounds,"\n")
                    print(p2.upper()+"'S TURN!")
                    stamina=10
                    sql="select Name, Damage, Heal, Burn, Poison, Buff, Mark, Stamina from cards order by rand() limit 5"
                    mycursor.execute(sql)
                    hand=mycursor.fetchall()
                    while stamina>0:
                        #these first few ifs and elifs print an [M] next to the name of the player that is marked
                        if p1mark==0 and p2mark==0:
                            print(p1+"'s health: ",p1health,"|",p2+"'s health:",p2health)
                        elif p1mark>0 and p2mark>0:
                            print(p1+"'s health: ",p1health,"[M] |",p2+"'s health:",p2health,"[M]")
                        elif p1mark>0 and p2mark==0:
                            print(p1+"'s health: ",p1health,"[M] |",p2+"'s health:",p2health)
                        elif p1mark==0 and p2mark>0:
                            print(p1+"'s health: ",p1health,"|",p2+"'s health:",p2health,"[M]")
                        handindex=[]
                        for card in hand:
                            handindex.append(hand.index(card))
                            print(hand.index(card)," : ","(",card[0],"|Damage:",card[1],"|Heal:",card[2],"|Burn:",card[3],
                                  "|Poison:",card[4],"|Buff:",card[5],"|Mark:",card[6],"|Stamina:",card[7],")")
                        if p2burn!=0:
                            p2health=p2health-2
                            print(p2,"takes 2 damage due to burn.",p2burn-1,"round(s) left")
                        if p2poison!=0:
                            p2health=p2health-1
                            print(p2," takes 1 damage due to poison.",p2poison-1,"round(s) left")
                        if p2buff>0:
                            print(p2,"is currently buffed.",p2buff-1,"round(s) remaining.")          
                        if p2mark>0:
                            print(p2,"is currently marked.",p2mark-1,"round(s) remiaining.")
                        print("Stamina: ",stamina)

                        ch=input("Please enter the corresponding number with the card to choose that card or\
 p to pass your turn: ")
                        if ch=="p":
                            print(p2," chooses to pass their turn!")
                            break
                        else:
                        #this next while loop checks whether the value entered by the user is a legal value or not
                            while True:
                                legal1=0
                                legal2=0
                        #the next if checks whether the number entered by the user has a corresponding card
                                if ch not in str(handindex):
                                    pass
                                else:
                        #this part is to check whether the user has enough stamina to play the chosen card
                                    legal1+=1
                                    usedcard=hand.pop(int(ch))
                                    cardstamina=int(usedcard[7])
                                    if cardstamina>stamina:
                                        hand.insert(int(ch),usedcard)
                                        pass
                                    else:
                                        legal2+=1
                                if legal1==1 and legal2==1:
                                    break
                                else:
                                    print("Invalid input. You either don't have enough stamina to play this\
 card or you have entered an incorrect index.")
                                    ch=input("Please enter the corresponding number with the card to choose that \
card or p to pass your turn: ")
                                    if ch=="p":
                                        print(p1," chooses to pass their turn!")
                                        break
                            
                        damage=int(usedcard[1])
                        heal=int(usedcard[2])
                        burn=int(usedcard[3])
                        poison=int(usedcard[4])
                        buff=int(usedcard[5])
                        mark=int(usedcard[6])
                        print(p2," has used: ", usedcard)
                        if damage!=0:
                            if p2buff>0:
                                damage=damage*1.15
                            if p1mark>0:
                                damage=damage*1.15
                            if p2poison>0:
                                damage=damage*0.80
                            print(p2,"deals",damage,"damage to",p1)
                            p1health=p1health-damage
                        if heal!=0:
                            if p2buff>0:
                                heal=heal*1.15
                            if p2burn>0:
                                heal=heal*0.80
                            print(p2,"heals themselves for", heal)
                            if heal+p2health>100:
                                p2health=100    
                            else:
                                p2health=p2health+heal
                        if burn!=0:
                            p1burn=burn+1
                            print(p2,"afflicts",p1,"with burn for the next",burn,"round(s)!")
                        if poison!=0:
                            p2posion=poison+1
                            print(p2,"afflicts",p1,"with a poison for the next",poison,"round(s)!")
                        if buff!=0:
                            p2buff=buff+1
                            print(p2,"buffs themselves for the next",buff,"round(s)!")
                        if mark!=0:
                            p1mark=mark+1
                            print(p2,"marks",p1,"for the next",mark,"round(s)!")
                        stamina=stamina-cardstamina
                    else:
                        break


        if p1burn>0:
            p1burn=p1burn-1
        if p2burn>0:
            p2burn=p2burn-1
        if p1poison>0:
            p1poison=p1poison-1
        if p2poison>0:
            p2posion=p2poison-1
        if p1mark>0:
            p1mark=p1mark-1
        if p2mark>0:
            p2mark=p2mark-1
        if p1buff>0:
            p1buff=p1buff-1
        if p2buff>0:
            p2buff=p2buff-1
        rounds=rounds+1
        
    else:
    #When the number of rounds exceeds 15, the game stops and the winner is automatically calculated
        print("\nThe number of rounds has exceeded 15!")
        print("Calculating winner...")
        if p1health>p2health:
            print(p1.upper()," WINS!")
        elif p2health>p1health:
            print(p2.upper()," WINS!")
        else:
            print("Its a perfect draw!")
            
    ch=input("Would you like to play another match or return to the main menu? Enter y to play another match or n \
to return to the main menu: ")
    if ch.lower()=="y" or ch.lower()=="yes":
        Match()
    else:
        return    
                
            
