# This program selects a random number between 1 to 10 and lets the user know if they guessed right
import random
number = random.randrange(1, 10)
user_numb = input ('Enter a number between 1 and 10 \n')
counter = 0
while user_numb != number:
    user_numb = int(user_numb)
    # check if user number is greater than random number
    if user_numb > number:
        print('Too high, try again')
        counter += 1
        user_numb = input('Enter a number between 1 and 10 \n')
    elif user_numb == number:
        counter += 1
        break
    else:
        print('Too low, try again')
        counter += 1
        user_numb = input('Enter a number between 1 and 10 \n')

print(f'Correct! you guess right in {counter} tries')