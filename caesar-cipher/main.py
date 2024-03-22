from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(message, offset):
    encrypted_mssg = ""
    for char in message:
        if char not in alphabet:
            encrypted_mssg += char
        else:
            curr_index = alphabet.index(char) + 1
            offset_index = ((curr_index +  offset) % 26) - 1
            encrypted_mssg += alphabet[offset_index]
    print(f"Here's the encoded result: {encrypted_mssg}")


def decryption(message, offset):
    decrypted_mssg = ""
    for char in message:
        if char not in alphabet:
            decrypted_mssg += char
        else:
            curr_index = alphabet.index(char)
            offset_index = (curr_index -  offset)
            if offset_index >= 0:
                decrypted_mssg += alphabet[offset_index]
            else:
                decrypted_mssg += alphabet[26 + offset_index]

    print(f"Here's the decoded result: {decrypted_mssg}")        

print(logo)
program_exit = False
while not program_exit:
    task = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if task == "encode":
        #Carry out the encode logic
        message = input("Type your message: \n").lower()
        offset = int(input("Type the shift number: \n"))
        encryption(message, offset)

    elif task == "decode":
        #Carry out the decode logic
        message = input("Type your message: \n").lower()
        offset = int(input("Type the shift number: \n")) % 26
        decryption(message, offset)   

    else:
        #Display the message that the option that u r asking for is not present
        print("You have entered a wrong option. Try again !")
    want_to_go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()
    if want_to_go_again == "no":
        program_exit = True


print("Thank you for playing Caesar-Cipher!")
