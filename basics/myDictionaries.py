

exDict = {'Jack': 15, 'Bob': 22, 'Alice': 12, 'Kevin': 17}
print(exDict)
print(exDict['Jack'])

exDict['Tim'] = 14
print(exDict)

exDict['Tim'] = 15
print(exDict)

del exDict['Tim']
print(exDict)


# another dictionary

exDict2 = {'Jack': [15, 'blond'], 'Bob': [22, 'brown'], 'Alice': [12, 'black'], 'Kevin': [17, 'red']}
print(exDict2['Jack'][1])
