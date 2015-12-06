
def score2num(checknum, difficulty):
    scorenum = 0
    if difficulty == 0:
        if checknum <= 3:
            scorenum = 100
        else:
            scorenum = 100 - ((checknum - 3) * 10)
    elif difficulty == 1:
        if checknum <= 3:
            scorenum = 200
        else:
            scorenum = 200 - ((checknum - 3) * 20)
    else:
        if checknum <= 3:
            scorenum = 300
        else:
            scorenum = 300 - ((checknum - 3) * 30)
    return scorenum

