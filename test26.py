from test25 import Battlepass

Name = input(" Please enter your Name: ")


Choice = input("""
                                                    what would u like to claim? 
                                          skin        pet     pickaxe        soundtrack  
                                                Enter here: """)

if Choice == "skin":
    c1 = Battlepass(Name, "skin")
    c1.skin()
if Choice == "pickaxe":
    c2 = Battlepass(Name, "pickaxe")
    c2.pickaxe()

if Choice == "soundtrack":
    c3 = Battlepass(Name, "soundtrack")
    c3.soundtrack()

if Choice == "pet":
    c4 = Battlepass(Name, "pet")
    c4.pet()