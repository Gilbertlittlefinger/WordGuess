"""
WordGuess game implementation.

@author xt0fer
@version 1.0.0
@date 5/27/21 11:02 AM
"""
#add a way to import more random words focusing on the theme of programming languages, data structures, and algorithms. I will also add a way to keep track of the user's score and allow them to play multiple rounds of the game.
import random
import person

class WordGuess:
    """WordGuess game class - ready for implementation."""
    def __init__(self):
        self.words = ["python", "java", "Sqlscript", "javascript", "ruby", "csharp", "cryptography", "algorithm", "data", "structure"]
        self.selected_word = random.choice(self.words)
        self.guessed_letters = set()
        self.max_attempts = 6
        self.attempts = 0
        pass
    def play(self):
        while True:
            pass
            guess = input("Welcome to Word Guess! Guess a letter: ").lower()
            if guess in self.selected_word:
                self.guessed_letters.add(guess)
                print(f"Good guess! {guess} is in the word.")
            elif guess in self.guessed_letters:
                print(f"You've already guessed {guess}. Try a different letter.")
                continue
            else:
                self.attempts += 1
                print(f"Wrong guess! {guess} is not in the word. Attempts left: {self.max_attempts - self.attempts}")
            if self.attempts >= self.max_attempts:
                print(f"Game over! The word was: {self.selected_word}")
                break

          # Check if the player has guessed all letters in the word
            if all(letter in self.guessed_letters for letter in self.selected_word):
                print(f"Congratulations! You've guessed the word: {self.selected_word}")
                break
            
            
            if self.attempts == 3:
                print("Hint: The word is related to programming languages, data structures, and algorithms.")
            elif self.attempts == 5:
                print("Hint: The word starts with the letter '{}'.".format(self.selected_word[0]))
            if len(self.guessed_letters) >= 3:
                full_guess = input("Do you want to guess the entire word? (y/n): ").lower()
                if full_guess == "y":
                    word_guess = input("Enter your guess for the word: ").lower()
                    if word_guess == self.selected_word:
                        print(f"Congratulations! You've guessed the word: {self.selected_word}")
                        break
                    else:
                        self.attempts += 1
                        print(f"Wrong guess! {word_guess} is not the word. Attempts left: {self.max_attempts - self.attempts}")
                        if self.attempts >= self.max_attempts:
                            print(f"Game over! The word was: {self.selected_word}")
                            break
        user_input = input("Do you want to play again? (y/n): ").lower()
        if user_input == "y":
            self.__init__()  # Reset the game state
            self.play()  # Start a new game
        else:
            print("Thanks for playing! Goodbye!")

            
    




def main():
    game = WordGuess()
    game.play()


if __name__ == "__main__":
        main()
