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
