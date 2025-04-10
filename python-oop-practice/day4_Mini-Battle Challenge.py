from abc import ABC, abstractmethod
import random

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
    
    def calculate_power(self):
        return self.strength + self.agility + self.magic

class Knight(Hero):
    def __init__(self, name, strength, agility, magic, armor):
        super().__init__(name, strength, agility, magic)
        self.armor = armor
    
    def special_move(self):
        print(f"{self.name} performs 'Shield Slam'! Armor absorbs heavy damage.")

class Mage(Hero):
    def __init__(self, name, strength, agility, magic, mana):
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
    def __init__(self, name, strength, agility, magic, gun, bullets):
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

a = random.randint(0, 3)
b = random.randint(0, 3)

player1 = heroes[a]
player2 = heroes[b]
print(f"\n--- Randomly Selected Players ---")
print(f"Player 1: {player1.name}")
print(f"Player 2: {player2.name}")

def final_showdown(player1, player2):
    if player1.name == player2.name:
        print("Both players are the same!")
    else:
        print(f"{player1.name} vs {player2.name} - The final showdown")
        player1.display_stats()
        player2.display_stats()

        print("\nSpecial Moves:")
        player1.special_move()
        player2.special_move()

        power1 = player1.calculate_power()
        power2 = player2.calculate_power()

        print(f"\n{player1.name}'s Power: {power1}")
        print(f"{player2.name}'s Power: {power2}")

        if power1 > power2:
            print(f"\n{player1.name} wins the battle!")
        elif power2 > power1:
            print(f"\n{player2.name} wins the battle!")
        else:
            print("\nIt's a tie!")

final_showdown(player1, player2)
