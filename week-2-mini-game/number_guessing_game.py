import random


def play_game():

    secret_number = random.randint(1, 10)

    max_essais = 4
    compteur = 0


    while max_essais > compteur:
        compteur += 1
        guess = int(input("Guess the number between 1 and 10 : "))

        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print(f"You won in {compteur} attempt(s)! 🎉")
            return True

    print(f"Oh no ! You have lost ! The secret number was {secret_number}.")
    return False


def ask_play_again():
    answer = input("Would you like to play again? (yes/no): ").strip().lower()
    return answer == "yes"

def main():
    games_played = 0
    games_won = 0

    print("****************************************************************************************************************")
    print("*                                                                                                              *")
    print("*                                      Welcome on my first game !                                              *")
    print("*                                                                                                              *")
    print("****************************************************************************************************************")
    print("Your goal is to find the good number with only 4 attemps ! Good luck !", "\n")

    playing = True

    while playing:
        games_played += 1 

        if play_game():
            games_won += 1
        
        playing = ask_play_again()

    print("\nGame over !")
    print(f"Games played : {games_played}")
    print(f"Games won : {games_won}")

if __name__ == "__main__":
    main()