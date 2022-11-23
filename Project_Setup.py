#This file sets up a table in MySQL required for the game
import os
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", passwd="root")
mycursor=mydb.cursor()

def createdb():
    #this function creates the cards table
    mycursor.execute("drop database if exists xii_project")    
    mycursor.execute("create database xii_project")
    mycursor.execute("use xii_project")
    table="CREATE TABLE Cards(CardID int(3) PRIMARY KEY,Name varchar(50),Damage varchar(2) NOT NULL,\
Heal varchar(2) NOT NULL, Burn varchar(2) NOT NULL,Poison varchar(2) NOT NULL, Buff varchar(2) NOT NULL,\
Mark varchar(2) NOT NULL, Stamina varchar(2) NOT NULL)"
    mycursor.execute(table)

def insert():
    #this function inserts cards into the table
    mycursor.execute("use xii_project")
    sql="insert into cards values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data=[(1,"The Eye of Ra",10,10,2,0,0,0,5),(2,"Dragon Breath",6,0,1,0,0,0,1),
          (3,"Plague of Anubis",15,10,0,0,2,0,7),(4,"Zeus' Bolt",30,0,0,0,2,0,10),
          (5,"Monolith of Terra",6,15,0,0,2,0,8),(6,"Fist of Mercury",8,0,0,0,0,0,1),
          (7,"The Eye of Horus",15,10,0,0,2,0,6),(8,"Staff of Sun Wukong",20,0,0,0,2,0,8),
          (9,"Slice of Excalibur",15,0,0,0,0,0,2),(10,"Might of Hercules",10,3,0,0,1,0,1),
          (11,"Achilles' Shield",7,5,0,0,0,1,2),(12,"Brush of Zhong Kui",7,5,0,1,0,2,3),
          (13,"Sword of Ao Kuang",15,5,0,0,0,1,5),(14,"Susano's Typhoon",25,0,0,0,0,0,9),
          (15,"Bite of Bakasura",15,8,0,0,2,1,6),(16,"Sol's Solar Flare",15,8,3,0,0,0,6),
          (17,"Agni's Path of Flames",10,0,4,0,0,0,6),(18,"Deadly thicket of Cernunnos",10,5,0,3,0,0,6),
          (19,"Scythe of Thanatos",15,10,0,0,2,2,7),(20,"Apollo's Melodey",12,5,0,0,2,0,4),
          (21,"Bacchus' Royal Feast",20,20,0,0,2,0,10),(22,"Artemis' Flurry of Arrows",15,0,0,1,1,0,8),
          (23,"Rama's Astral Strike",15,0,0,0,2,1,9),(24,"Mjolnir's strike",7,0,0,0,0,0,1),
          (25,"Medusa's Stone Gaze",15,0,0,1,0,1,8),(26,"Odin's Warcry",10,0,0,0,1,0,2),
          (27,"Anhur's Spear",10,0,0,0,0,2,3),(28,"Nox's Black Candles",17,0,0,0,0,1,6),
          (29,"Wizardry of Merlin",15,0,1,0,1,0,7),(30,"Loki's Daggers",12,0,0,2,0,0,4)]

    mycursor.executemany(sql,data)
    mydb.commit()

def setup():
    with open("DONOTDELETE.txt",'w') as f:
        f.write("Please do not delete this file, it is required to properly run the game.")
    return

dndpath=os.path.join(os.path.dirname(__file__), "DONOTDELETE.txt")
#dndpath stands for DoNotDelete path. Donotdelete is the text file created after table creation to show that
#the structures required for the game have been created

try:
    with open(dndpath,'r') as f:
        pass
except FileNotFoundError:
    print("Performing automatic Setup...")
    createdb()
    insert()
    setup()
    print("Setup Complete!")
