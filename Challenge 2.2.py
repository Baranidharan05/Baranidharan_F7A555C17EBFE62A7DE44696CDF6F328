class player:

  def play(self):
    print("The player is playing cricket.")


class batsman(player):

  def play(self):
    print("The Batsman is batting...")


class bowler(player):

  def play(self):
    print("The Bowler is bowling...")


player = player()
batsman = batsman()
bowler = bowler()

player.play()
batsman.play()
bowler.play()
