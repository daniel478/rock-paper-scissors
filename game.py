import random

def get_player_choice(options: list) -> str:
    while True:
        player_choice = input("\nRock, Paper or Scissors: ").upper()
        
        if player_choice in options:
            return player_choice
        else:
            print("Invalid option!! Choose again")

def get_computer_choice(options: list) -> str:
    return random.choice(options)

def determine_winner(player, computer, rules):
    if player == computer:
        return "Draw!!"
    elif rules[player] == computer:
        return "Win!!"
    else:
        return "Loss!!"

def play_game():
    beats = {'ROCK': 'SCISSORS', 'PAPER': 'ROCK', 'SCISSORS': 'PAPER'}
    game_options = list(beats.keys())

    print("=" * 80)
    print("ROCK - PAPER - SCISSORS")
    print("=" * 80)

    player_choice = get_player_choice(game_options)
    computer_choice = get_computer_choice(game_options)
    
    result = determine_winner(player_choice, computer_choice, beats)

    print()
    print("=" * 80)
    print(f"GAME RESULT: {result}")
    print("=" * 80)

    print("=" * 80)
    print(f"Player: {player_choice}")
    print(f"Computer: {computer_choice}")
    print("=" * 80)

if __name__ == "__main__":
    play_game()