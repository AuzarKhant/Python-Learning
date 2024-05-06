class Phone():

    def __init__(link, Brand, Model, Battery = 100):
        link.Brand = Brand
        link.Model = Model
        link.battery = Battery 

    def camera(link):
        print(link.Brand + " is filming. Cha luck!")
        
    def call(link):
        print(link.Brand + " is calling. tu tu tu")


    
