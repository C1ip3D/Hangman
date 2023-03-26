import random


words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]


word = random.choice(words)


hidden_word = ["_"] * len(word)


guesses_left = 6


while guesses_left > 0 and "_" in hidden_word:

    print(" ".join(hidden_word))
    print("Guesses left:", guesses_left)


    guess = input("Guess a letter: ").lower()


    if guess in word:

        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        print("Correct!")
    else:
        guesses_left -= 1
        print("Wrong!")


if "_" not in hidden_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Sorry, you ran out of guesses. The word was:", word)
