import copy

listA = [1,2,['x','y','z'],3,4]
listB = copy.copy(listA)
print(f'ListA: {listA}')
print(f'ListB: {listB}')

listA[1] = 9
listB[2][0] = 'change'
print(f'ListA Memory: {hex(id(listA[2][0]))}')
print(f'ListB Memory: {hex(id(listB[2][0]))}')
print(f'ListA: {listA}')
print(f'ListB: {listB}')
