import random
number = random.randint(1,100)
while True:
    guess = int (input("guess the number (between 1 and 100);"))
    if guess < number:
        print("too low ")
    elif guess > number:
        print("too high")
    else:
        print ("you guessed it right", number)
        break