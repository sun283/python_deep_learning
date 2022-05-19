
nameList = ['John Wick', 'Jason Voorhees',
            'Freddy Krueger', 'Keyser Soze',
            'Mohinder Singh Pandher']

splitNameList = []

for name in nameList:
    splitNameList.append(name.split())
    print(splitNameList)
    nameList = []
    for name in sorted(splitNameList, key=lambda name: name[-1]):
        nameList.append(' '.join(name))
        print(nameList)
        
    