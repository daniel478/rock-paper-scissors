import random
import os

BEATS = {'ROCK': 'SCISSORS', 'PAPER': 'ROCK', 'SCISSORS': 'PAPER'}
GAME_OPTIONS = list(BEATS.keys())

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_player_choice() -> str:
    while True:
        player_choice = input("\nRock, Paper or Scissors: ").upper()
        
        if player_choice in BEATS:
            return player_choice
        else:
            print("Invalid option!! Choose again")

def get_computer_choice() -> str:
    return random.choice(GAME_OPTIONS)

def determine_winner(player, computer):
    if player == computer:
        return "DRAW"
    elif BEATS[player] == computer:
        return "WIN"
    else:
        return "LOSS"

def scoreboard(scores: dict):
    print("=" * 80)
    print("SCOREBOARD")
    print()
    print(f"Wins: {scores['WIN']}")
    print(f"Losses: {scores['LOSS']}")
    print(f"Draws: {scores['DRAW']}")
    print()
    print(f"Win ratio: {scores['win_ratio']:.2f}%")
    print("=" * 80)

def play_game():

    score = {
        "WIN": 0,
        "LOSS": 0,
        "DRAW": 0,
        "games_played": 0,
        "win_ratio": 0
    }

    while True:
        print("=" * 80)
        print("ROCK - PAPER - SCISSORS")
        print("=" * 80)

        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        result = determine_winner(player_choice, computer_choice)
        score[result] += 1
        score["games_played"] += 1
        
        try:
            score["win_ratio"] = (score["WIN"] / score["games_played"]) * 100
        except ZeroDivisionError:
            score["win_ratio"] = 0


        print()
        print("=" * 80)
        print(f"GAME RESULT: {result}")
        print("=" * 80)

        print("=" * 80)
        print(f"Player: {player_choice}")
        print(f"Computer: {computer_choice}")
        print("=" * 80)

        scoreboard(score)

        while True:
            continue_choice = input("Play again (Y/N): ").upper()
            if continue_choice == "N": return
            elif continue_choice == "Y": break
            else: print("Invalid option!! Choose again")
        
        clear_screen()

if __name__ == "__main__":
    play_game()