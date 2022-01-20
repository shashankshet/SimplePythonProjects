from art import logo
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
# function to return key for any value
def get_key(val):
    for key, value in bidInfo.items():
         if val == value:
             return key
 
    return "key doesn't exist"

print(logo)
print("Welcome to secret auction program!")
bidInfo = {}
flag = True
while(flag):
    name = input("what is your name? ")
    bidInfo[name] = int(input("What's your bid? $"))

    check = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if(check=="yes"):
        clearConsole()
    elif(check== "no"):
        flag = False
        Keymax = max(zip(bidInfo.values(), bidInfo.keys()))[1]
        # print(Keymax)
        print("The winner is "+str(Keymax)+" with a bid of $"+str(bidInfo[Keymax]))

