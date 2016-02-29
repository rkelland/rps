# A simple text based Rock Paper Scissor Emulator
# rkelland@gmail.com

import random
win_count=0

while 1==1:
	user_choice = raw_input("Enter rock, paper, or scissor:\n")
	computer = (random.randint(0,2))
	if computer == 0:
		computer_choice = 'rock'
	elif computer == 1:
		computer_choice = 'paper'
	else:
		computer_choice = 'scissor'

	print ('computer chose: ' + computer_choice)

	if computer_choice == user_choice:
		print('TIE')
	elif user_choice == 'rock' and computer_choice=='scissor':
		win_count+=1
		print('WINNER!\n\tyou have won ' + str(win_count)+ ' times.')
	elif user_choice =='paper' and computer_choice=='rock':
		win_count+=1
		print('WINNER!\n\tyou have won ' + str(win_count)+ ' times.')
	elif user_choice == 'scissor' and computer_choice=='paper':
		win_count+=1
		print('WINNER!\n\tyou have won ' + str(win_count)+ ' times.')
	else:
		print('Sorry you lost.\n\tyou have won ' + str(win_count)+ ' times.')
raw_input("press any key to start again.")
