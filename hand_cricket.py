import random
from optimus import optimus_compare as opticmp

toss_choice = (input('Choose Odd or Even :')).capitalize()

computer_input = random.randint(1,11)
while True:
    try:
        player_input = int(input('Enter a number for toss :'))
        assert 0 <= player_input < 11
    except ValueError:
        print("Not an integer! Please enter an integer.")
    except AssertionError:
        print("Please enter an integer from 1 to 10")
    else:
        break

print(f'Comp : {computer_input}')
print(f'player : {player_input}')

b_b = ['Batting','Bowling']
state = ""
if toss_choice == 'Even':
    if ((int(computer_input) + int(player_input))%2 == 0):
        print('You WON the TOSS !!')
        state = input('Do you want to Batt or Bowl (Batting or Bowling):')
    else:
        comp = random.choice(b_b)
        if comp == 'Batting':
            print(f'The Computer WON the TOSS and chose {comp}')
            state = 'Bowling'
        elif comp == 'Bowling':
            print(f'The Computer WON the TOSS and chose {comp}')
            state = 'Batting'

        
if toss_choice == 'Odd':
    if ((int(computer_input) + int(player_input))%2 == 1):
        print('You WON the TOSS !!')
        state = (input('Do you want to Batt or Bowl (Batting or Bowling):'))
        state.capitalize()
    else:
        comp = random.choice(b_b)
        if comp == 'Batting':
            print(f'The Computer WON the TOSS and chose {comp}')
            state = 'Bowling'
        elif comp == 'Bowling':
            print(f'The Computer WON the TOSS and chose {comp}')
            state = 'Batting'

print(f'player : {state}')

score = 0
target = 1
innings = 1

def unoptimized_game_handling():
    global state, score, innings, target

    while True:
        while True:
            try:
                player_num = int(input(f'You are {state} and its innings {innings}. Enter the number :'))
                assert 0 <= player_num < 11
            except ValueError:
                print("Not an integer! Please enter an integer.")
            except AssertionError:
                print("Please enter an integer from 1 to 10")
            else:
                break

        computer_num = random.randint(1,11)

        if (player_num == computer_num):
            if (state == 'Batting' and innings == 1):
                state = 'Bowling'
                innings = 2
                print('Achooooo! You are out. Go defend your target')
                print(f'Your score is {score}')
            elif (state == 'Bowling' and innings == 1):
                state = 'Batting'
                innings = 2
                print(f'Hurray!! The computer is out. Chase your Target..')
                print(f'You should hit {target}')
            elif (state == 'Batting' and innings == 2):
                print('Computer Won the match')
                return
            elif  (state == 'Bowling' and innings == 2):
                print('You Won the match')
                return
            else:
                break

        else:
            if (state == 'Batting' and innings == 1):
                score += player_num
                print(f'Your score for now {score}')
            elif (state == 'Bowling' and innings == 1):
                target += computer_num
                print(f"The computer's score for now {target - 1}")
            elif (state == 'Batting' and innings == 2):
                if(target - player_num > 0):
                    target -= player_num
                    print(f'You should hit more {target} runs')
                    pass
                else:
                    print('you won the match')
                    return
            elif (state == 'Bowling' and innings == 2):
                if(score - player_num > 0):
                    score -= computer_num
                    print(f'You have {score} more runs to defend.')
                    pass
                else:
                    print('Computer won the match')
                    return
            else:
                break


def optimized_game_handling():
    global state, score, innings, target

    while True:
        while True:
            try:
                player_num = int(input(f'You are {state} and its innings {innings}. Enter the number :'))
                assert 0 <= player_num < 11
            except ValueError:
                print("Not an integer! Please enter an integer.")
            except AssertionError:
                print("Please enter an integer from 1 to 10")
            else:
                break

        computer_num = random.randint(1,11)

        if (player_num == computer_num):
            match state:
                case "Batting":
                    if innings == 1:
                        state = 'Bowling'
                        innings = 2
                        print('Achooooo! You are out. Go defend your target')
                        print(f'Your score is {score}')

                    else:
                        print('Computer Won the match')
                        return

                case "Bowling":
                    if innings == 1:
                        state = 'Batting'
                        innings = 2
                        print(f'Hurray!! The computer is out. Chase your Target..')
                        print(f'You should hit {target}')

                    else:
                        print('You Won the match')
                        return

                case _:
                    break

        else:
            match state:
                case "Batting":
                    if innings == 1:
                        score += player_num
                        print(f'Your score for now {score}')

                    else:
                        if(target - player_num > 0):
                            target -= player_num
                            print(f'You should hit more {target} runs')
                            pass
                        else:
                            print('you won the match')
                            return
                        
                case "Bowling":
                    if innings == 1:
                        target += computer_num
                        print(f"The computer's score for now {target - 1}")

                    else:
                        if(score - player_num > 0):
                            score -= computer_num
                            print(f'You have {score} more runs to defend.')
                            pass
                        else:
                            print('Computer won the match')
                            return

                case _:
                    break

print()
opticmp('unoptimized_game_handling', 'optimized_game_handling', iterations = 1, multiplier = 1, verbose = True)
print()

