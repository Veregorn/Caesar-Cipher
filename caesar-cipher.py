logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

# The program runs in a loop until user selects 'no'
repeat = "yes"

while repeat == "yes":
    # Reset repeat variable
    repeat = ""

    # OPTION RECORDING: While no right option typed, print the select option message
    option = ""

    while not(option == "encode") and not(option == "decode"):
        option = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ")

    # MESSAGE RECORDING: All messages are valid
    message = input("Type your message: ")

    # SHIFT RECORDING: All shifts are valid, but only numbers
    shift = 0

    while not(shift > 0 and shift < 27):
        shift = int(input("Type the shift number (1 - 26): "))

    # Encode function implementation
    def caesar(message,shift,option):
        encoded_word = ""
        if option == "encode":
            # Forward shift
            for char in message:
                if 'a' <= char <= 'z':  # Check if char is a lowercase letter
                    encoded_word = encoded_word + chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                elif 'A' <= char <= 'Z':  # Check if char is an uppercase letter
                    encoded_word = encoded_word + chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                else:
                    encoded_word = encoded_word + char

            print(f"Here's the encoded result: {encoded_word}")
        else:
            #Backward shift
            for char in message:
                if 'a' <= char <= 'z':  # Check if char is a lowercase letter
                    encoded_word = encoded_word + chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                elif 'A' <= char <= 'Z':  # Check if char is an uppercase letter
                    encoded_word = encoded_word + chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                else:
                    encoded_word = encoded_word + char

            print(f"Here's the decoded result: {encoded_word}")

    # Call caesar function
    caesar(message,shift,option)

    # Ask user if he/she wants to repeat
    while not(repeat == "yes") and not(repeat == "no"):
        repeat = input("Type 'yes' if you want to go again. Otherwise type 'no': ")