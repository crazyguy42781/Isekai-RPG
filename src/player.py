import random as rnd
import time
import sys


class Players:
    """This class holds all the player information."""

    def __init__(self):
        self.p_name = ""
        # Current level so far lvl 100 is the highest obtainable
        self.lvl = 1
        # Player Experience. When the player hits the thresh hold
        # they will level up. to get to level 100 is 329240xp with
        # the current progression levels
        self.XP = 0
        self.maxXP = 10
        # Job title of the player.
        # Magician, Warrior, Archer
        self.job = ['Magician', 'Warrior', 'Archer', '?']
        # classes
        self.p_class = rnd.randint(0, 0)
        # Health
        self.HPh = 10
        self.maxHP = 10
        # Mana for Magician class
        self.MPh = 10
        self.maxMP = 10
        # Energy for Warrior and Archer class
        self.ENh = 10
        self.maxEN = 10
        # Stats
        self.Energy = 0
        self.Strength = 0
        self.Intellect = 0
        self.Agility = 0
        self.Accuracy = 0
        self.Luck = 0
        # Unassigned points that allow you to boost your stats through the game
        self.usp = 0
        # Calls the attribute function to give your player stats for its class
        self.set_stats()
        # skills for each class
        self.skills = {}
        self.get_skills()
        # difficulty
        self.difficulty = 0
        # players current location
        self.main_location = 2
        self.location = 'Home'
        self.text = 0.05

    def display_info(self) -> None:
        print_speed(f"Level: {self.lvl}   XP: {int(self.XP):,}/{int(self.maxXP):,}")
        print_speed(f"Job: {self.job[self.p_class]} Class: {self.p_class}")
        for k, v in self.skills[self.job[self.p_class]].items():
            if v['name'] != "":
                print_speed(f"    Skill: {v['name']}")
        print_speed(f"Health Power: {self.HPh}/{self.maxHP}")
        if self.p_class == 0:
            print_speed(f"Mana Power: {self.MPh}/{self.maxMP}")
        elif self.p_class in [1, 2]:
            print_speed(f"Energy: {self.ENh}/{self.maxEN}")
        print_speed(f"Strength: {self.Strength}")
        print_speed(f"Intellect: {self.Intellect}")
        print_speed(f"Agility: {self.Agility}")
        print_speed(f"Accuracy: {self.Accuracy}")
        print_speed(f"Luck: {self.Luck}")
        print_speed(f"Unassigned Stat Points: {self.usp}")
        return

    def unassigned_points(self) -> None:
        while self.usp > 0:
            print_speed(f'You have {self.usp} points to spend')
            user_input = str(input('Would you like to spend your points (Yes, No)? '))
            if user_input.lower() not in ['yes', 'no', 'n', 'y']:
                print_speed('Incorrect answer. Please try again')
            elif user_input.lower() in ['no', 'n']:
                print_speed('No Points Spent')
                break
            else:
                more = True
                while self.usp > 0 and more == True:
                    print_speed(f'You have {self.usp} Points to use.')
                    print_speed('Which category do you want to assign your points?')
                    print_speed('(S)trength')
                    print_speed('(I)ntellect')
                    print_speed('(A)gility')
                    print_speed('S(t)amina')
                    print_speed('(L)uck')
                    user_input = str(input('Insert: '))
                    if user_input.lower() not in ['s', 'i', 'a', 't', 'l']:
                        print_speed('Incorrect answer. Please try again')
                    else:
                        while True:
                            a_input = int(input('How many points do you want to assign? '))
                            if a_input > self.usp:
                                print_speed(
                                    'Sorry you can not spend more points than you currently have. Please try again.')
                            elif a_input < 0:
                                print_speed('Sorry you cannot spend less than 1 point.')
                            else:
                                break
                        if user_input.lower() == 's':
                            self.Strength += a_input
                        elif user_input.lower() == 'i':
                            self.Intellect += a_input
                        elif user_input.lower() == 'a':
                            self.Agility += a_input
                        elif user_input.lower() == 't':
                            self.Accuracy += a_input
                        elif user_input.lower() == 'l':
                            self.Luck += a_input
                        self.usp -= a_input
                    if self.usp > 0:
                        wrong_answer = True
                        print_speed(f'You have {self.usp} points left to spend')
                        while wrong_answer == True:
                            user_input = str(input('Would you like to spend more points (Yes, No)? '))
                            if user_input.lower() not in ['yes', 'no', 'n', 'y']:
                                print_speed('Incorrect answer. Please try again')
                                wrong_answer = True
                            elif user_input.lower() in ['no', 'n']:
                                print_speed('No Points Spent')
                                more = False
                                wrong_answer = False
                                break
                            else:
                                wrong_answer = False
        return

    def level_up(self) -> None:
        """This function is to level up the character"""
        while self.XP >= self.maxXP:
            # XP leveling section
            self.XP -= self.maxXP
            self.maxXP += self.level_progression()
            self.maxXP = self.maxXP
            self.lvl += 1
            # Healing power
            self.maxHP += 10
            self.maxMP += 10
        return

    def level_progression(self) -> float:
        if 0 < self.lvl <= 10:
            return 25
        elif 10 < self.lvl <= 20:
            return 50
        elif 20 < self.lvl < 50:
            return 75
        elif 50 < self.lvl < 75:
            return 100
        elif 75 < self.lvl < 100:
            return 125
        return 25

    def set_stats(self) -> None:
        if self.p_class == 0:
            self.Strength = rnd.randint(7, 11)
            self.Intellect = rnd.randint(12, 16)
            self.Agility = rnd.randint(8, 12)
            self.Accuracy = rnd.randint(12, 16)
            self.Luck = rnd.randint(8, 12)
            self.usp = rnd.randint(1, 3)
        elif self.p_class == 1:
            self.Strength = rnd.randint(12, 16)
            self.Intellect = rnd.randint(7, 11)
            self.Agility = rnd.randint(8, 12)
            self.Accuracy = rnd.randint(8, 12)
            self.Luck = rnd.randint(12, 16)
            self.usp = rnd.randint(1, 3)
        elif self.p_class == 2:
            self.Strength = rnd.randint(8, 12)
            self.Intellect = rnd.randint(8, 12)
            self.Agility = rnd.randint(12, 16)
            self.Accuracy = rnd.randint(7, 11)
            self.Luck = rnd.randint(12, 16)
            self.usp = rnd.randint(1, 3)
        return

    def get_skills(self) -> None:
        # ['Magician', 'Warrior', 'Archer', '?']
        self.skills['Magician'] = {
            'Fireball': {'name': 'Fireball', 'mana': 2, 'attack': '2*intellect on 1 enemy'},
            'Heal': {'name': 'Heal', 'mana': 3, 'attack': 'heal yourself for 50 HP'},
            'Electrocute': {'name': 'Electrocute', 'mana': 3, 'attack': '1*intellect to all creatures'},
            'Hit': {'name': 'Hit', 'mana': 0, 'attack': '1*strength on 1 enemy'},
            'Special': {'name': '', 'mana': 0, 'attack': ''}}
        self.skills['Warrior'] = {
            'Pierce': {'name': 'Pierce', 'mana': 2, 'attack': '2*strength on max 3 enemies'},
            'Slice': {'name': 'Slice', 'mana': 3, 'attack': '4*strength on one enemy'},
            'Strengthen': {'name': 'Strengthen', 'mana': 4, 'attack': 'augment your shield by 50 for 3 turns'},
            'Hit': {'name': 'Hit', 'mana': 0, 'attack': '1*strength on 1 enemy'},
            'Special': {'name': '', 'mana': 0, 'attack': ''}}
        self.skills['Archer'] = {}
        """elif c_num == 3:
            return ", Watershot (5 mana, 3*intelligence on 1 creature)"
        else:
            return "?"
        """
        return

    def rest(self):
        self.HP = self.maxHP
        self.MP = self.maxMP
        # self.ENh=self.maxENh
        print_speed("You are sleeping")
        return

    def rank(self) -> str:
        if self.lvl < 11:
            guild_id = "F"
        elif 10 < self.lvl < 21:
            guild_id = "E"
        elif 20 < self.lvl < 31:
            guild_id = "D"
        elif 30 < self.lvl < 41:
            guild_id = "C"
        elif 40 < self.lvl < 51:
            guild_id = "B"
        elif 50 < self.lvl < 61:
            guild_id = "A"
        elif 60 < self.lvl < 71:
            guild_id = "S"
        elif 70 < self.lvl < 81:
            guild_id = "SS"
        elif 80 < self.lvl:
            guild_id = "SSS"
        return guild_id


p = Players()


def print_speed(input_str):
    for letter in input_str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(p.text)
    print()