import random
import time 

def getRandomDate(startdate,endate):
    print("printing random date between",startdate,"and",endate)
    randomGenerator = random.random()
    dateformat= '%m/%d/%Y'
    startime =time.mktime(time.strptime(startdate, dateformat))
    endtime = time.mktime(time.strptime(endate, dateformat))

    randomtime= startime + randomGenerator *(endtime - startime)
    randomdate= time.strftime(dateformat, time.localtime(randomtime))
    return randomdate
print("Randomdate =", getRandomDate("1/1/2016","12/12/2018"))
