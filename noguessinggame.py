import random
sn=random.randint(1,100)
gn=int(input("Guess a number between 1 to 100 : "))
while gn!=sn:
    if gn<sn:
        print("Your guess is too low. :(")
    else:
        print("Your guess is too high. :(")
    gn=int(input("Guess s number between 1 to 100 : "))
print("Congratulations! you guessed the number correctly. :)")
        
