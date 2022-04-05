is_hot = False # Ture
is_cold = True # False

if is_hot: 
    print("It is a hot day")
    print("Drink plenty of water")
elif is_cold:     
    print("It is a cold day")
    print("Wear warm clothes")
else:
    print("It is a lovely day")
print("Enjoy your day")

#-----------------------------------
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")

#---------------------------------------
has_good_credit = True
has_high_income = False
has_criminal_record = False

if has_good_credit and has_high_income:
    print("1: Eligible for loan")

if has_good_credit or has_high_income:
    print("2: Eligible for loan")    

if has_good_credit and not has_criminal_record:
    print("3: Eligible for loan")

#--------------------------------------
temperature = 30

if temperature > 30:
    print("It is a hot day")
else: 
    print("It is not a hot day")

#----------------------------------
name = "J"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else: 
    print("Name looks good")

#---------------------------------------------------
weight = int( input('Weight: ') )
unit = input('(L)bs or (K)g: ') 
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
