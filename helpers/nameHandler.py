from datetime import date

def getCurrentMonth() :
    return date.today().strftime("%B")

def getPaychecks(howOften) :
    Dict.get(howOften)

def getWeeklyPaycheck() :
    print("WEEKLY")

def getBiWeeklyPaycheck() :
    print("BiWeekly")
    
def getSemiMonthlyPaycheck() :
    print("SemiMonthly")
    
def getMonthlyPaycheck() :
    print("MONTHLY")


Dict = {1: getWeeklyPaycheck(), 2 : getBiWeeklyPaycheck(), 3 : getSemiMonthlyPaycheck(), 4 : getMonthlyPaycheck()}