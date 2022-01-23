#importing nessacary modules
from subprocess import check_output
from menu import MENU
from menu import resources

#main function of the coffee machine
def coffee():
    choice = input("What would you like to have?\nespresso: $1.5 \nlatte: $2.5 \ncappuccino: $3.0\nType here--> ")
    if choice == "report": #to check if the user wants to check the report
        print("\n")
        print("water:"+str(resources["water"]))
        print("milk: "+str(resources["milk"]))
        print("coffee:"+str(resources["coffee"]))
        print("\n")
        coffee() #calls back reccursively after printing the report
    print("Please enter coins") #takes the user input for coins
    quaters = int(input("How many quaters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How may nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quaters*0.25 + dimes*0.10 + nickles*0.05 +pennies*0.01 #finds the total amount of money inserted by the user

    


    if total >= MENU[choice]["cost"]: #checks if the user added amount is suffitient to buy the choosen coffee
        if(resources["water"]>=MENU[choice]["ingredients"]["water"]):
            if(resources["milk"]>= MENU[choice]["ingredients"]["milk"]):
                if(resources["coffee"]>=  MENU[choice]["ingredients"]["coffee"]):
                    print("Here is $"+str(round(total-MENU[choice]["cost"],2))+" in change.")
                    resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
                    resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
                    resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
                    print("\nHere is your "+choice+". Enjoy!\n")
                else:
                    print("Sorry there is no enough coffee\n")
            else:
                print("Sorry there is no enough milk\n") 
        else:
            print("Sorry there is no enough water\n")
    else:
        print("Sorry that's not enough money. Money refunded.\n")
    coffee()

coffee()