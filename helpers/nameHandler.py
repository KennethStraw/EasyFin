from datetime import date

def getCurrentMonth() :
    return date.today().strftime("%B")