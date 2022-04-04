birth_year = input('Birth year: ')
print(type(birth_year))
# need to convert string to int
# error:  age = 2019 - birth_year
# int()
# float()
# bool()
age = 2022 - int(birth_year)
print(type(age))
print(age)

weight_kg = input('Weight(kg): ')
weight_lbs = int(weight_kg) / 0.45
print('Weight(lbs):')
print(weight_lbs)