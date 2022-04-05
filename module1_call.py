import numbers
import module1
numbers = [10,4,6,22]
print(module1.find_max(numbers))

from module1 import find_max
numbers = [9,2,8,4,1,11]
print(find_max(numbers))