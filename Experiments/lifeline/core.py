setup = input('\n M A I N   M E N U\n'+
             ' new | load | help ')
if setup == 'new':
    username = input('\nMy nickname is ')
elif setup == 'load':
    # load = input('L O A D\nThe game file is called: ')
    with open('stats.txt','r') as save:
        lines = save.readlines()

active = True
while active:
    main = input('\n H O M E\n'+
                 ' new | load | help ')
