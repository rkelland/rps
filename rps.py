# A simple text based Rock Paper Scissor Emulator
# rkelland@gmail.com

import random


while 1==1:
    computer = (random.randint(0,2))

    if computer == 0:
        computer_choice = 'rock'
    elif computer == 1:
        computer_choice = 'paper'
    else:
        computer_choice = 'scissor'

    user_choice = raw_input("Enter rock, paper, or scissor:\n")

    print ('computer chose: ' + computer_choice)

    if computer_choice == user_choice:
        print('TIE')
    elif user_choice == 'rock' and computer_choice=='scissor':
        print('WIN')
    elif user_choice =='paper' and computer_choice=='rock':
        print('WIN')
    elif user_choice == 'scissor' and computer_choice=='paper':
        print('WIN')
    else:
        print('You lose :( Computer wins :D')
raw_input("press any key to start again.")
