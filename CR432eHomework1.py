# Course: CR432E
# Students: Wan Lan HE and Maxime PAQUIN

##############################################################################################
#Part1: Question1
def encrypt(plain_text, key):
    encrypted_text = ""
    
    for char in plain_text:
        # Check if the character is a lowercase letter
        if char.islower():
            # Calculate the shifted position and wrap around using modulo
            shifted = (ord(char) - ord('a') + key) % 26 + ord('a')
            encrypted_text += chr(shifted)
        else:
            # If it's not a lowercase letter, keep it unchanged
            encrypted_text += char
    
    return encrypted_text

# Prompt the user for the message to encrypt
message = input("Please enter the message to encrypt: ")

# Prompt the user for the key
key = int(input("Please enter the shift key (integer): "))

# Encrypt the message using the provided key
encrypted_message = encrypt(message, key)

# Output the encrypted message
print(f"Encrypted message: {encrypted_message}")


############################################################################################
#Part1: Question2
def decrypt(cipher_text, key):
    decrypted_text = ""
    
    for char in cipher_text:
        # Check if the character is a lowercase letter
        if char.islower():
            # Calculate the shifted position and wrap around using modulo
            shifted = (ord(char) - ord('a') - key) % 26 + ord('a')
            decrypted_text += chr(shifted)
        else:
            # If it's not a lowercase letter, keep it unchanged
            decrypted_text += char
    
    return decrypted_text

# Prompt the user for the message to decrypt
cipher_message = input("Please enter the message to decrypt: ")

# Prompt the user for the key
key = int(input("Please enter the shift key (integer): "))

# Decrypt the message using the provided key
decrypted_message = decrypt(cipher_message, key)

# Output the decrypted message
print(f"Decrypted message: {decrypted_message}")


############################################################################################
#Part1: Question3

#Encryption: Plaintext is combined with a secret key to produce scrambled data (ciphertext).
#Decryption: The ciphertext and the same secret key are used to revert the scrambled data back to the original plaintext.

############################################################################################
#Part1: Question4
import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add the argument for the character string
parser.add_argument('input_string', nargs='?', type=str)
parser.add_argument('--key', type=int, default=2)

# Parse the arguments
args = parser.parse_args()

# Validation of the input string
if args.input_string is None:
    args.input_string = input("Please enter a character string: ")

#Function to encrypt the message
def encrypt(plain_text, key):
    encrypted_text = ""
    
    for char in plain_text:
        # Check if the character is a lowercase letter
        if char.islower():
            # Calculate the shifted position and wrap around using modulo
            shifted = (ord(char) - ord('a') + key) % 26 + ord('a')
            encrypted_text += chr(shifted)
        else:
            # If it's not a lowercase letter, keep it unchanged
            encrypted_text += char
    return encrypted_text

#  Saves the encrypted string to a file.
def save_encrypted_file(encrypted_text):
    with open("encrypted_file.txt", "w") as f:
        f.write(encrypted_text)
    print("Encrypted file output to 'encrypted_file.txt'.")

# Encrypt the input string using the provided key
encrypted_text = encrypt(args.input_string, args.key)

# Save the encrypted string to a file
save_encrypted_file(encrypted_text)


############################################################################################
#Part1: Question5
def decrypt(cipher_text, key):
    decrypted_text = ""
    
    for char in cipher_text:
        # Check if the character is a lowercase letter
        if char.islower():
            # Calculate the shifted position and wrap around using modulo
            shifted = (ord(char) - ord('a') - key) % 26 + ord('a')
            decrypted_text += chr(shifted)
        else:
            # If it's not a lowercase letter, keep it unchanged
            decrypted_text += char
    
    return decrypted_text

def brute_force(cipher_text):
    possible_plaintexts = {}
    
    for key in range(26):  # There are 26 possible keys in the Caesar cipher
        decrypted_text = decrypt(cipher_text, key)
        possible_plaintexts[key] = decrypted_text
    
    return possible_plaintexts

# Prompt the user for the encrypted message
cipher_message = input("Please enter the encrypted message: ")

# Prompt the user for the key
key = int(input("Please enter the shift key (integer): "))

# Decrypt the message using the provided key
decrypted_message = decrypt(cipher_message, key)

# Output the decrypted message
print(f"Decrypted message: {decrypted_message}")

# Perform brute-force decryption on the encrypted message
brute_force_results = brute_force(cipher_message)

# Print the brute force results
print("Brute force results:")
for k, v in brute_force_results.items(): #method called from dictionary, 
    #K will hold the key as in V will hold the correspoing to that key
    print(f"Key {k}: {v}")



############################################################################################
#Part1: Question6
def decrypt(cipher_text, key):
    decrypted_text = ""
    
    for char in cipher_text:
        # Check if the character is a lowercase letter
        if char.islower():
            # Calculate the shifted position and wrap around using modulo
            shifted = (ord(char) - ord('a') - key) % 26 + ord('a')
            decrypted_text += chr(shifted)
        else:
            # If it's not a lowercase letter, keep it unchanged
            decrypted_text += char
    
    return decrypted_text

def brute_force(cipher_text):
    possible_plaintexts = {}
    
    for key in range(26):  # There are 26 possible keys in the Caesar cipher
        decrypted_text = decrypt(cipher_text, key)
        possible_plaintexts[key] = decrypted_text
    
    return possible_plaintexts

# Prompt the user for the encrypted message
cipher_message = input("Please enter the encrypted message: ")

# Prompt the user for the key
key = int(input("Please enter the shift key (integer): "))

# Decrypt the message using the provided key
decrypted_message = decrypt(cipher_message, key)

# Output the decrypted message
print(f"Decrypted message: {decrypted_message}")

# Perform brute-force decryption on the encrypted message
brute_force_results = brute_force(cipher_message)

# Print the brute force results
print("Brute force results:")
for k, v in brute_force_results.items(): #method called from dictionary, 
    #K will hold the key as in V will hold the correspoing to that key
    print(f"Key {k}: {v}")
