msg = "Hello World"
print(msg)

print("LX")

print('O----')
print(' ||||')

print('*' * 10)
print('lx' * 5)

price = 10
print('price')
print(price)

price = 20
rating = 4.9
name = 'xli'
is_published = False #boolean value
# Python is case sensitive language, its sensitive to lower case and upper case letters
print(price)

course = " Python's Course for beginners "
print(course)

course = ' Python for "beginners" '
print(course)

course = '''
Hi John,

Here is our first email to you.

Thank you
Xli
'''
print(course)

course = 'Python for Beginners'
print(course[0])
print(course[-1])
print(course[-2])
print(course[0:3]) #exclude the character at index 3
print(course[0:])
print(course[2:])
print(course[:5])
print(course[:])
another = course[:]
print(another)

name = 'Jennifer'
print(name[1:-1])

first = 'John'
last = 'Smith'
# message = first + ' [' + last + '] ' is a coder 
msg = f'{first} [{last}] is a coder'
# f: formatted string
print(msg)

course = 'Python for Beginners'
print(len(course)) # can enforce a limit on the #characters
# print, len are functions
# string.xxx are methods
print( course.upper() )  #course.lower
print( course )
print( course.find('P'))
print( course.find('o'))
print( course.find('x'))
print( course.find('Beginners'))
print( course.replace('Beginners', 'Absolute Beginners'))
print( course.replace('P', 'G'))

course = 'Python for Beginners'
print( 'Python' in course ) # a boolean expression 
print( 'python' in course )

