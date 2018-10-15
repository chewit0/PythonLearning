import re
import datetime

# Script to take dates in multiple formats from string
# and unify them into UK sformat dd/mm/yyyy

# Dates it will correct
# dd-,/.mm-yy (if year > current year, assumed to be 19yy, ootherwise 20yy)
# mm-dd-yy (if day>12)


def regex(searchString, reg):
    match = re.compile(reg)
    result = match.findall(searchString)
    return result


def updateDate(date, check=True):

    now = datetime.datetime.now()
    day = date[0]
    month = date[1]
    year = date[2]

    # Year checker
    if (len(year) == 2):
        if int(year) > now.year % 100:
            year = int(str(19) + year)
        else:
            year = int(str(20) + year)

    # American format check
    if (int(date[1]) > 12):  # if condition met - must be an american format
        day = month
        month = date[0]
    else:
        if check:
            print(
                "It is possible that {}/{}/{} is in american format, "
                "please check".format(day, month, year))
            print("To remove this warning, pass flag check=false to function")

    newdate = str(day) + '/' + str(month) + '/' + str(year)
    return newdate


def main():

    newdates = []
    searchString = '02-10-1960 03,17 40 00 00 00asd American: 12/31/60asdawerf'
    dateRegex = '(\d{1,2})[-.,/](\d{1,2})[-. ,/](\d{2,4})'

    result = regex(searchString, dateRegex)

    for date in result:
        newdates.append(updateDate(date, False))
    print(newdates)

if __name__ == "__main__":
    main()
