from numpy import random

class dungeon():
    def __init__(self):
        self.warrior_attack_level = 50
        self.warrior_energy = 100
        self.attack_bonus = 0
        self.sidekick_bonus = 0
        self.monster_life = 0
        self.race = ''
        self.sidekick_name = ''
        self.mystic_name = ''
        self.warrior_name= ''
        self.monster_selected = ''
        
    def warrior_action(self,attack,defense,sneak,fireball_cost,beard_cost,snow_cost):
        chosen_attack = input('Choose an attack: 1-fireball, 2-beardslap, or 3-snowstorm')
        if chosen_attack == '1':
            attack_type = 'fireball'
            if self.monster_selected == 'Metal Dragon':
                self.attack_bonus = 15
                print('Super effective against Metal Dragon!')
            else:
                self.attack_bonus = 10
            self.warrior_energy = self.warrior_energy - fireball_cost
        elif chosen_attack == '2':
            attack_type = 'beard slap'
            if self.monster_selected == 'Hairy Spider':
                self.attack_bonus = 3
                print('Super effective against Hairy Spider!')
            else:
                self.attack_bonus = 1
            self.warrior_energy = self.warrior_energy - beard_cost
        elif chosen_attack == '3':
            attack_type = 'snow storm'
            if self.monster_selected == 'Hairy Spider':
                self.attack_bonus = 10
                print('Has little effect on Hairy Spider!')
            else:
                self.attack_bonus = 20
            self.warrior_energy = self.warrior_energy - snow_cost
        else:
            attack_type = 'your attack failed!'
            self.attack_bonus = 0
            self.warrior_energy = self.warrior_energy - 10
        attack_total = attack + self.attack_bonus + self.sidekick_bonus
        print(f'{self.warrior_name} is a {self.race} and uses a {attack_type} with {attack_total} attack effect.')
        return attack, attack_type
    
    def monster_generator(self,monster_rng):
        if monster_rng == 1: 
            self.monster_selected = 'Metal Dragon'
            self.monster_life = 2000
        if monster_rng == 2:
            self.monster_selected = 'Stone Golem'
            self.monster_life = 1750
        if monster_rng == 3:
            self.monster_selected = 'Hairy Spider'
            self.monster_life = 1500
    
    def mystic(self,energy):
        self.warrior_energy = self.warrior_energy + energy
        print(f'The beautiful mystic, {self.mystic_name}, has given you {energy} energy!!!')
        
    def sidekick(self,bonus):
        if bonus == 5 or bonus == 10:
            self.sidekick_bonus =  25
            print(f'{self.sidekick_name}, the wonder sidekick, has given you an attack bonus of {self.sidekick_bonus}')
        else:
            print(f'{self.sidekick_name} finds you annoying and decides not to help...')
            
    def monster_action(self,attack,defense):
        print(f'{self.monster_selected} has a defense of {defense}')
        return defense
    
    def battle(self,monster_defense, warrior_attack):
        
        warrior_attack_with_bonus = warrior_attack + self.attack_bonus + self.sidekick_bonus
        if monster_defense < warrior_attack_with_bonus:
            self.warrior_attack_level = self.warrior_attack_level + 1
            self.monster_life = self.monster_life - warrior_attack_with_bonus
            print(f'{self.monster_selected} has been wounded and has {self.monster_life} life points left!')
            print(f'{self.warrior_name} has a new attack skill level of {self.warrior_attack_level}')
        else: 
            print('{self.warrior_name} attack failed!') 
            self.warrior_attack_level = self.warrior_attack_level - 1
            print(f'{self.warrior_name} has a new attack skill level of {self.warrior_attack_level}')
            
        print(f'{self.warrior_name} has {self.warrior_energy} energy left!')


Mossy_Dungeon = dungeon()

# monster generated
monster_gen = random.randint(1,4, size=(1))
Mossy_Dungeon.monster_generator(monster_gen)

# Dungeon Settings
print('WELCOME TO THE MOSSY DUNGEON!!')
Mossy_Dungeon.warrior_name = input('What is your name?')
Mossy_Dungeon.race = input('What are you (race)?')
Mossy_Dungeon.sidekick_name = input('Enter Sidekick Name: ')
Mossy_Dungeon.mystic_name = input('Enter Mystic Name:')
print(f'Watchout here comes the {Mossy_Dungeon.monster_selected}, prepare for battle! Defeat the dragon before running out of energy!')
print('Learn about your attacks below:')
print(f'Fireball (6-10 energy cost): Was a secret knowledge only known to the sun god. The knowledge was stolen by a wizard tribe in 1200BC and is now taught and practiced by all races. \n'
            f'Beardslap (0-3 energy cost): Discovered by the longest beard record holder, when he accidently dismembered his pet snake when he turned around to quickly and struck the poor creature on the head \n'
            f'Snowstorm (5-25 energy cost): After suffering severe frostbite some races have their DNA infused with ice crystals that they can summon as a massive snowstorm at great expense of energy and soul')
i = 0

while Mossy_Dungeon.warrior_energy > 0 and Mossy_Dungeon.warrior_attack_level > 0 and Mossy_Dungeon.monster_life > 0:
    
    #RNG
    warrior_attack = random.randint(0,Mossy_Dungeon.warrior_attack_level+1, size=(1))
    monster_defense = random.randint(0,51, size=(1))
    fireball_cost = random.randint(6,11, size=(1))
    beard_cost = random.randint(3,6, size=(1))
    snow_cost = random.randint(5,26, size=(1))
    heal = random.randint(0,2, size=(1))
    sidekick_help = random.randint(0,10, size=(1))
    
    #SIM ACTIONS
    Mossy_Dungeon.sidekick(sidekick_help)
    luis_wizard = Mossy_Dungeon.warrior_action(warrior_attack, 2, 10,fireball_cost,beard_cost,snow_cost)
    monster = Mossy_Dungeon.monster_action(1,monster_defense)
    Mossy_Dungeon.battle(monster,luis_wizard[0])
    Mossy_Dungeon.mystic(heal)
    i = i + 1
    print('-----------------------------------------------')
    print(f'Attack run #{i}')
    
if Mossy_Dungeon.warrior_energy <= 0 or Mossy_Dungeon.warrior_attack_level <= 0:
    score = (Mossy_Dungeon.warrior_attack_level*.75) + (Mossy_Dungeon.warrior_energy*.25)
    print(f'The warrior has passed out with a final attack level of {Mossy_Dungeon.warrior_attack_level} after {i} attack runs!')
    print(f'Your score is {score}')
elif Mossy_Dungeon.monster_life <= 0:
    score = (Mossy_Dungeon.warrior_attack_level*.75) + (Mossy_Dungeon.warrior_energy*.25)
    print(f'You have defeated the monster and scored {score}! Collect your treasure and leave the dungeon!')


        