import random


class Creatures:
    """This class is for all the creatures. It holds all info of the
    creatures. Creates the party for the attacks."""

    def __init__(self):
        # random number between 3 and 6 creatures for a party
        self.num_cs = 0
        self.num_c()
        # c_names holds a dict of all the creatures
        self.c_names = {}
        # c_names_list holds the creatures names to make the party
        self.c_names_list = []
        self.name_list()
        # creating the party with random creatures per level
        self.fight_creatures = self.fight_party()

    def num_c(self) -> None:
        self.num_cs = random.randint(3, 6)
        return

    def fight_party(self, level=1) -> dict:
        temp_n = {}
        if self.c_names == {}:
            self.creature_name()
        for i in range(self.num_cs):
            temp_n[i] = self.c_names[self.creature_group(level)]
        return temp_n

    def creature_name(self) -> None:
        self.c_names = {'goblin': {'name': 'goblin', 'hp': 20, 'attackpower': 1, 'class': 'general'},
                        'hobgoblin': {'name': 'hobgoblin', 'hp': 50, 'attackpower': 1, 'class': 'general'},
                        'slime': {'name': 'slime', 'hp': 10, 'attackpower': 1, 'class': 'general'},
                        'zombie': {'name': 'zombie', 'hp': 40, 'attackpower': 1, 'class': 'general'},
                        'kobolds': {'name': 'kobolds', 'hp': 75, 'attackpower': 1, 'class': 'general'},
                        'ghost': {'name': 'ghost', 'hp': 75, 'attackpower': 1, 'class': 'general'},
                        'goblinking': {'name': 'goblinking', 'hp': 200, 'attackpower': 1, 'class': 'general'},
                        'spider': {'name': 'spider', 'hp': 100, 'attackpower': 1, 'class': 'general'},
                        'wolf': {'name': 'wolf', 'hp': 150, 'attackpower': 1, 'class': 'general'},
                        'skeletonsoldier': {'name': 'skeletonsoldier', 'hp': 50, 'attackpower': 1, 'class': 'general'},
                        'skeletonknight': {'name': 'skeletonknight', 'hp': 250, 'attacakpower': 1, 'class': 'general'},
                        'ghoul': {'name': 'ghoul', 'hp': 250, 'attackpower': 1, 'class': 'general'},
                        'spiderqueen': {'name': 'spiderqueen', 'hp': 500, 'attackpower': 1, 'class': 'general'},
                        'orc': {'name': 'orc', 'hp': 400, 'attackpower': 1, 'class': 'general'},
                        'beastman': {'name': 'beatman', 'hp': 500, 'attackpower': 1, 'class': 'general'},
                        'basilisk': {'name': 'baskilisk', 'hp': 500, 'attackpower': 1, 'class': 'general'},
                        'centipede': {'name': 'centipede', 'hp': 600, 'attackpower': 1, 'class': 'general'},
                        'centaur': {'name': 'centaur', 'hp': 650, 'attackpower': 1, 'class': 'general'},
                        'satyr': {'name': 'satyr', 'hp': 800, 'attackpower': 1, 'class': 'general'},
                        'earthelemental': {'name': 'earthelemental', 'hp': 750, 'attackpower': 1, 'class': 'general'},
                        'fireelemental': {'name': 'fireelemental', 'hp': 750, 'attackpower': 1, 'class': 'general'},
                        'waterelemental': {'name': 'waterelemental', 'hp': 750, 'attackpower': 1, 'class': 'general'},
                        'windelemental': {'name': 'windelemental', 'hp': 750, 'attackpower': 1, 'class': 'general'},
                        'fusedelemental': {'name': 'fusedelemental', 'hp': 1250, 'attackpower': 1, 'class': 'general'},
                        'fairy': {'name': 'fairy', 'hp': 1000, 'attackpower': 1, 'class': 'general'},
                        'elf': {'name': 'elf', 'hp': 1500, 'attackpower': 1, 'class': 'general'},
                        'dwarf': {'name': 'dwarf', 'hp': 1750, 'attackpower': 1, 'class': 'general'},
                        'darkknight': {'name': 'darkknight', 'hp': 2000, 'attackpower': 1, 'class': 'general'},
                        'darkmage': {'name': 'darkmage', 'hp': 2500, 'attackpower': 1, 'class': 'general'},
                        'skeletondragon': {'name': 'skeletondragon', 'hp': 3000, 'attackpower': 1, 'class': 'general'},
                        'golem': {'name': 'golem', 'hp': 10000, 'attackpower': 1, 'class': 'general'},
                        'minotaur': {'name': 'minotaur', 'hp': 10000, 'attackpower': 1, 'class': 'general'},
                        'demonlackey': {'name': 'demonlackey', 'hp': 12500, 'attackpower': 1, 'class': 'general'},
                        'werewolf': {'name': 'werewolf', 'hp': 12500, 'attackpower': 1, 'class': 'general'},
                        'succubi': {'name': 'succubi', 'hp': 15000, 'attackpower': 1, 'class': 'general'},
                        'kraken': {'name': 'kraken', 'hp': 15000, 'attackpower': 1, 'class': 'general'},
                        'manticore': {'name': 'manticore', 'hp': 16000, 'attackpower': 1, 'class': 'general'},
                        'darkelf': {'name': 'darkelf', 'hp': 15000, 'attackpower': 1, 'class': 'general'},
                        'wyvern': {'name': 'wyvern', 'hp': 16000, 'attackpower': 1, 'class': 'general'},
                        'troll': {'name': 'troll', 'hp': 15500, 'attackpower': 1, 'class': 'general'},
                        'phoenix': {'name': 'phoenix', 'hp': 19000, 'attackpower': 1, 'class': 'general'},
                        'lich': {'name': 'lich', 'hp': 17500, 'attackpower': 1, 'class': 'general'},
                        'vampire': {'name': 'vampire', 'hp': 20000, 'attackpower': 1, 'class': 'general'},
                        'giant': {'name': 'giant', 'hp': 25000, 'attackpower': 1, 'class': 'general'},
                        'chimera': {'name': 'chimera', 'hp': 30000, 'attackpower': 1, 'class': 'general'},
                        'dragon': {'name': 'dragon', 'hp': 50000, 'attackpower': 1, 'class': 'general'},
                        'demonlord': {'name': 'demonlord', 'hp': 100000, 'attackpower': 1, 'class': 'general'}}

    def name_list(self):
        self.c_names_list = ['goblin', 'hobgoblin', 'slime', 'zombie', 'kobolds', 'ghost',
                             'goblinking', 'spider', 'wolf', 'skeletonsoldier', 'skeletonknight',
                             'ghoul', 'spiderqueen', 'orc',  'beastman', 'basilisk', 'centipede',
                             'centaur', 'satyr', 'earthelemental', 'fireelemental', 'waterelemental',
                             'windelemental', 'fusedelemtneal', 'fairy', 'elf', 'dwarf', 'darkknight',
                             'darkmage', 'skeletondragon', 'golem', 'minotaur', 'demonlackey',
                             'werewolf', 'succubi', 'kraken', 'manticore', 'darkelf', 'wyvern',
                             'troll', 'phoenix', 'lich', 'vampire', 'giant', 'chimera',
                             'dragon', 'demonlord']
        return

    def creature_group(self, level=1) -> str:
        l, h = 0, 0
        if 0 < level <= 10:
            l, h = 0, 4
        elif 10 < level <= 20:
            l, h = 4, 9
        elif 20 < level <= 30:
            l, h = 9, 14
        elif 30 < level <= 40:
            l, h = 14, 19
        elif 40 < level <= 50:
            l, h = 19, 24
        elif 50 < level <= 60:
            l, h = 24, 29
        elif 60 < level <= 70:
            l, h = 29, 34
        elif 70 < level <= 80:
            l, h = 34, 39
        elif 80 < level <= 90:
            l, h = 39, 44
        elif 90 < level <= 100:
            l, h = 40, 46
        return self.c_names_list[random.randint(l, h)]