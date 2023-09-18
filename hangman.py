import random
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"
# List of words for the game
word_list = ["python", "developer", "hangman", "coding", "challenge"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to initialize the game
def initialize_game():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # Number of allowed attempts

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    return word_to_guess, guessed_letters, attempts

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to play the game
def play_hangman():
    word_to_guess, guessed_letters, attempts = initialize_game()

    while attempts > 0:
        print("\nAttempts left:", attempts)
        current_display = display_word(word_to_guess, guessed_letters)
        print("Current word:", current_display)

        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
               
                print(YELLOW + "You already guessed that letter." + RESET)
            elif guess in word_to_guess:
                guessed_letters.append(guess)
               
                print(GREEN + "Letter in guess word." + RESET)
                if set(word_to_guess) == set(guessed_letters):
                    print("Congratulations! You guessed the word:", word_to_guess)
                    break
            else:
                guessed_letters.append(guess)
        
                print(RED + "Letter not in guess word" + RESET)
                attempts -= 1
        else:
            print("Please enter a single letter.")

    if attempts == 0:
        print("\nOut of attempts. The word was:", word_to_guess)

# Main function to start the game
if __name__ == "__main__":
    play_hangman()
