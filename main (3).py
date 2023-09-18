class Player:
    def play(self):
        print("The player is playing cricket")

class Batsman(Player):
    def play(self):
        print("The batsman is batting")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling")

# Creating objects of Batsman and Bowler classes and calling the play() method for each object
batsman = Batsman()
bowler = Bowler()

batsman.play()  # Output: "The batsman is batting"
bowler.play()   # Output: "The bowler is bowling"