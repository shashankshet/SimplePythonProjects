#password generator using python
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','-','=','+',':',';','<','>',',','.','/','?']
numbers = [1,2,3,4,5,6,7,8,9,0]

print("Welcome to ShankPassword generator!")

letter_length = int(input("How many letters would you like in your password?: \n"))
symbol_length = int(input("How many symbols would you like in your password?: \n"))
number_length = int(input("How many numbers would you like in your passeord?: \n"))

password = ""

for i in range(0,letter_length):
    password += random.choice(letters)
for i in range(0,symbol_length):
    password += random.choice(symbols)
for i in range(0,number_length):
    password += str(random.choice(numbers))

print(''.join(random.sample(password,len(password)))) #to shuffle the elements in the string