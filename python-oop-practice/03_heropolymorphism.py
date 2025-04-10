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
        print("Healing increased to", self.magic)

    def equip_weapon(self, weapon="bare hands"):
        self.weapon = weapon
        print(f"{self.name} has equipped the {self.weapon} of Destiny!")

    def battle_cry(self):
        print(f"{self.name} shouts: 'For Glory!'")

# ---------------------------

class Knight(Hero):
    def __init__(self, name, strength, agility, magic, armor):
        super().__init__(name, strength, agility, magic)
        self.armor = armor

    def display_stats(self):
        super().display_stats()
        print(f"Armor: {self.armor}")

    def shield_block(self):
        print(f"{self.name} blocks with their shield! Armor absorbs damage.")

    def sword_attack(self):
        print(f"{self.name} attacks with their sword!")

# ---------------------------

class Mage(Hero):
    def __init__(self, name, strength, agility, magic, mana):
        super().__init__(name, strength, agility, magic)
        self.mana = mana

    def display_stats(self):
        super().display_stats()
        print(f"Mana: {self.mana}")

    def cast_spell(self, spell):
        if self.mana >= 10:
            print(f"{self.name} casts {spell}!")
            self.mana -= 10
        else:
            print(f"{self.name} does not have enough mana to cast {spell}.")

    def regenerating(self):
        if self.mana <= 10:
            print(f"{self.name} is regenerating mana!")
            self.mana += 10
        else:
            print(f"{self.name} has enough mana!")

# ---------------------------

class Archer(Hero):
    def __init__(self, name, strength, agility, arrow):
        super().__init__(name, strength, agility, magic=0)
        self.arrow = arrow

    def shoot_arrow(self):
        if self.arrow > 0:
            print(f"{self.name} shoots an arrow!")
            self.arrow -= 1
        else:
            print(f"{self.name} has no arrows left!")

    def buy_arrow(self, arrows):
        self.arrow += arrows
        print(f"{self.name} has bought {arrows} arrows! Total arrows: {self.arrow}")

    def display_stats(self):
        super().display_stats()
        print(f"Arrows: {self.arrow}")

# ---------------------------

class GunMan(Hero):
    def __init__(self, name, strength, agility, gun, bullets):
        super().__init__(name, strength, agility, magic=0)
        self.gun = gun
        self.bullets = bullets

    def shoot_bullet(self):
        if self.bullets > 0:
            print(f"{self.name} shoots a bullet!")
            self.bullets -= 1
        else:
            print(f"{self.name} has no bullets left!")

    def buy_bullet(self, bullets):
        self.bullets += bullets
        print(f"{self.name} has bought {bullets} bullets! Total bullets: {self.bullets}")

    def change_gun(self, new_gun):
        self.gun = new_gun
        print(f"{self.name} has changed their gun to {self.gun}!")

    def display_stats(self):
        super().display_stats()
        print(f"Gun: {self.gun}, Bullets: {self.bullets}")


def start_battle(hero_obj):
    hero_obj.battle_cry()
    hero_obj.display_stats()
    hero_obj.equip_weapon()
    hero_obj.train()
    hero_obj.heal()

heroes = [Knight("Arjun", 10, 8, 5, "Steel Armor"), Mage("Gandalf", 8, 6, 10, 50), Archer("Eklavya", 7, 10, 5), GunMan("Rambo", 9, 7, "AK-47", 30)]
for hero in heroes:
    start_battle(hero)# New line for better readability
