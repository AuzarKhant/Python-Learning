class Character():
    
    def __init__(link, name, spell, hp=100):
        link.name = name
        link.spell = spell
        link.hp = hp

    def jump(link):
        print(link.name + " is jumping")

    def prone(link):
        print(link.name + "is proning")

    def run(link):
        print(link.name + "is running")

    def shoot(link):
        print(link.name + "is shooting")