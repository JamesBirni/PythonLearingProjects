playersAndScore = {}
letterAndPoints ={'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, ' ':0}
def playerAmount():
    try:
        players = int(input("How many player will be playing "))
    except ValueError:
        print("Invaild type please type a number")
        players = playerAmount()
    if players<1:
        print("Invaild player count")
        players = playerAmount()
    return players
def namePlayers():
    for i in range(1,numPlayers+1):
        name = input("Player {} what is you're name ".format(i))
        playersAndScore[name] = 0
def wordToPoints(word):
    upperWord =word.upper()
    pointTotal = 0
    for letter in upperWord:
        if letter in letterAndPoints:
            pointTotal += letterAndPoints.get(letter)
    return pointTotal
def round():
    end = input("If you would like to end the game type YES, if you would like to continue press enter ")
    if end == "YES":
        return
    else:
        for i in playersAndScore.keys():
            print("{} What word did you score press enter if you have no words".format(i))
            word = input()
            playersAndScore[i] += wordToPoints(word)
        round()
def endOfGame():
    winnerName = "No one"
    winnerScore = 0
    print("Game is over score of each player is")
    for player,score in playersAndScore.items():
        print("{} you have {} score".format(player,score))
        if(winnerScore < score):
            winnerName = player
            winnerScore = score
    print("Game winner is {} with {} score".format(winnerName, winnerScore))

numPlayers = playerAmount()
namePlayers()
round()
endOfGame()