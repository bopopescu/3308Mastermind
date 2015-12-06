#class for each playable slot
class User():
    def __init__(self, name):
        self.name = name
        self.highScore = loadHighScore(self.name)
        self.difficulty = loadDifficulty(self.name)
    def newScore(self, score):
        addScore(self, score)
    def changeDifficulty(self, difficulty):
        changeDefaultDifficulty(self, difficulty)

def loadHighScore(user):
    scores = open("scores.csv", 'r')
    highScore = 0
    for line in scores:
        userInfo = line.split(',')
        if userInfo[0] == user:
            for i in range(1, len(userInfo)):
                currScore = int(userInfo[i])
                if currScore > highScore:
                    highScore = currScore
    return highScore

def loadDifficulty(user):
    scores = open("scores.csv", 'r')
    for line in scores:
        userInfo = line.split(',')
        if userInfo[0] == user:
            return userInfo[1]
    return 0

def changeDefaultDifficulty(self , difficulty):
    scores = open("scores.csv", 'r')
    scoreFile = ""
    tempLine = ""
    for line in scores:
        userInfo = line.split(',')
        if userInfo[0] == self.name:
            tempLine = line[0: line.find(',')] + difficulty + line[line.find(',', line.find(',') + 1) : len(line)]
            scoreFile += tempLine
        else:
            scoreFile += line
    overwriteScoreFile(scoreFile)

def addScore(self, score):
    scores = open("scores.csv", 'r')
    scoreFile = ""
    success = 0
    for line in scores:
        userInfo = line.split(',')
        scoreFile += line
        if userInfo[0] == self.name:
            scoreFile += (',' + str(score))
            success = 1
    if(success != 1):
        scoreFile += self.name + ',' + self.difficulty + ',' + score
    overwriteScoreFile(scoreFile)

def overwriteScoreFile(fileContents):
    scores = open("scores.csv", 'w')
    scores.write(fileContents)