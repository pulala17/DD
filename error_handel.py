
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid value')
    # except block only catches exceptions of type ValueError,
    # like when convert a nonnumberical value to integer
except ZeroDivisionError:
    print('Age cannot be 0.')    