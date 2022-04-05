def greet_user(first_name, last_name):
    print(f'Hi {first_name}, {last_name}!')
    print('Welcome!')


print("Start!")
greet_user("John","Smith")
greet_user("Mary","Lee")
greet_user(last_name="Smith",first_name="John")
print("Finish!")

def square(number):
    return number * number  # by default python return None

print(square(3))  

#-------------------------------------------------------
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        "smile": ":)",
        "sad":":("
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " " 
    return output


message = input(">")
print(emoji_converter(message))
