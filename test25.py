class Battlepass():
    
    def __init__(link, name, item, points = 100):
        link.name = name
        link.item = item 
        link.points = points

    def skin(link):
        print(link.name + " claimed a skin!")
        print(link.name + " You have ", link.points - 50, " points left!")
        

    
    def soundtrack(link):
        print(link.name + " claimed a sound track!")
        print(link.name + " You have ", link.points - 40, " points left!")
        
    

    def pickaxe(link):
        print(link.name + " claimed a pickaxe!")
        print(link.name + " You have  ", link.points - 30, " points left!")
        
    

    def pet(link):
        print(link.name + " claimed a pet!")
        print(link.name + " You have ", link.points - 80, " points left!")