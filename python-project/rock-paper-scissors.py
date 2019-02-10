import random
list = ['rock','paper','scissors']

def compare(cop,player):
    if cop == player:
        return ('draw')
    elif cop == 'rock':
        if player == 'paper':
            return ('player win')
        else:
            return ('cop win')
    elif cop == 'paper':
        if player == 'scissors':
            return ('player win')
        else:
            return ('cop win')
    elif cop == 'scissors':
        if player == 'rock':
            return ('player win')
        else:
            return ('cop win')    

while True:
    random.shuffle(list)
    cop = list[0]
    player = input('Your input: ')
    print('Cop:',cop)
    print(compare(cop,player))
    print('Press A to play again')
    print('Press anything to quit')
    user_choice = input("Input your choice:")
    if user_choice in ['A','a']:
        print('-'*30)
        continue
    else:
        break