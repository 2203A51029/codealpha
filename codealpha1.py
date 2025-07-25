import random

# Small list of predefined words
word_list = ["apple", "tiger", "house", "pizza", "chair"]

# Randomly choose a word from the list
word_to_guess = random.choice(word_list)
guessed_word = ["_"] * len(word_to_guess)
guessed_letters = []
max_attempts = 6
wrong_guesses = 0

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))

while wrong_guesses < max_attempts and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                guessed_word[i] = guess
        print("Good job! Current word:", " ".join(guessed_word))
    else:
        wrong_guesses += 1
        print(f"Wrong guess! You have {max_attempts - wrong_guesses} guesses left.")

# Final result
if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("❌ Game over! The word was:", word_to_guess)