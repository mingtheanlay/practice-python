def get_interger():
    user_choice = int(input('Input a number: '))
    return user_choice

def deteminer(number):
    if number == 1:
        return 'Not Prime'
    elif number == 2:
        return 'Prime'
    else:
        for i in range (2,number):
            if number % i == 0:
                return 'Not Prime'
        return 'Prime'

choice = get_interger()
print(deteminer(choice))
        
        