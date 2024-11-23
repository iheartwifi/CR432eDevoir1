# Course: CR432E
# Students: Wan Lan HE and Maxime PAQUIN

############################################################################################
#Part 2: Question 7
def frq_txt(text):
    # Create a dictionary to count occurrences of each character
    char_count = {}
    
    # Count occurrences of each character
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Convert the dictionary to a list of tuples and sort it
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    
    # Convert tuples to a list of dictionaries
    result = [{char: count} for char, count in sorted_char_count]
    
    return result

# Program to read the entire file using read() function
file = open("english_sample.txt", "r")
content = file.read()

# Call the function with the english sample text
character_frequencies = frq_txt(content)
print(character_frequencies)


############################################################################################
#Part 2: Question 8
def frq_cpr(byte_sequence):
    # Create a dictionary to count occurrences of each byte
    count = {}

    # Count occurrences of each byte
    for byte in byte_sequence:
        if byte in count:
            count[byte] += 1
        else:
            count[byte] = 1

    # Sort the dictionary by count in descending order
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    return sorted_count

# Open the binary file
with open("cipher_sample.bin", "rb") as byte_sequence:  # Open in binary mode
    # Read the entire content of the file
    data = byte_sequence.read()

# Call the function and print the result
result = frq_cpr(data)
print(result)


############################################################################################
#Part 2: Question 9
#When compare these ordered lists, one from a byte perspective and 
#the other from a character perspective on a frequency analysis.

############################################################################################
#Part 2: Question 10

def build_dec_key(encrypt_key, partial_keys):
    decrypt_key = {}
    
    # Iterate through the specified partial keys
    for char in partial_keys:
        # Get the encrypted value for the character
        encrypted_char = encrypt_key.get(char)
        if encrypted_char is not None:
            # Map the encrypted character back to the original character
            decrypt_key[encrypted_char] = char
    
    return decrypt_key

# Example usage
encryption_key = {
    'a': b'1a',
    'b': b'2b',
    'c': b'3c',
    'd': b'4d',
}

# Specify which characters to include in the partial decryption key
partial_keys = ['a', 'b']  # Only create mappings for 'a' and 'b'

# Build the partial decryption key
partial_decryption_key = build_dec_key(encryption_key, partial_keys)

# Output the partial decryption key
print("Partial Decryption Key:", partial_decryption_key)


############################################################################################
#Part 2: Question 11

