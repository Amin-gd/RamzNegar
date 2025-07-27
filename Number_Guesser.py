import random
adad = random.randint(1, 100)

print('Welcome to Number Guesser '
      '\nYou have 10 Chances to guess the number '
      '\nSend a number between 1 and 100 to play the game: ')

s = 10
while s > 0:
    i = input()
    if not i.isdigit():
        print("Error! "
              "\nPlease send a valid number:")
        continue
    i = int(i)
    if i > 100 or i < 1:
        print('Please send me a number between 1 and 100')
        continue
    if i == adad:
        print('You Won!')
        print('Your score is', s)
        break
    if i > adad:
        print('Your number is bigger')
    if i < adad:
        print('Your number is smaller')
    s -= 1

if s == 0:
    print("You lost!"
          " \nThe number was:", adad)


