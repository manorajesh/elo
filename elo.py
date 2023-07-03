import math

class Player:
    def __init__(self, name, rating, K):
        self.name = name
        self.rating = rating
        self.K = K

    def __repr__(self):
        return f"{self.name} ({self.rating})"

# Get file with games
with open("games.txt") as f:
    games = f.readlines()

games = [game.split()[2] for game in games]

player1 = Player("Player 1", 1200, 20)
player2 = Player("Player 2", 1200, 20)

for game in games:
    # Calculate the expected score for each player
    player1_expected = 1 / (1 + math.pow(10, (player2.rating - player1.rating) / 400))
    player2_expected = 1 / (1 + math.pow(10, (player1.rating - player2.rating) / 400))

    match game:
        case "1-0":
            player1_actual = 1
            player2_actual = 0
        case "0-1":
            player1_actual = 0
            player2_actual = 1
        case "1-1":
            player1_actual = 0.5
            player2_actual = 0.5
        case _:
            raise ValueError("Unknown game result: " + game)

    # Calculate the rating changes for each player
    player1_change = player1.K * (player1_actual - player1_expected)
    player2_change = player2.K * (player2_actual - player2_expected)

    # Update the ratings for each player
    player1.rating += player1_change
    player2.rating += player2_change

# Print the new ratings
print(player1)
print(player2)
