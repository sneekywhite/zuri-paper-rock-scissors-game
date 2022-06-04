from operator import truediv
import random

#user choice
# user choice include (R-rock, P-paper, S-scissors)
while True:
    user_take = str(input("kindly input your choice: ").upper())

#computer choice
    comp_pick = random.randint(1,3)
    if comp_pick == 1:
        comp_pick = 'R'
    elif comp_pick ==2:
        comp_pick = 'P'
    else:
       comp_pick = 'S'

    print(f"\nYou choose {user_take}, computer choose {comp_pick}. \n")


##function to play
    if user_take == comp_pick:
        print("tie, You both select same!")
    elif user_take == 'R' and comp_pick == 'P':
        print('You loose, computer select paper!')
    elif user_take == 'R' and comp_pick == 'S':  
        print('You win, computer select scissors!')
    elif user_take == 'P' and comp_pick == 'S':
        print('You lost,computer select scissors!')
    elif user_take == 'P' and comp_pick == 'R':
        print('You lost, computer select rock!')
    elif user_take == 'S' and comp_pick == 'R':
        print('You lost, computer select rock!')
    elif user_take == 'S' and comp_pick == 'P':
        print('You win, computer select paper!')
    else:
        print('invalid: choose any one -- rock, paper, scissors')
    
    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        break







