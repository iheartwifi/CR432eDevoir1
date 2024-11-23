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
