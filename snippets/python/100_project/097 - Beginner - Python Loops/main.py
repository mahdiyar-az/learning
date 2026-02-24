import random

letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 'w', 'x', 'y','z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V','W','X','Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("welcome to the Pypassword generator!")
print("how many letters would you like in your password? ")
length_letters = int(input())
print("How many symbols would you like in your password? ")
length_symbols = int(input())
print("How many numbers would you like in your password? ")
length_numbers = int(input())

password_letter = []

for char in range(1, length_letters+1):
    password_letter.append(random.choice(letters))

for char in range(1, length_symbols+1):
    password_letter.append(random.choice(symbols))

for char in range(1, length_numbers+1):
    password_letter.append(random.choice(numbers))


password = ''
random.shuffle(password_letter)
for char in password_letter:
    password += char
print("your password is : "+password)
