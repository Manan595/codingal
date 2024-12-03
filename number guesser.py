import random
playing = True 
number = str (random.randint(10,20))

print("I will generate a number from 10 to 20 and you have to guess the number ")
print("The game ends when you get 1 hero!")

while playing:
    guess= input("give me your best guess and win the game")
    if number == guess:
        print("you win the game ")
        print("the number was", number)
        break
    else:
        print("your guess is wrong try again ")

