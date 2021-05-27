import random
print("Welcome to the Advanced Password Generator!")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["!", "£", "$", "%", "^", "&", "*", "(", ")"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

num_of_letters = int(input("How many letters would you like in you password?\n"))
num_of_symbols = int(input("How many symbols would you like in you password?\n"))
num_of_numbers = int(input("How many numbers would you like in you password?\n"))

total_characters = num_of_numbers + num_of_letters + num_of_symbols

password = []
for t in range(1, num_of_letters + 1):
    password.append(random.choice(letters))
for t in range(1, num_of_symbols + 1):
    password.append(random.choice(symbols))
for t in range(1, num_of_numbers + 1):
    password.append(random.choice(numbers))
random.shuffle(password)

password_string = ""
for value in password:
    password_string = password_string + value
print(password_string)
print(f"Your new password: {password_string}")
