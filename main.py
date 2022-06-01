# # # # # # # # # # # # # # # # # # # # # # # #
#                                             #
#   Rock Paper Scissors Game - Zuri Training  #
#                                             #
#   @author Allwell Onen                      #
#   Wednesday, 1st June 2022                  #
#                                             #
# # # # # # # # # # # # # # # # # # # # # # # #

from time import sleep
import random


rock = """
    _____
___/  ___)
     (____)
     (____)
__   (____)
  \__(__)
"""

paper = """
    ____
___/  __)___
        ____)
       ______)
__   ______)
  \______)
"""

scissors = """
    ____
___/  __)___
        ____)
       ______)
__   (___)
  \__(__)
"""

draw = """
# # # # # # # # # # # # # #
#                         #
#       ITS A DRAW!       #
#                         #
# # # # # # # # # # # # # #
"""

win = """
# # # # # # # # # # # # # #
#                         #
#        YOU  WIN!        #
#                         #
# # # # # # # # # # # # # #
"""

loose = """
# # # # # # # # # # # # # #
#                         #
#        YOU LOOSE!       #
#                         #
# # # # # # # # # # # # # #
"""


options = ['r', 'p', 's'] # options for only the bot
bot = random.choice(options)
player1 = 'CPU'
game_started = True
game_data = {'r': {'option': 'Rock', 'number': 0, 'image': rock}, 'p': {'option': 'Paper', 'number': 1, 'image': paper}, 's': {'option': 'Scissors', 'number': 2, 'image': scissors}}

def getOption(player_option):
    return game_data[player_option]['option']

def getImage(player_option):
    return game_data[player_option]['image']


# start game
print('Rock Paper Scissors Game\n')
player2 = input('Enter your name: ')
print(player1 + ' vs ' + player2 + '(You)')

while(game_started):
    print('\nGame Menu')
    print('"R" for Rock')
    print('"P" for Paper')
    print('"S" for Scissors\n')

    # get user input and convert it to lowercase character
    user = input('Choose: ')
    user = user.lower()

    if user != 'r' and user != 'p' and user != 's':
        print('Invalid option\nTry again.!')
        continue

    sleep(0.9)
    print(f'\nYou: {getOption(user)} {getImage(user)}')

    sleep(1.5)
    print(f'\nCPU: {getOption(bot)} {getImage(bot)}')
    sleep(0.3)

    # game logic/condition for user to win
    user_wins = ((user == 'r') and (bot == 's')) or ((user == 'p') and (bot == 'r')) or ((user == 's') and (bot == 'p'))

    # game login/condition for bot to win
    bot_wins = ((bot == 'r') and (user == 's')) or ((bot == 'p') and (user == 'r')) or ((bot == 's') and (user == 'p'))

    if (getOption(user) == getOption(bot)):
        print(draw)
        print('Pick again!')
        continue

    elif user_wins:
        print(win)
        game_started = False

    elif bot_wins:
        print(loose)
        game_started = False

    else:
        print('Invalid option!')
        continue
