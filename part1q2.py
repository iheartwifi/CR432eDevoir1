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
