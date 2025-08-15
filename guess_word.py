import random
player = input("Enter your name= ").upper()
print(f"""Hii {player}!!

        Press Enter to start the game...
""")
start = input("> ")
if start == '':
    a=['tree','hello','welcome','hazel','peak','encyclopedia']
    random_words = random.choice(a)
    word_length = len(random_words)
    print(f"The word contain {word_length} alphabets.")
    word_char = list(random_words)
    user_input = ''
    jumbled_words = []
    for attempt in range(0,6):
        user_input = input("> ")
        t = 0
        for alphabet in word_char:
            if user_input == random_words:
                print(f"""Congratulations {player}!! You guess the correct word.""")
                exit()
            elif user_input == alphabet:                
                print(f"The '{user_input}' is in a word.")
                t = 1
                jumbled_words.append(alphabet)
                break
        if (t == 0):
            print("Sorry!! You guess it wrong.")
        print(f"{5 - attempt} attempts left.")
        print(f"Alphabet you got are {jumbled_words}")
        user_input = ''