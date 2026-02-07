import random

letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
#len 52

numbers = ['0','1','2','3','4','5','6','7','8','9']
#len 10

symbols = ['!','#','$','%','&','(',')','*','+']
#len 9

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
if nr_letters <= 0 or nr_letters > 52:
    print("Your input must be between 1 and 52")
if nr_symbols <= 0 or nr_symbols > 10:
    print("Your input must be between 1 and 10")
if nr_numbers <= 0 or nr_numbers > 9:
    print("Your input must be between 1 and 9")



new_list = []

for i in range(0,nr_letters):
    letter = random.choice(letters)
    new_list.append(letter)


for i in range(0,nr_symbols):
    symbol = random.choice(symbols)
    new_list.append(symbol)

for i in range(0,nr_numbers):
    number = random.choice(numbers)
    new_list.append(number)

random.shuffle(new_list)
password = "".join(new_list)
print(f"Your new password is: {password}")
