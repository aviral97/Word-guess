import random
word_list = ['python', 'java', 'kotlin', 'javascript']
choice = random.choice(word_list)
hint = list("-" * len(choice))
lives = 8
wletter = []
print("H A N G M A N")
inp = input('Type "play" to play the game, "exit" to quit:')
if inp == "play":
    while lives > 0:
        print()
        print(''.join(hint))
        letter = input("Input a letter:")
        if letter == "-":
            print("Please enter a lowercase English letter")
            continue

        if letter in hint or letter in wletter:
            print("You've already guessed this letter")
            continue
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if letter.islower() == False:
            print("Please enter a lowercase English letter")
            continue

        for i in range(len(choice)):
            if letter == choice[i]:
                hint[i] = letter
        if letter not in choice:
            wletter.append(letter)
            print("That letter doesn't appear in the word")

            lives -= 1

        if "-" not in hint:
            print("You guessed the word!")
            if lives >= 0:
                print("You survived!")
            break
    else:
        print("You lost!")
