# import random package for generating random numbers
import random

# Creating one function to defined range of random number
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    # taking user input for number of players
    players = input("Enter number of players (2-4): ")

    # checking entered input is integer or not
    if players.isdigit():
        players = int(players)

        # check the entered input in between given range
        if 2 <= players <= 4:
            break
        else:
            print("players must be in between (2-4)")

    else:
        print("Invalid, try agin")

# defining one variable to reach that score
max_score = 50
# declare initial score 0 of each player
players_score = [0 for i in range(players)]

while max(players_score) < max_score:

    for player_index in range(players):
        print("\n player number", player_index+1, "turn has just started")
        # declare for counting the score
        current_score = 0

        print("your total score is: ", players_score[player_index])

        while True:
            roll_dice = input("Would you like to roll (y) ? : ").lower().strip()
            # if user not entered "y/Y" then break statement execute
            if roll_dice != "y":
                break

            value = roll()
            # when roll generate 1 number that following thing happen
            if value == 1:
                print("You rolled a 1!, your turn Done..")
                current_score = 0
                break
            else:
                # counting the score
                current_score += value
                print("You rolled a :", value)

            print("Your score is: ", current_score)
        # counting score of each particluar index of player
        players_score[player_index] += current_score
        print("Your total score is: ", players_score[player_index])
# validate the score of players who will win
max_score = max(players_score)
win = players_score.index(max_score)
print("Player number", win+1, "is the winner with a score of : ", max_score)