class Character():
    def __init__(self, name, hp, mp, atk, lvl):
        print("Character Created")
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.lvl = lvl
        print("Character name created " + self.name)

charone = Character("Jack", 100, 100, 10, 1)