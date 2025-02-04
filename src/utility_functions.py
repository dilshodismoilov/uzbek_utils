digitsAndTens = {
    "bir": 1,
    "ikki": 2,
    "uch": 3,
    "to'rt": 4,
    "besh": 5,
    "olti": 6,
    "yetti": 7,
    "sakkiz": 8,
    "to'qqiz": 9,
    "o'n": 10,
    "yigirma": 20,
    "o'ttiz": 30,
    "qirq": 40,
    "ellik": 50,
    "oltmish": 60,
    "yetmish": 70,
    "sakson": 80,
    "to'qson": 90
}
hundredText = "yuz"
thousandText = "ming"
millionText = "million"
billionText = "milliard"
trillionText = "trillion"

values = {
    hundredText: 100,
    thousandText: 1000,
    millionText: 1e6,
    billionText: 1e9,
    trillionText: 1e12
}

months = {
    "yanvar": 1,
    "fevral": 2,
    "mart": 3,
    "aprel": 4,
    "may": 5,
    "iyun": 6,
    "iyul": 7,
    "avgust": 8,
    "sentabr": 9,
    "oktyabr": 10,
    "noyabr": 11,
    "dekabr": 12
}


def numberTextToInt(numberText: str):
    res = 0
    #bir yuz ellik olti ming ikki yuz oltimsh uch
    temp = 0
    for el in numberText.split():
        el = removeInchi(el)
        if el in digitsAndTens:
            temp += digitsAndTens[el]
        elif el==hundredText:
            if temp != 0:
                temp *= 100
            else:
                temp = 100
        elif el==thousandText or el == millionText or el == billionText or el == trillionText:
            if temp != 0:
                temp *= values[el]
            else:
                temp = values[el]
            res += temp
            temp = 0
    res += temp
    return res

#print(numberTextToInt("to'qqiz yuz yigirma olti million bir yuz ellik olti ming ikki yuz oltmish"))

def removeInchi(numberText: str):
    if numberText.endswith("nchi"):
        numberText = numberText[:-4]
        if numberText not in digitsAndTens:
            numberText = numberText[:-1]
    return numberText
