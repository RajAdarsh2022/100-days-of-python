import random

# Initializing the game and providing instructions
print("Welcome to Hangman !")
print("You have 7 lives in total, so guess correctly")
print("All the Best !")
print("*******************************************************")

word_list = ["aardvark", "baboon", "camel"]
life_count = 7
isTerminate = False

# Randomly choosing a word from the word_list
chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
word_till_now = ['_'] * chosen_word_length

while not isTerminate:
    # Asking the user to guess a letter and making guess lowercase.
    guess = input("Enter your guess: ")
    letter = guess.lower()

    # Checking if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == letter:
                word_till_now[i] = letter
        if ''.join(word_till_now) == chosen_word:
            break
        else:
            print("Your guess was correct.")
            print(f"The word till now is {' '.join(word_till_now)}")
    else:
        # One life goes away
        life_count -= 1
        print(f"Oops, You guessed incorrectly! You have {life_count} chances remaining.")

        if life_count == 0:
            isTerminate = True

if isTerminate:
    print("Sorry you lost!")
else:
    print("Congratulations! You Won !!!")
    print(f"The word was {chosen_word}")


    