class Hero:
    def __init__(self, name, strength, agility, magic):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.magic = magic

    def display_stats(self):
        print(f"{self.name} - STR: {self.strength}, AGI: {self.agility}, MAG: {self.magic}")

    def train(self):
        self.strength += 5
        self.agility += 3
        self.magic += 2
        print(f"{self.name} has trained and leveled up!")

    def heal(self):
        self.magic += 3
        print("Healing increase", self.magic)

    def equip_weapon(self, weapon="bare hands"):
        self.weapon = weapon
        print(f"{self.name} has equipped the {self.weapon} of Destiny!")
        print(f"{self.name} - STR: {self.strength}, AGI: {self.agility}, MAG: {self.magic} | Weapon: {self.weapon}")


# Sample usage and practice
hero1 = Hero("Arjun", 10, 8, 5)
hero1.display_stats()
hero1.train()
hero1.display_stats()
hero1.heal()
hero1.equip_weapon("Sword")

