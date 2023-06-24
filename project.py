import random
import os
import re

def check_play_status():
    valid_responses =['yes','no']
    while True:
        try:
            response = input('Do you wish to play again?(Yes or No):')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')
            if response.lower() == 'yes':
                return True
            else:
                os.system('cls'if os.name=='nt'else'clear')
                print("Thanks for playing!")
                exit()
        except ValueError as err:
            print(err)
#------------------------------------------------------------------------------

def play_rps():
    play =True
    while play:
        os.system('cls'if os.name=='nt'else'clear')
        print('')
        print('Rock,paper,scissors - Shoot!')

        user_choice = input('Choose Your Weapon'
                            '[R]ock,[P]aper, or [S]cissors')
        if not re.match("[SsRrPp]",user_choice):
            print("Please Choose a letter:")
            print('[R]ock,[P]aper, or [S]cissors')
            continue
        print(f'I choose: {user_choice}')

        choice = ['R','P','S']
        opp_choice=random.choice(choice)

        print(f'AI choose: {opp_choice}')

#-----------------------------------------------------------------------------
        if opp_choice==user_choice.upper():
            print("Tie!")
            play=check_play_status()
        elif opp_choice=='R' and user_choice.upper()=='S':
            print("Rock beats Scissors, AI wins")
            play=check_play_status()
        elif opp_choice=='S' and user_choice.upper()=='P':
            print("Scissors beats Paper, AI wins")
            play=check_play_status()
        elif opp_choice=='P' and user_choice.upper()=='R':
            print("Paper beats Rock, AI wins")
            play=check_play_status()
        else:
            print("Human Win!\n")
            play=check_play_status()

#------------------------------------------------------------------------------------

if __name__ == '__main__':
    play_rps()
