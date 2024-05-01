class Battlepass():
    
    def __init__(link, name, item, points = 100):
        link.name = name
        link.item = item 
        link.points = points

    def skin(link):
        print(link.name + " claimed a skin!")
        print(link.name + " You have 0 points left!")
    
    def soundtrack(link):
        print(link.name + " claimed a sound track!")
        print(link.name + " You have 0 ponts left!")

    def pickaxe(link):
        print(link.name + " claimed a pickaxe!")
        print(link.name + " You have 0 points left!")

    def pet(link):
        print(link.name + " claimed a pet!")
        print(link.name + " You have 0 point left!")