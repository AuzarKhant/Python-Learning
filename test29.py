from test27 import Phone

class Smartphone(Phone) :
    def __init__(link, brand, model, battery = 100):
        super(). __init__(brand, model, battery)

    def touch(link):
        print("Scrolling the Phone")

    def game(link):
        print(link.battery- 10, "battery percent left")

    def nonestop(link):
        while True:
            if link.battery >= 0:
                link.battery -= 10
                print(link.battery-10, "left")
            else:
                print("out of battery")
            


        