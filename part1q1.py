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
