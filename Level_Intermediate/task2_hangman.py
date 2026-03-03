import random

# 1. Visual Progress: ASCII Art for the Hangman stages
HANGMAN_PICS = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

# 2. Expanded Words and Hints Dictionary
WORDS_AND_HINTS = {
    # Original Words
    "python": "A popular programming language named after a snake.",
    "developer": "Someone who writes code to build software.",
    "internship": "A temporary position to gain real-world experience.",
    "shadowfox": "The name of the company you are interning at!",
    "variable": "A container for storing data values in code.",
    
    # Python Specific Concepts
    "dictionary": "A data structure that stores key-value pairs.",
    "boolean": "A data type that can only be True or False.",
    "string": "A sequence of characters enclosed in quotes.",
    "integer": "A whole number without a fractional part.",
    "tuple": "An immutable data collection in Python.",
    "function": "A reusable block of code that performs a specific task.",
    
    # General Programming & Computer Science
    "algorithm": "A step-by-step set of instructions to solve a problem.",
    "debugging": "The process of finding and fixing errors in code.",
    "syntax": "The spelling and grammar rules of a programming language.",
    "loop": "A programming construct that repeats a sequence of instructions.",
    "iteration": "A single pass through a set of operations or a loop.",
    "compiler": "A program that translates source code into machine code.",
    "exception": "An event that occurs during execution that disrupts normal flow.",
    
    # Web & Developer Tools
    "github": "A web-based platform used for version control and collaboration.",
    "repository": "A central location where code and files are stored and managed.",
    "terminal": "A text-based interface used to interact with the operating system.",
    "framework": "A foundation with pre-built code to help develop software faster.",
    "frontend": "The part of a website or app that users interact with directly.",
    "backend": "The server side of an application where logic and databases reside.",
    "database": "An organized collection of data, typically stored electronically.",
    "api": "A set of rules allowing different software applications to communicate."
}

def play_hangman():
    print("Welcome to Hangman: ShadowFox Edition!")
    
    # Pick a random word and its hint
    word, hint = random.choice(list(WORDS_AND_HINTS.items()))
    word = word.upper()
    
    guessed_letters = set()
    incorrect_guesses = 0
    max_guesses = len(HANGMAN_PICS) - 1
    
    while incorrect_guesses < max_guesses:
        # Display the visual progress
        print(HANGMAN_PICS[incorrect_guesses])
        
        # Display the current state of the word (e.g., P _ T _ O N)
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print(f"\nWord: {display_word}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Win condition check
        if "_" not in display_word:
            print(f"\n🎉 Congratulations! You guessed the word: {word}")
            return

        # Player Input
        guess = input("\nGuess a letter (or type '?' for a hint): ").upper()
        
        # Hint logic
        if guess == '?':
            print(f"\n💡 HINT: {hint}")
            continue
            
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("\n⚠️ Invalid input. Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("\n⚠️ You already guessed that letter. Try again!")
            continue
            
        # Process the guess
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"\n✅ Good job! '{guess}' is in the word.")
        else:
            print(f"\n❌ Wrong guess! '{guess}' is not in the word.")
            incorrect_guesses += 1
            
    # Loss condition check (Loop ends)
    print(HANGMAN_PICS[-1])
    print(f"\n💀 Game Over! You've been hung. The word was: {word}")

# --- Main Execution ---
if __name__ == "__main__":
    while True:
        play_hangman()
        play_again = input("\nDo you want to play again? (Y/N): ").upper()
        if play_again != 'Y':
            print("Thanks for playing! Goodbye.")
            break