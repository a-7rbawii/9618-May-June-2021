class TreasureChest:
    def __init__(self, quest, ans, pts):
        self.__question = quest #as STRING
        self.__answer = ans #as INTEGER
        self.__points = pts #as INTEGER
    
    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self, key):
        if key == self.__answer:
            return True
        else:
            return False
    
    def getPoints(self, numOfAttempts):
        if numOfAttempts == 1:
            return int(self.__points)
        if numOfAttempts == 2:
            return int(self.__points) // 2
        if numOfAttempts == 3 or numOfAttempts == 4:
            return int(self.__points) // 4
        else:
            return 0

arrayTreasure = [None for i in range(5)] #as TreasureChest
def readData():
    File = r"C:\Users\Abood\Desktop\School\Final Revision Files\Computer Science\Past paper python\P4 Papers\May June 2021\TreasureChestData.txt"
    try:
        file = open(File, "r")
        dataFetched = (file.readline()).strip
        while dataFetched != "":
            question = dataFetched
            answer = (file.readline()).strip
            points = (file.readline()).strip
            arrayTreasure.append(TreasureChest(question, answer, points))
            dataFetched = (file.readline()).strip
        file.close()
    except IOError:
        print("Could not find file")

readData()
QuestChoice = input("Choose treasure chest: ")
if QuestChoice > 0 and QuestChoice < 6:
    result = False
    attempts = 0
    while result == False:
        answer = int(input(arrayTreasure[QuestChoice - 1].getQuestion()))
        result = arrayTreasure[QuestChoice - 1].checkAnswer(answer)
        attempts = attempts + 1
    print(int(arrayTreasure[QuestChoice - 1].getPoints(attempts)))
