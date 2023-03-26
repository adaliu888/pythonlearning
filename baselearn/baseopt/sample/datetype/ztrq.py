import datetime


def getyesterday():
    today = datetime.date.today()
    print(today)
    print(type(today))
    oneday = datetime.timedelta(days=4)
    yesterday = today - oneday
    return yesterday


def getfurdays():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=7)
    nextday = oneday + today
    return nextday


print(getyesterday())

print(getfurdays())
