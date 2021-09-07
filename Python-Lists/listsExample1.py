#List Declaration/Creation
#exampleList = [] #square bracket method
exampleList = list() #constructor method


#Append Method
#Definition: Adds an element or an item at the end of a list.
print(exampleList)
exampleList.append(10) #exampleList = [] -> [10]
print(exampleList)
exampleList.append(9) #exampleList = [10] -> [10,9]
print(exampleList)
exampleList.append(100) #exampleList = [10,9] -> [10,9,100]
print(exampleList)

#Extend Method
#Definition: Adds a list of elements or another list at the end of the list expanding the main list.
exampleList.extend([90,'abc'])
print(exampleList)
newList = ['bob','sally']
exampleList.extend(newList)
print(exampleList)

#Insert Method
#Definition: Adds/Insert an element or item at the given index position.
print(exampleList[2])
exampleList.insert(2,'xyz')
print(exampleList[2])
print(exampleList)
exampleList.insert(0,987)
print(exampleList)

#Remove Method
#Definition: Removes the first element or item that matches the criteria it's given.
exampleList.remove('bob')
print(exampleList)

#Pop Method
#Definition: Removes the element given by it's index location and returns the element or item that was removed
print(exampleList.pop(0))
print(exampleList)
print(exampleList.pop(3))
print(exampleList)

#Index Method
#Definition: Returns the index location of the item that matches the criteria it's given. Raises a ValueError if there was no match.
index = exampleList.index('xyz')
print(exampleList[index])


#Count Method
#Definition: Returns the number of tiems the item that matches the criteria of the count.
print(exampleList.count(10))
exampleList.append(10)
print(exampleList.count(10))

#Reverse Method
#Definition: Reverses the order of the elemnts or items in the list.
exampleList.reverse()
print(exampleList)

#Copy Method
#Definition: Shallow copies the list to another variable making that variable a copy of the original list.
exampleList.insert(0,[100,920,'abxc'])
newList = exampleList.copy()
newList[1] = 'bob'
newList[0][1] = 'u'
print(newList)
print(exampleList)

#Clear Method
#Definition: Removes all the elements or items in the list.
print(exampleList)
exampleList.clear()
newList.clear()
print(exampleList)
print(newList)

#Sort Method
#Definition: Sorts the elements or items in the list using the Timsort algorithm.
exampleList.append(10)
exampleList.append(8)
exampleList.append(80)
exampleList.append(1)
print(exampleList)

exampleList.sort()
print(exampleList)
exampleList.clear()
exampleList.append('x')
exampleList.append('b')
exampleList.append('d')
exampleList.append('t')
print(exampleList)
exampleList.sort()
print(exampleList)