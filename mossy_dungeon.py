from numpy import random
import streamlit as st


class dungeon:

    def __init__(self):
        self.warrior_attack_level = 50
        self.warrior_energy = 100
        self.attack_bonus = 0
        self.sidekick_bonus = 0
        self.monster_life = 0
        self.race = ''
        self.sidekick_name = ''
        self.mystic_name = ''
        self.warrior_name = ''
        self.monster_selected = ''

    def warrior_action(self, attack, chosen_attack, fireball_cost, beard_cost, snow_cost):
        if chosen_attack == 'fireball':
            attack_type = 'fireball'
            if self.monster_selected == 'Metal Dragon':
                self.attack_bonus = 15
            else:
                self.attack_bonus = 10
            self.warrior_energy = self.warrior_energy - fireball_cost
        elif chosen_attack == 'wind vortex':
            attack_type = 'wind vortex'
            if self.monster_selected == 'Hairy Spider':
                self.attack_bonus = 3
            else:
                self.attack_bonus = 1
            self.warrior_energy = self.warrior_energy - beard_cost
        elif chosen_attack == 'lightning strike':
            attack_type = 'lightning strike'
            if self.monster_selected == 'Hairy Spider':
                self.attack_bonus = 10
            else:
                self.attack_bonus = 20
            self.warrior_energy = self.warrior_energy - snow_cost
        else:
            attack_type = 'your attack failed!'
            self.attack_bonus = 0
            self.warrior_energy = self.warrior_energy - 10
        attack_total = attack + self.attack_bonus + self.sidekick_bonus
        st.info(f'You used {attack_type} with {attack_total} attack effect.')
        return attack, attack_type


    def monster_generator(self, monster_rng):
        if monster_rng == 1:
            self.monster_selected = 'Metal Dragon'
            self.monster_life = 2000
        if monster_rng == 2:
            self.monster_selected = 'Stone Golem'
            self.monster_life = 1750
        if monster_rng == 3:
            self.monster_selected = 'Hairy Spider'
            self.monster_life = 1500

    def mystic(self, energy):
        self.warrior_energy = self.warrior_energy + energy
        st.success(f'The beautiful mystic, {self.mystic_name}, has given you {energy} energy!!!')

    def sidekick(self, bonus):
        if bonus == 5 or bonus == 10:
            self.sidekick_bonus = 25
            st.success(
                f'{self.sidekick_name}, the wonder sidekick, has given you an attack bonus of {self.sidekick_bonus}')
        else:
            st.warning(f'{self.sidekick_name} finds you annoying and decides not to help...')

    def monster_action(self, attack, defense):
        st.info(f'{self.monster_selected} has a defense of {defense}')
        return defense

    def battle(self, monster_defense, warrior_attack):

        warrior_attack_with_bonus = warrior_attack + self.attack_bonus + self.sidekick_bonus
        if monster_defense < warrior_attack_with_bonus:
            self.warrior_attack_level = self.warrior_attack_level + 1
            self.monster_life = self.monster_life - warrior_attack_with_bonus
            st.success(f'{self.monster_selected} has been wounded and has {self.monster_life} life points left!')
            st.success(f'{self.warrior_name} has a new attack skill level of {self.warrior_attack_level}')
        else:
            st.warning(f'{self.warrior_name} attack failed!')
            self.warrior_attack_level = self.warrior_attack_level - 1
            st.error(f'{self.warrior_name} has a new attack skill level of {self.warrior_attack_level}')

        st.info(f'{self.warrior_name} has {self.warrior_energy} energy left!')
