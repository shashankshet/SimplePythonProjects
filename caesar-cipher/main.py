alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text,shift_amout,cipher_direction):
    end_text = ""
    if(cipher_direction=="decode"):
        shift_amout *=-1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position+shift_amout
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here is the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

should_continue = True
while(should_continue):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift%26

    caesar(start_text=text,shift_amout=shift,cipher_direction=direction)

    result = input("type 'yes' if you want to go again, otherwise type 'no'.\n").lower()

    if(result=="no"):
        should_continue = False
        print("Good bye")