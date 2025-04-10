from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, strength, agility, magic):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.magic = magic

    @abstractmethod
    def special_move(self):
        pass
    
    def display_stats(self):
        print(f"{self.name} - STR: {self.strength}, AGI: {self.agility}, MAG: {self.magic}")

class Knight(Hero):
    def __init__(self, name, strength, agility, magic, armor):
        super().__init__(name, strength, agility, magic)
        self.armor = armor
    
    def special_move(self):
        print(f"{self.name} performs 'Shield Slam'! Armor absorbs heavy damage.")

class Mage(Hero):
    def __init__(self,name, strength, agility, magic, mana):
        super().__init__(name, strength, agility, magic)
        self.mana = mana
    
    def special_move(self):
        print(f"{self.name} casts 'Arcane Blast' using mana {self.mana}!")

class Archer(Hero):
    def __init__(self, name, strength, agility, magic, arrows):
        super().__init__(name, strength, agility, magic)
        self.arrows = arrows
    
    def special_move(self):
        print(f"{self.name} unleashes 'Rain of Arrows'!")

class GunMan(Hero):
    def __init__(self, name, strength, agility, magic,gun, bullets):
        super().__init__(name, strength, agility, magic)
        self.bullets = bullets
        self.gun = gun
    
    def special_move(self):
        print(f"{self.name} fires 'Rapid Fire' with {self.bullets} bullets!")


def start_round(hero):
    print("\n--- Battle Begins ---")
    hero.display_stats()
    hero.special_move()
    print("--- Battle Ends ---\n")


heroes = [
    Knight("Arjun", 12, 9, 5, "Steel Armor"),
    Mage("Gandalf", 8, 6, 15, 50),
    Archer("Eklavya", 10, 12, 0, 20),
    GunMan("Rambo", 14, 10, 0, "AK-47", 30)
]

for hero in heroes:
    start_round(hero)
