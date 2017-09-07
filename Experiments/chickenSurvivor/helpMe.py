#------ HELP AND TIPS ------
def home():
    print('This is your home.\nHere you will have four options:\n'+
          'The first, \"help\", brings up this text of information.\n'+
          'The second, \"stats\", shows you facts and current statistics.\n'+
          'For example: how much money you have, the value of your eggs\n'+
          'It is recommended to check this out!\n'+
          'The third, \"market\", is where you sell eggs, buy items and get paid.\n'+
          'The fourth, \"sleep\", starts the night, survive 15 nights and you win.')

def stats():
    print('')

def market():
    print('This is the market.\nHere you will have four options:\n'+
          'The first, \"buy\" lets you buy an item.'+
          'The second, \"sell\" lets you sell your eggs. OBS! If you have over\n'+
          'ten eggs, you have a chance to get a new chicken. Also, the value for an egg\n'+
          'changes every day.'+
          'The third, \"help\", prints out this text document.'+
          'The fourth, \"leave\", returns you home.')

'''
Defense and the attack will be compared to determine the outcome during nighttime
All three attributes are prone to be insuffficient the player's defence.
Certain actions might be overcome a weakness of the new fox, resulting in a win.
The less chickens, the less money you earn during the preparation stage.
On the other side, the more chickens you lose; the more enraged you become.
The enraged factor is will be added to your sum of defense as a helping hand'''
