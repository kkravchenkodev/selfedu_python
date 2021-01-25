import random

print('Hello. What is you name?')
name = input()

print(f'Well, {name}, I am thinking of a number between 1 and 20')
secret_number = random.randint(1, 20)

print(f'DEBUG: Secret number is {secret_number}')

for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break  # This condition is for the correct guess

if guess == secret_number:
    print(f'Good job, {name}! You guessed my number in {guesses_taken} guess')
else:
    print(f'Nope. The number I was thinking of was {secret_number}')
