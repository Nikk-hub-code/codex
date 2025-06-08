import random
plyr_name = input("Enter you name= ")
print(f"""
    Hii {plyr_name}!!

    Welcome to Number Guess Game.

    Guess the number between 0 and 100.
""")
chances = 0
target_number = random.randint(0,100)
while chances < 6:
    plyr_guess = int(input("Guess a number= "))
    if plyr_guess >=0 and plyr_guess <= 100:
        if plyr_guess > target_number:
            print("Ohhoo.... That's greater then the actual number.")
        elif plyr_guess < target_number:
            print("Ohh no.... That's smaller then the actual number.")
        elif target_number == plyr_guess:
            print(f"Congratulations {plyr_name}!! You got it correct.")
        else:
            print("Oops!! You got it wrong.")
        chances += 1
    else:
        print("Invalid Number....")