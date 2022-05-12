# Organize employee name in alphabetical order
# Refs : https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-names-by-last-name/
# explicit function sort names
# by their surnames
def sortBySurname(nameList):
    splitNameList = []
  
    # create 2d list of names
    for name in nameList:
        splitNameList.append(name.split())
    nameList = []
  
    # sort by last name
    for name in sorted(splitNameList, key=lambda name: name[-1]):
        nameList.append(' '.join(name))
  
    # return sorted list
    return nameList
  
# assign list of names
nameList = ['John Wick', 'Jason Voorhees',
            'Freddy Krueger', 'Keyser Soze',
            'Mohinder Singh Pandher']
  
# print('\nList of Names:\n', nameList)
print('\nAfter sorting:\n', sortBySurname(nameList))

