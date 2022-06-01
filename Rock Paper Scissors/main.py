from random import choice

# R: Rock, P: Paper, S: Scissors
options = ['R', 'P', 'S']
playerScore = 0
cpuScore = 0

def runGame():
    while True:
        player = input('Pick either R, P or S or enter Q to end the Game: ').upper()
        cpu = choice(options)

        global playerScore
        global cpuScore

        if(player == 'Q'):
            print('You ended the game ')
            print('Scores: ')
            print(f'Player ( {playerScore} ) : CPU ( {cpuScore} ) ')
            if(playerScore > cpuScore):
                print('Player Won - Congrats!! ')
            elif playerScore < cpuScore:
                print('CPU Won - Congrats!! ')
            else:
                print('It was a tie! ')
                print('No one won :(')
            break
        elif player == cpu:
            print(f'Player ( {player} ) : CPU ( {cpu} ) ')
            print("It's a tie! ... Choose again ")
        elif player == 'R':
            if cpu == 'P':
                print(f'Player ( {player} ) : CPU ( {cpu} ) ')
                print(f'Paper ({cpu}) beats Rock ({player}). CPU Wins !! ')
                cpuScore += 1
            else:
                print(f'Player ( {player} ) : CPU ( {cpu} ) ')
                print(f'Rock ({player}) beats Scissors ({cpu}). Player Wins !! ')
                playerScore += 1
        elif player == 'P':
            if cpu == 'S':
                print(f'Player ( {player} ) : CPU ( {cpu} ) ')
                print(f'Scissors ({cpu}) beats Paper ({player}). CPU Wins !! ')
                cpuScore += 1
            else:
                print(f'Player ( {player} ) : CPU ( {cpu} ) ')
                print(f'Paper ({player}) beats Rock ({cpu}). Player Wins !! ')
                playerScore += 1
        elif player == 'S':
            if cpu == 'P':
                print(f'Player ( {player} ) : CPU ( {cpu} ) ')
                print(f'Rock  ({cpu}) beats Scissors ({player}). CPU Wins !! ')
                cpuScore += 1
            else:
                print(f'Player ( {player} ) : CPU ( {cpu} ) ')
                print(f'Scissors ({player}) beats Paper ({cpu}). Player Wins !! ')
                playerScore += 1
        else:
            print('The chosen character is not in the options. Please try again! ')

# Run the game function
runGame()




