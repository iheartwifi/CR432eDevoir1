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
