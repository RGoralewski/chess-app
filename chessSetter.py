import random

def setMatches(players):
    # 2D list with matches
    result = []

    # A list to save who has played with who
    matches = []
    for p in players:
        matches.append([])

    # Current match number
    matchNumber = 1

    # Calculate total number of matches to play and print it
    matchesToPlay = 0
    for i in range(1, len(players)):
        matchesToPlay += i

    allMatchesSet = False
    while allMatchesSet == False:
        # Find the least playing player
        leastPlayingPlayer = 0
        for i in range(1, len(matches)):
            if len(matches[i]) < len(matches[leastPlayingPlayer]):
                leastPlayingPlayer = i

        # Starting opponent - different than first player
        leastPlayingOpponent = random.randrange(len(players))
        if leastPlayingOpponent == leastPlayingPlayer:
            leastPlayingOpponent += 1
            if leastPlayingOpponent >= len(players):
                leastPlayingOpponent = 0

        # Find an opponent
        found = False
        # Opponents that have already played with chosen player
        knownOpponents = []
        while not found:
            # Find the least playing player besides first player and known opponents
            for i in range(0, len(matches)):
                if ((len(matches[i]) < len(matches[leastPlayingOpponent])) and (i != leastPlayingPlayer)) and (i not in knownOpponents):
                    leastPlayingOpponent = i

            # Check if players have already played
            found = True
            for m in matches[leastPlayingOpponent]:
                if m == leastPlayingPlayer:
                    found = False
                    knownOpponents.append(leastPlayingOpponent)

                    # Find a new starting opponent
                    leastPlayingOpponent = random.randrange(len(players))
                    while (leastPlayingOpponent == leastPlayingPlayer) or (leastPlayingOpponent in knownOpponents):
                        leastPlayingOpponent += 1
                        if leastPlayingOpponent >= len(players):
                            leastPlayingOpponent = 0

                    break


        # Save match
        result.append([players[leastPlayingPlayer], players[leastPlayingOpponent]])
        matchNumber += 1
        matches[leastPlayingPlayer].append(leastPlayingOpponent)
        matches[leastPlayingOpponent].append(leastPlayingPlayer)

        # Check if all matches are already set
        if (matchNumber > matchesToPlay):
            allMatchesSet = True
            break

    return result


# Unit test
def main():
    # List of players
    players = ["Radek", "Adam", "Maciek", "Patryk"]

    # Set matches
    matches = setMatches(players)

    # Print matches
    for i in range(0, len(matches)):
        print("{}. {} - {}".format(i+1, matches[i][0], matches[i][1]))



if __name__ == '__main__' :
    main()
