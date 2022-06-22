# def rps(p1,p2):
#     if p1 == "scissors" and p2 == "paper" or  p1 == "rock" and p2 == "scissors" or p1 == "rock" and p2 == "paper":
#         return "Player 1 won!"
#     elif p2 == "scissors" and p1 == "paper" or p1 == "scissors" and p2 == "rock" or p2 == "paper " and p1 =="rock":
#         return "Player 2 won!"
#     else:
#         return "Draw!"

# print(rps("paper", "paper"))

def rps(p1,p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        print("Player 1 won!")
    if beats[p2] == p1:
        print( "Player 2 won!")

print(rps('rock','paper'))