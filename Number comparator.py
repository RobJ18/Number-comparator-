firstnum = input('Pick a number: ')

secondnum = input('Pick another number: ')

if (firstnum > secondnum):
    print(firstnum, ' is the bigger number')

elif (firstnum < secondnum):
    print (secondnum, ' is the bigger number')

elif (firstnum == secondnum):
    print ('These numbers are equal')

else:
    exit()
