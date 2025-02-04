from utility_functions import *
import datetime
# split birthday text into parts: day, month, year
# standard case: ikki ming birinchi yil o'n yettinchi noyabr
def splitStandard(birthDateText: str):
    birthDateAr = birthDateText.split(" ")
    yearText = ""
    monthText = ""
    dayText = ""
    temp = ""
    for el in birthDateAr:
        if el != "yil" and el not in months:
            temp += el + " "
        elif el == "yil":
            yearText =  temp
            temp = ""
        elif el in months:
            dayText = temp
            monthText = el
    return [yearText, monthText, dayText]

def birthDateTextToStandard(birthDateText: str):
    splitResult = splitStandard(birthDateText)
    year = numberTextToInt(splitResult[0])
    if year < 100:
        year += 1900
    month = months[splitResult[1]]
    day = numberTextToInt(splitResult[2])
   
    return datetime.datetime(year, month, day)
    #print(f"{year}-{month}-{day}")

#birthDateTextToStandard("ikki ming eee ... asdsad birinchi yil o'n yettinchi noyabr")
print(birthDateTextToStandard("eee nima ediya yo'q to'qson to'qqizinchi yil birinchi iyul"))