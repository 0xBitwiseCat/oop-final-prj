from GameManager import GameManager


def main_menu():
    print(f"********************")
    print(f"*Power Grid Master!*")
    print(f"********************")
    print("")
    print("1. New Game")
    print("2. Exit")

    print('Enter your option [1-2]:')
    return int(input())

def bye():
    print("Thanks for playing!")
    print("Good bye")
    print("")

def select_difficulty():
    print(f"**********************")
    print(f"Select the difficulty:")
    print(f"**********************")
    print("")
    print("1. EASY")
    print("2. NORMAL")
    print("3. HARD")
    print("4. INSANE")
    print("5. ADMIN")
    print("")
    print('Enter your option [1-5]:')
    return int(input())

difficulties = ["EASY", "NORMAL", "HARD", "INSANE", "ADMIN"]
while(True):
    # let's play !
    option = main_menu()
    if option != 1:
        bye()
        break

    difficulty = select_difficulty()
    if difficulty < 1 or difficulty > 5:
        difficulty = 2
    game_manager = GameManager(difficulties[difficulty-1])


