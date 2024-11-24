import pickle
import collections

############################################################################################
# Part 2: Question 7 -
def frq_txt(text):
    """
    Analyzes the frequency of characters in a text.

    Args:
        text: The input text.

    Returns:
        A sorted list of dictionaries containing characters and their frequencies.
    """
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return [{char: count} for char, count in sorted_char_count]

# Analyze character frequencies in a text file
with open("english_sample.txt", "r") as file:
    content = file.read()

character_frequencies = frq_txt(content)
print(character_frequencies)

############################################################################################
# Part 2: Question 8 - Byte Frequency Analysis
def frq_cpr(byte_sequence):
    """
    Analyzes the frequency of bytes in a binary sequence.

    Args:
        byte_sequence: The input binary data.

    Returns:
        A sorted list of tuples containing bytes and their frequencies.
    """
    count = {}
    for byte in byte_sequence:
        count[byte] = count.get(byte, 0) + 1
    return sorted(count.items(), key=lambda x: x[1], reverse=True)

# Analyze byte frequencies in a binary file
with open("cipher_sample.bin", "rb") as file:
    data = file.read()

byte_frequencies = frq_cpr(data)
print(byte_frequencies)

############################################################################################
# Part 2: Question 9 - Comparing Frequencies
# Compare frequency analysis results from text and binary data (left for interpretation).

############################################################################################
# Part 2: Question 10 - Building Decryption Keys
def build_dec_key(enc_key, partial_keys=None):
    """
    Builds a decryption key by inverting the encryption key.
    Optionally creates a partial decryption key.

    Args:
        enc_key: The encryption key as a dictionary.
        partial_keys: A list of keys to include in the partial decryption key (optional).

    Returns:
        The decryption key as a dictionary.
    """
    if partial_keys:
        return {enc_key[k]: k for k in partial_keys if k in enc_key}
    return {v: k for k, v in enc_key.items()}

def guess_txt(ciphertext, partial_key):
    """
    Decrypts a ciphertext using a partial key.

    Args:
        ciphertext: The ciphertext to decrypt.
        partial_key: A dictionary mapping encrypted characters to plaintext characters.

    Returns:
        The decrypted plaintext.
    """
    return ''.join([partial_key.get(char, '$') for char in ciphertext])

############################################################################################
# Frequency Analysis and Key Creation
def analyze_frequency(text_file):
    """
    Analyzes the frequency of characters in a text file.

    Args:
        text_file: The path to the text file.

    Returns:
        A dictionary of character frequencies.
    """
    with open(text_file, 'r') as file:
        text = file.read().lower()
    char_counts = collections.Counter(text)
    total_chars = sum(char_counts.values())
    return {char: count / total_chars for char, count in char_counts.items()}

############################################################################################
# Main Program
def main():
    # Load encryption key
    with open("enc_key.pkl", "rb") as file:
        enc_key = pickle.load(file)

    # Build decryption key
    dec_key = build_dec_key(enc_key)

    # Question 11: Test guess_txt
    ciphertext = "Uif sfbejoh pg uif qspkfdu dbo cf nf! Jt bsf b qspkfdu."
    partial_key = {
        'e': b'2d', 't': b'68', 'a': b'73', 'o': b'6f', 'i': b'61',
        'n': b'75', 's': b'69', 'r': b'6e', 'h': b'72', 'l': b'6f',
        'd': b'64', 'c': b'6c', 'm': b'6d', 'u': b'65', 'w': b'70',
        'g': b'67', 'y': b'62'
    }
    decrypted_text = guess_txt(ciphertext, partial_key)
    print(f"Decrypted text (Question 11): {decrypted_text}")

    # Question 12: Decrypt binary ciphertext
    with open("cipher_sample.bin", "rb") as file:
        ciphertext = file.read()
    decrypted_text = guess_txt(ciphertext.decode(), partial_key)
    print(f"Decrypted text (Question 12): {decrypted_text}")

    # Question 13: Frequency analysis
    frequencies = analyze_frequency("english_sample.txt")
    print(f"Character frequencies (Question 13): {frequencies}")

    # Question 14: Decrypt binary file using decryption key
    with open("test.bin", "rb") as file:
        ciphertext = file.read()
    decrypted_text = ''.join([dec_key.get(char, '$') for char in ciphertext])
    print(f"Decrypted text (Question 14): {decrypted_text}")

if __name__ == "__main__":
    main()
