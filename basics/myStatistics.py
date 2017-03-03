import csv

myList = [
            [2, 6],
            [6, 2],
            [8, 2],
            [5, 12]
         ]
print(myList[1][0])


with open('example.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')

    dates = []
    colors = []

    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    try:
        whatColor = input('what color do you wish to know the date of? ')

        if whatColor in colors:
            coldex = colors.index(whatColor.lower())
            theDate = dates[coldex]
            print('The date of', whatColor, 'is:', theDate)
        else:
            print('Color nor found, or is not a color')
    except Exception as e:
        print(e)

    print('continuing...')