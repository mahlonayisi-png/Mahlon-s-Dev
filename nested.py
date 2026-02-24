allGuest= {'Alice':{'apples' :5,'pretzels':12},
              'Bob':{'ham sandwiches' : 3,'apple': 2},
             'Carol':{'cup':3,'apple pies':1}}

def totalBrought(guests,item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item,0)
    return numBrought
print('Number of things being brought:')
print('-Apples      ' + str(totalBrought(allGuest,'apple')))
print('-cups    ' + str(totalBrought(allGuest, 'cups')))
print('-ham Sandwich '+ str(totalBrought(allGuest,'ham sandwiches')))
print('-cakes  '+ str(totalBrought(allGuest,'cakes')))
print('-Apple Pies '+ str(totalBrought(allGuest,'apple pies')))
