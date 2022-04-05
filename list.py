names = ['John','Bob','Mosh','Sarah','Mary']
print(names)
print(names[0])
print(names[-1])
print(names[2:4])
print(names[2:])
names[0] = 'Jon'
print(names)

#------------------------
numbers = [1,4,7,8,3,2]
max = numbers[0]
for num in numbers:
    if max <= num:
        max = num
print(max)

#------------------2 dimensional lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0])
print(matrix[1][2])
matrix[1][2] = 22
print(matrix[1][2])

for row in matrix:
    for item in row:
        print(item)

#---------------------
numbers = [5,2,1,7,4]
numbers.append(20)
print(numbers)        
numbers.insert(0,10) # insert(location, number)
print(numbers)   
numbers.remove(5)
print(numbers)   
numbers.clear()
print(numbers)

numbers = [3,4,6,2,8,1,9,5]
numbers.pop()
print(numbers)    
print(numbers.index(6)) 
print(50 in numbers) # print(numbers.index(50))
print(numbers.count(5))  
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(10)
print(numbers)
print(numbers2)

#----------remove the duplicates in a list
numbers = [2,2,4,6,3,4,6,1]
uniques = []
for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(uniques)        