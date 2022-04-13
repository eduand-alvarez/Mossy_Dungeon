import streamlit as st
from numpy import random
from mossy_dungeon import dungeon
from PIL import Image


@st.cache
def load_image(path):
    image = Image.open(path)
    return image


image = load_image(r'C:\Users\eduan\Documents\MD_banner.png')
st.image(image)

# instantiate dungeon
my_dungeon = dungeon()
# monster generated
monster_gen = random.randint(1, 4, size=1)
my_dungeon.monster_generator(monster_gen)
st.caption(f'Watch-out here comes the {my_dungeon.monster_selected}, prepare for battle! Defeat the monster '
           f'before running out of energy!')

left, middle, right = st.columns(3)

with left:
    st.subheader('Build the Dungeon')
    my_dungeon.warrior_name = st.text_input('What is your name?')
    my_dungeon.race = st.text_input('What is your race?')
    my_dungeon.mystic_name = st.text_input('Who is your mystic?')
    my_dungeon.sidekick_name = st.text_input('Who is your sidekick?')

with middle:
    st.subheader('Select an Attack')
    fireball = st.button('Fireball', key='fb', help='Fireball (6-10 energy cost): Was a secret knowledge only known '
                                                    'to the sun god. The knowledge was stolen by a wizard tribe in'
                                                    ' 1200BC and is now taught and practiced by all races.')
    wind_vortex = st.button('Wind Vortex', key='bs', help='Wind Vortex (3-5 energy cost): Warriors discovered this '
                                                          'unique power that allowed to create powerful storms that '
                                                          'cause damage to objects and creatures in its path.')
    lightning_strike = st.button('Lighting Strike', key='sb',
                                 help='Lighting Strike (5-25 energy cost): After suffering lighting strikes '
                                      'some races have their DNA infused with mutated electrons that they '
                                      'use to summon devastating lighting strikes, at great expense of energy '
                                      'and soul')

    if fireball:
        attack_chosen = 'fireball'
        st.image(
            'https://th.bing.com/th/id/R.56992d737cb4c73a0756cb13e79035b6?rik=%2f9pWrY2SniWWOg&riu=http%3a%2f%2ffc08.deviantart.net%2ffs71%2ff%2f2013%2f139%2f7%2fe%2ffireball_fx_2d_animation_test_by_bat_19-d65jxxv.gif&ehk=tHiYoVLA%2f0JoU%2fCPca0wElYwq%2bo51j5CAYABBXIPNa0%3d&risl=&pid=ImgRaw&r=0')
    elif wind_vortex:
        attack_chosen = 'wind vortex'
        st.image('https://media.tenor.com/images/458946ad99370f637ca389df7dd3f17a/tenor.gif')
    elif lightning_strike:
        attack_chosen = 'lightning strike'
        st.image('https://media.giphy.com/media/MSQvCAEwBr5XG/giphy.gif')

    if fireball and my_dungeon.monster_selected == 'Metal Dragon':
        st.info('Super Effective Against Metal Dragon!')
    elif wind_vortex and my_dungeon.monster_selected == 'Hairy Spider':
        st.info('Additional Bonus Against Hairy Spider')
    elif lightning_strike and my_dungeon.monster_selected == 'Hairy Spider':
        st.info('Hairy Spider has Special Resistance!')

with right:
    st.subheader('Results of Attack Run')

    try:
        while my_dungeon.warrior_energy > 0 and my_dungeon.warrior_attack_level > 0 and my_dungeon.monster_life > 0:
            # st.info(f'Starting Attack run #{i}')
            # RNG
            warrior_attack = random.randint(0, my_dungeon.warrior_attack_level + 1, size=1)
            monster_defense = random.randint(0, 51, size=1)
            fireball_cost = random.randint(6, 11, size=1)
            wind_vortex = random.randint(3, 6, size=1)
            lightning_cost = random.randint(5, 26, size=1)
            heal = random.randint(0, 2, size=1)
            sidekick_help = random.randint(0, 10, size=1)

            # SIM ACTIONS
            my_dungeon.sidekick(sidekick_help)
            luis_wizard = my_dungeon.warrior_action(warrior_attack, attack_chosen, fireball_cost, wind_vortex,
                                                    lightning_cost)
            monster = my_dungeon.monster_action(1, monster_defense)
            my_dungeon.battle(monster, luis_wizard[0])
            my_dungeon.mystic(heal)
            i = i + 1
    except:
        st.error('Choose an attack!')

    if my_dungeon.warrior_energy <= 0 or my_dungeon.warrior_attack_level <= 0:
        score = (my_dungeon.warrior_attack_level * .75) + (my_dungeon.warrior_energy * .25)
        st.write(
            f'The warrior has passed out with a final attack level of {my_dungeon.warrior_attack_level} after {i} attack runs!')
        st.write(f'Your score is {score}')
    elif my_dungeon.monster_life <= 0:
        score = (my_dungeon.warrior_attack_level * .75) + (my_dungeon.warrior_energy * .25)
        st.balloons()
        st.write(f'You have defeated the monster and scored {score}! Collect your treasure and leave the dungeon!')
