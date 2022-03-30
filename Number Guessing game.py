import random
guessTaken = 0
    
def distance():
    if guess == number -10:
        print("You are not far away!")

    if guess == number -9:
        print("You are not far away!")

    if guess == number -8:
        print("You are not far away!")

    if guess == number -7:
        print("You are not far away!")

    if guess == number -6:
        print("You are not far away!")

    if guess == number -5:
        print("You are not far away!")

    if guess == number -4:
        print("You are not far away!")

    if guess == number -3:
        print("You are not far away!")
        
    if guess == number -2:
        print("You are not far away!")

    if guess == number -1:
        print("You are not far away!")

    return

def distance2():
    if guess == number +10:
        print("You are not far away!")

    if guess == number +9:
        print("You are not far away!")

    if guess == number +8:
        print("You are not far away!")

    if guess == number +7:
        print("You are not far away!")

    if guess == number +6:
        print("You are not far away!")

    if guess == number +5:
        print("You are not far away!")

    if guess == number +4:
        print("You are not far away!")

    if guess == number +3:
        print("You are not far away!")
        
    if guess == number +2:
        print("You are not far away!")

    if guess == number +1:
        print("You are not far away!")

    return

print("Hello! What is your name?")
Name = input()

number = 50
print("Well, " + Name + ", I am thinking of a number between 1 and 100")



for guessTaken in range(10):
    print("Take a guess")
    guess = int(input())

    distance()

    if guess < number:
        print("Your guess is too low!")

    distance2()

    if guess > number:
        print("Your guess is too high!")

    if guess == number:
        break


if guess == number:
    guessTaken = str(guessTaken + 1)
    print("Good job! ," + Name + "! You guessed the number in " + guessTaken + " guesses!")

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number + '.')