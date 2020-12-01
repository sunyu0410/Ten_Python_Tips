# 1. Mutable objects and copy

listA = [1, 2, 3, 4]
listB = listA

print('listA:', listA)

listB.append(5)
print('listB:', listB)
print('listA:', listA)

# Check identity
listB is listA
id(listB) == id(listA)

# Solution 1 - slicing
listA = [1, 2, 3, 4]
listB = listA[:]
listB.append(5)
print('listB:', listB)
print('listA:', listA)

# Solution 2
import copy
listA = [1, 2, 3, 4]
listB = copy.copy(listA)
listB.append(5)
print('listB:', listB)
print('listA:', listA)

# However, this won't work if the object is nested
listC = [[1, 2], [3, 4], [5, 6]]
listD = listC[:]
listD[0][0] = 'one'
print('listD:', listD)
print('listC:', listC)

# For nested objects using copy.deepcopy()
listC = [[1, 2], [3, 4], [5, 6]]
listD = copy.deepcopy(listC)
listD[0][0] = 'one'
print('listD:', listD)
print('listC:', listC)

listA = [1, 2, 3, 4]
listB = copy.deepcopy(listA)
listB.append(5)
print('listB:', listB)
print('listA:', listA)