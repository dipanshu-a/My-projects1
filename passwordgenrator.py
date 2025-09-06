
import random

letters = [ 'a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = [ '0','1','2','3','4','5','6','7','8','9']

symbol = ['!', '#', '$', '%', '&','(', ')','*','+']

print("Welcome to the password generator ")

nr_letters = int(input( " How many latters would to like your password?\n"))

nr_symbol = int(input(f" How many symbol would you like ?\n"))

nr_numbers = int(input(f" How many numbers would you like?\n"))

password = ""

for char in range (0, nr_letters):
    password += random.choice(letters)

for char in range (0 , nr_symbol):

    password += random.choice(symbol)

for char in range ( 0 , nr_numbers):

    password += random.choice(numbers)

    print(password)

    print(" Thanks for wising The password genrator ")