import random

beats = {'ROCK': 'SCISSORS', 'PAPER': 'ROCK', 'SCISSORS': 'PAPER'}
game_options = list(beats.keys())

print("=" * 80)
print("ROCK - PAPER - SCISSORS")
print("=" * 80)

while True:
    player_choice = input("\nRock, Paper or Scissors: ").upper()
    
    if player_choice in game_options:
        break
    else:
        print("Invalid option!! Choose again")

comp_choice = random.choice(game_options)

if player_choice == comp_choice:
    print("\nDraw!!")
elif beats[player_choice] == comp_choice:
    print("\nYou Win!!")
else:
    print("\nYou Lose!!")

print(f"\nPlayer: {player_choice}")
print(f"Computer: {comp_choice}")