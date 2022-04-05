from string import digits


customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True  # each key should be unique in a dictionary
}
print(customer["name"])
# print(customer["Name"])
print(customer.get("birthdate"))
print(customer.get("birthdate","Jan 1 1980"))

customer["name"] = "Jack Smith"
print(customer)

customer["birthdata"] = "Jan 1 1980"
print(customer)

#----------------------------------------------------------------------
phone = input("Phone: ")
digits_mapping = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!") + " "  # ! a default value, so can get a word
print(output)    

#--------------------------------------------
message = input(">")
words = message.split(' ')
# go through string and find the character in ''(now a space),
# and use it as a boundary to seperate the string into multiple words & return a list
emojis = {
    "smile": ":)",
    "sad":":("
}
output = ""
for word in words:
    output += emojis.get(word, word) + " " 
print(output)
