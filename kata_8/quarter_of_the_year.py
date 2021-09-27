def quarter_of(month):
    #a year have 12 months and 4 quarter
    if (month <= 3):
        return 1
    elif (month <=6 and month >3):
        return 2
    elif (month <=9 and month >6):
        return 3
    elif (month <=12 and month >9):
        return 4