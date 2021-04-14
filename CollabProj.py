import gc
import webbrowser
import sys
import mysql.connector
from time import sleep
import os


global Fire

whatHappened = []

class listClass(list):
    def __init__(self):
        self = list()
    def add(self,name):
        self.append(name)

class recommended:
    def __init__(self,proc,ram,mother,graphics,drive,psu,price):
        self.proc = proc
        self.ram = ram
        self.mother = mother
        self.graphics = graphics
        self.drive = drive
        self.psu = psu
        self.price = price

class recommendedGames:
    def __init__(self,name,price,genre,audience,link):
        self.name = name
        self.price = price
        self.genre = genre
        self.audience = audience
        self.link = link

class dictGame(dict):
    def __init__(self):
        self = dict()
    def add(self,key,value):
        self[key] = value


#ARI PAG ADD SA GAME NGA CLASS KHE
"""
NOT YET COMPLETE NGA GAME CLASS
class Game:
    def __init__(self,name,price,genre,developer,link):
        self.name = name
""" 


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "home123",
    database = "expertsystem"
)



global _proc,_ram,_mother,_graphics,_drive,_psu,_price
link = mydb.cursor()
link2 = mydb.cursor()
anotherLink = mydb.cursor()
rowList = []
#mydb.commit()
recomList = []
recomListGames = []
class KnowBase:
    def Rule_1(self,antecedent,_object):
      
        link.execute("Select fact from factsForUse where fact = %s",(antecedent,))
        linkRes = link.fetchone()
       # rowList = linkRes
        for x in linkRes:
            if(x == "school" and antecedent == x):
                whatHappened.append("First: We check if the term (school) is in our database")
                engine(antecedent,_object)
                break
            else:
                break
     
            
    def Rule_2(self,antecedent,_object):
        link.execute("Select fact from factsForUse where fact = %s",(antecedent,))
        linkRes = link.fetchone()
       
        for x in linkRes:
            if(x == "gaming" and antecedent == x):
                whatHappened.append("First: We check if the term (gaming) is in our database")
                engine(antecedent,_object)
                break
            else:
                break

    def Rule_3(self,antecedent,_object):
        link.execute("Select fact from factsForUse where fact = %s",(antecedent,))
        linkRes = link.fetchone()
        
        for x in linkRes:
            if(x == "video editing" and antecedent == x):
                whatHappened.append("First: We check if the term (video editing) is in our database")
                engine(antecedent,_object)
                break
            elif(x == "gaming/videoEditing" and antecedent == x):
                whatHappened.append("First: We check if the term (video editing and gaming) is in our database")
                engine(antecedent,_object)
            else:
                break          


queryList = []
class KnowledgeBaseGames:
    def RuleGames_1(self,genre,gamer,budget):
        contS = "" 
        contOne = "" 
        link2.execute("Select fact from factsforgenres where fact = %s",(genre,))
        linkRes = link2.fetchone()
      

        

        if(linkRes[0] == "real time strategy games"):
            contS = "real time strategy games"
            
                
        anotherLink.execute("Select fact from factsforgamers where fact = %s",(gamer,))
        
        anotherLinkRes = anotherLink.fetchone()
        #print(anotherLinkRes[0])
        
        if(anotherLinkRes[0] == "casual"):
            contOne = "casual"
        elif(anotherLinkRes[0] == "mediocore"):  
            contOne = "mediocore"
        elif(anotherLinkRes[0] == "hardcore"):
            contOne = "hardcore"

      
        if(len(contOne) !=0 and len(contS) != 0):
            whatHappened.append("First: We checked if the genre RTS exist in the database")
            whatHappened.append("Second: We checked if the type of gamer is in the database")
            engineGames(genre,gamer,budget)
            print("Rule 1 True")
            return True
        else:
            print("Rule 1 False")
            return False
      
            

    def RuleGames_2(self,genre,gamer,budget):
        link2.execute("Select fact from factsforgenres where fact = %s",(genre,))
        
        linkRes = link2.fetchone()
        countS = ""
        contTwoStr = ""

        if(linkRes[0] == "rpg"):
            countS = "rpg"

        anotherLink.execute("Select fact from factsforgamers where fact = %s",(gamer,))
        
        anotherLinkRes = anotherLink.fetchone()
        
        if(anotherLinkRes[0] == "casual"):
            contTwoStr = "casual"
        elif(anotherLinkRes[0] == "mediocore"):  
            contTwoStr = "mediocore"
        elif(anotherLinkRes[0] == "hardcore"):
            contTwoStr = "hardcore"
        
        if(len(contTwoStr) != 0 and len(countS)!= 0):
            whatHappened.append("First: We checked if the genre RPG exist in the database")
            whatHappened.append("Second: We checked if the type of gamer is in the database")
            engineGames(genre,gamer,budget)
            print("Rule 2 True")
            return True
        else:
            print("Rule 2 False")
            return False

    def RuleGames_3(self,genre,gamer,budget):
        countS = ""
        contOneStr = ""
  
        link2.execute("Select fact from factsforgenres where fact = %s",(genre,))
        
        linkRes = link2.fetchone()
        if(linkRes[0] == "adventure"):
            countS = "adventure"
            
        anotherLink.execute("Select fact from factsforgamers where fact = %s",(gamer,))
        anotherLinkRes = anotherLink.fetchone()
        
        if(anotherLinkRes[0] == "casual"):
            contOneStr = "casual"
        elif(anotherLinkRes[0] == "mediocore"):  
            contOneStr = "mediocore"
        elif(anotherLinkRes[0] == "hardcore"):
            contOneStr = "hardcore"

        if(len(contOneStr) != 0 and len(countS)!= 0):
            whatHappened.append("First: We checked if the genre Adventure exist in the database")
            whatHappened.append("Second: We checked if the type of gamer is in the database")
            engineGames(genre,gamer,budget)
            print("Rule 3 True")
            return True
        else:
            print("Rule 3 False")
            return False

    def RuleGames_4(self,genre,gamer,budget):
        countS = ""
        contOneStr = ""
  
        link2.execute("Select fact from factsforgenres where fact = %s",(genre,))

        linkRes = link2.fetchone()
        if(linkRes[0] == "simulation"):
            countS = "simulation"
                
        anotherLink.execute("Select fact from factsforgamers where fact = %s",(gamer,))
        
        anotherLinkRes = anotherLink.fetchone()
        if(anotherLinkRes[0] == "casual"):
            contOneStr = x
        elif(anotherLinkRes[0] == "mediocore"):  
            contOneStr = x
        elif(anotherLinkRes[0] == "hardcore"):
            contOneStr = x

        if(len(contOneStr) != 0  and len(countS)!=0):
            whatHappened.append("First: We checked if the genre Simulation exist in the database")
            whatHappened.append("Second: We checked if the type of gamer is in the database")
            engineGames(genre,gamer,budget)
            print("Rule 4 True")
            return True
        else:
            print("Rule 4 False")
            return False


def engineGames(genre,gamer,budget):
    link2.execute("Select * from games where gameGenre = %s AND gamePrice < %s AND gameAudience = %s", (genre,budget,gamer,))    
    okayStr = str(budget)
    okay = "Third: We now fetch the data from database that are " + genre + " and suitable for a " + gamer + " gamer like you" + " and within your budget ₱" + okayStr
    whatHappened.append(okay)
    linkRes = link2.fetchall()
    for var in linkRes:
        gameName = var[1]
        gamePrice = var[2]
        gameGenre = var[3]
        gameAudience = var[4]
        gameLink = var[5]
            
        recomListGames.append(recommendedGames(gameName,gamePrice,gameGenre,gameAudience,gameLink))    




def engine(antecedent,_object):
        link.execute("Select * from setList where purpose = %s AND price < %s", (antecedent,_object,))
        okayStr = str(_object)
        whatHappened.append("Second: We check if there's suitable matches for the budget that you have")
        okay = "Third: We fetch the data from our database that matches best for your " + antecedent + " with ₱" + okayStr + " budget"
        whatHappened.append(okay)
        linkRes = link.fetchall()
        for var in linkRes:
            _proc = var[1]
            _ram = var[3]
            _mother = var[2]
            _graphics = var[4]
            _drive = var[5]
            _psu = var[6]
            _price = var[7]
            recomList.append(recommended(_proc,_ram,_mother,_graphics,_drive,_psu,_price))    



knowBaseGame = KnowledgeBaseGames()
knowBaseR = KnowBase()        
listMain = listClass()
dictMain = dictGame()
Fire = False
useChecker = False
checkerForBuilds = False
checkerForGames = False
#MENU
while(checkerForBuilds != True):
    count = 0
    checkerForGames = False
    x = "===>WELCOME TO NOT A PC SHOP<==="
    header = x.center(125)
    print("\n\n",header)
    use = input("\n(Press [e] to Exit)\n[build] Ask for recommended PC builds!\n[games] Having trouble deciding what games to play? Ask now!\nPick your poison: ")
    userHelp = use.lower()
    if(userHelp == 'e'):
        sys.exit()    
        checkerForBuilds = True
    elif(userHelp == "build"):
        use = input("\nYou will use this PC for?: ")
        budgetStr = input("\nBudget: ₱")
        budget = int(budgetStr)
                #RULE FIRING
        knowBaseR.Rule_1(use,budget)
        knowBaseR.Rule_2(use,budget)
        knowBaseR.Rule_3(use,budget)
                #END OF RULE FIRING
        if(recomList):
            for obj in recomList:
                count += 1
                if(count-1 == len(recomList)-1):
                    print("\n(BEST!) Recommendation #",count)
                else:
                    print("\n(Another Choice!) Recommendation #",count)
                print("\n[Processor]      ==> ",obj.proc,"\n[Motherboard]    ==> ", obj.mother,"\n[RAM]            ==> ",obj.ram,\
                    "\n[Graphics Card]  ==> ",obj.graphics,"\n[Storage]        ==> ",obj.drive,"\n[PSU]            ==> ",obj.psu,\
                    "\n[Price]          ==>  ₱",obj.price        
                )
        else:
            print("Sorry! There's no specific pc build set for that kind of budget :(")
        
        print("How did we arrive to this?: ")
        for var in whatHappened:
            print("\n")
            print(var)
        clear = input("Press Enter to Clear")
        os.system('cls')
        recomList.clear()
        whatHappened.clear()
        use = " "
    elif(userHelp == "games"):
        while(checkerForGames != True and checkerForBuilds != True): 
            count = 0  
            homeStr = input("\n\n[1] Choose Genre\n[2] Back to Main Menu\nInput: ")
            home = int(homeStr)
            if(home == 1):
                genreStr = input("\n(Type [back] to go back to main menu)\nEnter Genre: ")
                genre = genreStr.lower()
                budgetStr = input("\nLet's see your budget: ₱")
                budgetInt = int(budgetStr)
                typeOfGamerUp = input("\nHave you played games before?\n[not once] My first time actually [not really] I've played some [YES] I've spent thousand of hours of gaming.\nAnswer: ")
                if(typeOfGamerUp == "not once"):
                    typeofGamerLow = "casual"
                elif(typeOfGamerUp == "not really"):
                    typeofGamerLow = "mediocore"   
                else:
                    typeofGamerLow = "hardcore"
                
                
                                    #RULE FIRING
                knowBaseGame.RuleGames_1(genre,typeofGamerLow,budgetInt)
                knowBaseGame.RuleGames_2(genre,typeofGamerLow,budgetInt)
                knowBaseGame.RuleGames_3(genre,typeofGamerLow,budgetInt)
                knowBaseGame.RuleGames_4(genre,typeofGamerLow,budgetInt)
                                    #END OF RULE FIRING     
                if(recomListGames):
                    print("\nRecommended Games for your budget ₱", budgetInt,"\n")
                    for obj in recomListGames:
                        count += 1
                        print("[",count,"] ==> ",obj.name," <===> ",obj.price)
                        dictMain.add(count,obj.link)

                    
                    link = input("Type number to install: ")
                    for var in dictMain:
                        if(var == int(link)):
                            webbrowser.open(dictMain[var])  
                else:
                    print("Unfortunately, there's no games in that budget. You might wanna try some free games")
                print("How Did We Arrived to this?\n")
                for x in whatHappened:
                    print(x)
                clear = input("Press Enter to Clear")
                os.system('cls')
                whatHappened.clear()
                recomListGames.clear() 
            elif(home == 2):
                checkerForGames = True
                
                
    


            
