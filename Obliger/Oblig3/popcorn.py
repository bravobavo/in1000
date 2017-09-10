#En liste som skal kunne poppe en verdi utfra en if/else statement, samt legge til verdier.
complete = []
popping = True
while popping:
    answer = input("\nMichael Jackson is the king of ")
    if answer == "pop" or answer == "Pop":
        complete.append(answer)
        answer2 = input("\nAnd what goes along with pop? ")
        if answer2 == "corn" or answer2 == "Corn":
            complete.append(answer2)
            print(str(complete))
            answer3 = input("\nAnd what do we like to pop? ")
            if answer3 == "corn":
                complete.pop(1)
                print('\nThat\'s right!')
            elif answer3 == "pop":
                complete.pop(0)
                print('uhm... yes..\n')
            else:
                print('uhm...')
            print(complete)
    else:
        print("No you silly goose!")
