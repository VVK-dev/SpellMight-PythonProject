import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="xii_project")
mycursor=mydb.cursor()

def View_Cards():
    #to view all cards
    sql="SELECT*FROM Cards"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    print("The cards will be displayed in the following order: ")
    print("(CardID, Card Name, Damage, Heal, Burn, Poison, Buff, Mark, Stamina)\n")
    input("Press Enter to continue...")
    for card in result:
        print(card)
    return    


    
