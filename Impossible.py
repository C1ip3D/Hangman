import random


words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "testimony", "sesquipedalian", "phenomenon", "onomatopoeia", "supercalifragilisticexpialidocious", "worcestershire" 'imbe', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine']


word = random.choice(words)


hidden_word = ["_"] * len(word)


guesses_left = 2


while guesses_left > 0 and "_" in hidden_word:

    print(" ".join(hidden_word))
    print("Guesses left:", guesses_left)


    guess = input("Guess a letter or the word directly: ").lower()


    if guess == word:
        hidden_word = list(word)
    else:
        # Check if the letter is in the word
        if guess in word:
            # Update the hidden word with the correct letter
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
            print("Correct!")
        else:
            # Reduce the number of guesses left
            guesses_left -= 1
            print("Wrong!")

# Print the outcome of the game
if "_" not in hidden_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Sorry, you ran out of guesses. The word was:", word)
