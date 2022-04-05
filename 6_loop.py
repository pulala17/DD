i = 1
while i <= 5:
    print(i)
    print('*' * i)
    i = i + 1
print("done")

#-----------------

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break 
else: 
    print('sorry, you failed')    

#-------------------------------
command = ""    
#while command != "quit":
while True:    
    command = input("> ").lower()
    if command == "start":
        print("Car started ...")
    elif command == "stop":    
        print("Car stopped.")    
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break     
    else:
        print("Sorry. I dont understand the command")    

#-------------------------------------------for loop
for item in 'Python':
    print(item)

for item in ['Mosh','John','Sara']: 
    print(item)   

for item in [1,2,3,4]: 
    print(item)   

for item in range(5): 
    print(item) 

for item in range(7,9): 
    print(item)     

for item in range(10,20,4): 
    print(item)   

#-------------------------
prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total:{total}")    

#--------------------------nested loop
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

#---------------------------
numbers = [5,2,5,2,2]
for number in numbers:
    print('*' * number)   
#----------------------
numbers = [1,2,3]
for number in numbers:
    output = ''
    for count in range(number):
        output += '*'
    print(output)    
