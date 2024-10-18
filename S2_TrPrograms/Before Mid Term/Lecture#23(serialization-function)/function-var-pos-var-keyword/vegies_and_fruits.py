import random

def guess_the_word(word, attempts):
    print("Welcome to the guess game!")
    print("Try to guess the word.")

    for i in range(attempts):
        guess = input("Enter your guess: ").lower()
        if guess == word:
            print("Congratulations! You guessed the word.")
            return
        print(f"Wrong guess! {attempts - i - 1} attempts left.")

    print(f"Sorry, you ran out of attempts. The correct word was '{word}'.")

def main():
    category = input("Choose a category (1. Fruits, 2. Vegetables): ").strip()

    if category == "1":
        words = ["apple", "banana", "orange", "grape", "kiwi"]
        print("This is the fruits category. The word is related to fruits.")
    elif category == "2":
        words = ["carrot", "broccoli", "tomato", "cucumber", "potato"]
        print("This is the vegetables category. The word is related to vegetables.")
    else:
        print("Invalid choice. Exiting.")
        return

    word = random.choice(words)
    attempts = int(input("Enter the number of attempts (default is 3): ") or 3)

    #function call
    guess_the_word(word, attempts)

'''
if __name__ == "__main__":
    main()
'''
main()
