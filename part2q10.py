# Course: CR432E - Cybersecurity with Python
# Title: Homework 1: Cryptographic Attacks
# Student 1: Wan Lan HE (student number #2295821)
# Student 2: Maxime PAQUIN (student number #2249537)

import pandas as pd

# --- QUESTION 7 ---
# Please write a function "frq_txt" which takes as input parameter a text (represented as a string)
# (see the text in the file "english_sample.txt") and will return a list of dictionaries or tuples
# (your choice ), or each symbol is associated with the associated number of occurrences. The list
# must be ordered from the most frequent character to the least frequent characters.


# Function frq_text(text) outputs the frequency of each letter in a text input
def frq_text(text):
    # Load input file
    with open(text, "r", encoding="utf-8") as file:
        text = file.read()

    # Initialize an empty dictionary
    list_of_characters = {}

    # Calculate the frequency of each letter:
    # For each letter in the input text
    for letter in text:
        # If it's already in the dict, increment it
        if letter in list_of_characters:
            list_of_characters[letter] += 1
        # Otherwise initialize it to "1"
        else:
            list_of_characters[letter] = 1

    # Get items from the list_of_characters dict (characters) with their frequencies, turn into tuples,
    # and sort them based on the frequency (item[1]) in descending (reverse) order
    sorted_list_of_characters = sorted(list_of_characters.items(), key = lambda item : item[1], reverse = True)

    # Return the sorted tuples
    return sorted_list_of_characters

# Make a character frequency list based on the English sample
sorted_characters_frequency = frq_text("english_sample.txt")


# --- QUESTION 8 ---
# Please write a function "frq_cpr" which takes as input parameter a sequence of bytes (see the file
# "cipher_sample.bin") and will return a list of dictionaries or tuples (your choice), where each symbol
# is associated with the number of associated occurrences. The list must be ordered from the most frequent
# character to the least frequent characters.


# Similar to frq_text(text), function frq_cpr(text) outputs the frequency of each byte in a binary
def frq_cpr(text):
    # Load binary and read it
    with open(text, "rb") as file:
        text = file.read()

    # Initialize an empty dictionary
    list_of_bytes = {}

    # Calculate the frequency of each byte:
    # For each byte in the input binary
    for byte in text:
        # If it's already in the dict, increment it
        if byte in list_of_bytes:
            list_of_bytes[byte] += 1
        else:
            # Otherwise initialize it to "1"
            list_of_bytes[byte] = 1

    # Get items from the list_of_characters dict (characters) with their frequencies, turn into tuples,
    # and sort them based on the frequency (item[1]) in descending (reverse) order
    sorted_list_of_bytes = sorted(list_of_bytes.items(), key=lambda item: item[1], reverse=True)

    # Return the sorted tuples and the input text
    return sorted_list_of_bytes, text

# Make a byte frequency list based on "cipher_sample.bin"
sorted_bytes_frequency, unsorted_bytes = frq_cpr("cipher_sample.bin")


# --- QUESTION 9 ---
# When matching the two ordered lists, please compare the plain text to the encrypted text.
# (No Python code, it would need an explanation)

# The two frequency lists are the same. The first one shows the frequency of each letter in an unencrypted English
# sample, whereas the second one shows the same frequency for the byte-equivalent of each character.

'''
# Create a dataframe to display character and byte frequencies in a table
data = {
    "Character": [f"\"{char[0]}\"" for char in sorted_characters_frequency],
    "Byte": [byte[0] for byte in sorted_bytes_frequency],
    "Frq char": [char[1] for char in sorted_characters_frequency],
    "Frq byte": [byte[1] for byte in sorted_bytes_frequency],
}

df = pd.DataFrame(data)

print(df)
'''

# If we uncomment and run the ABOVE code segment (between the ''' ''' quotes),
# we can visualize this more easily in its output (below):
#
#   Character  Byte  Frq char  Frq byte
#0        " "   155        84        84
#1        "e"     1        64        64
#2        "t"   253        45        45
#3        "n"    49        43        43
#4        "i"     9        41        41
#5        "r"    92        40        40
#6        "a"   243        34        34
#7        "o"   208        32        32
#8        "l"    74        28        28
#9        "s"   122        27        27
#10       "h"   154        26        26
#11       "d"   143        19        19
#12       "c"   193        18        18
#13       "g"    72        15        15
#14       "u"    22        13        13
#15       "y"    25        10        10
#16       "m"    62         8         8
#17       "b"   103         7         7
#18       "v"   110         7         7
#19       "p"   211         6         6
#20       "f"    57         6         6
#21       ","   215         6         6
#22       "."    36         4         4
#23      "\n"    31         3         3
#24       "E"   196         2         2
#25       "x"    94         2         2
#26       "k"    56         2         2
#27       "q"    84         2         2
#28       "w"   108         2         2
#29       "-"   127         2         2
#30       "F"   227         1         1
#31       "T"   176         1         1
#32       "W"    99         1         1
#33       "j"    13         1         1


# --- QUESTION 10 ---
# Since encryption is done via a key in dictionary form (e.g., key={'a': b'2d', ...}), decryption is done
# with an inverted key (e.g., key={b'2d' : 'a', ...}), based on the observation made in the previous question,
# please write a function “build_dec_key” which will cover the partial decryption key.

# Function build_dec_key(sorted_bytes_frequency, sorted_characters_frequency, key_length=17) builds a partial
# decryption key based on frequency analysis.
def build_dec_key(sorted_bytes_frequency, sorted_characters_frequency, key_length=17):
    # Initialize an empty dictionary for the decryption key
    partial_decryption_key = {}

    # Looking only at the first element of the tuples (byte / char), zip both frequency lists and match bytes
    # to characters using the first/top 17 most frequent matches ([:key_length]).
    for (byte, _), (char, _) in zip(sorted_bytes_frequency[:key_length], sorted_characters_frequency[:key_length]):
        partial_decryption_key[byte] = char

    # Return the partial decryption key
    return partial_decryption_key

# Call build_dec_key(sorted_bytes_frequency, sorted_characters_frequency), save the result to partial_decryption_key,
# then print a blank line and the partial decryption key.
partial_decryption_key = build_dec_key(sorted_bytes_frequency, sorted_characters_frequency)
print("")
print(f"Partial decryption key: {partial_decryption_key}.")


# --- QUESTION 11 ---
# Please implement a "guess_txt" function having as inputs the ciphertext as well as a partial
# decryption key of the most frequent characters made based on the frequencies of the base English text.
# If a character cannot be deciphered, you can match with “$”. The length of the partial key with which
# the test will be carried out is 17.

# Function guess_txt(ciphertext, decryption_key) uses "partial_decryption_key" from question 10 to guess the
# unencrypted version of the inputted ciphertext.
def guess_txt(ciphertext, decryption_key):

    # Go over each byte in "ciphertext" and match each one to its character equivalent if possible, otherwise
    # output "$", then combine all the characters in a string using join() with an empty string as a separator,
    # and save that to "guessed_text".
    guessed_text = ''.join(decryption_key.get(byte, '$') for byte in ciphertext)

    # Return the partially decrypted text.
    return guessed_text


# --- QUESTION 12 ---
# Please test the “guess_txt” function on the “cipher_sample.bin” file.

# Using the input from cipher_sample.bin we got in question 8 via frq_cpr("cipher_sample.bin") with the partial
# decryption key from question 10 via build_dec_key(sorted_bytes_frequency, sorted_characters_frequency).

# Generate a partially decrypted text using guess_txt() and passing it "cipher_sample.bin" and the partial key.
guessed_text = guess_txt(unsorted_bytes, partial_decryption_key)

# Print a blank line followed by the partially decrypted text.
print("")
print(f"Guessed text: {guessed_text}.")


# --- QUESTION 13 ---
# Please deduce words or phrases from the frequency analysis of the “ english_sample.txt” file,
# this will allow you to recover the decryption key.

# The output is:
# Guessed text: $$$loring the $reathta$ing landsca$es o$ the $nglish countryside is truly a remar$a$le
# e$$erience$$$rom the rolling hills co$ered in $i$rant green to the charming little $illages nestled along
# meandering ri$ers$ there is an undenia$le sense o$ tran$uility and $eauty$$$he $ictures$ue scenery$ com$ined $ith
# the rich history and culture$ creates a $er$ect $lend o$ old$$orld charm and modern$day allure$$$hether you choose
# to stroll through the enchanting gardens$ $isit historic castles$ or indulge in traditional a$ternoon tea$ there
# is something $or e$eryone to en$oy in this ca$ti$ating destination$.

# Function expand_key() expands the  partial decryption key by comparing the English sample and "cipher_sample.bin".
def expand_key(ciphertext, partial_decryption_key, sorted_bytes_frequency, sorted_characters_frequency, sample):
    # Make a copy of the partial key
    expanded_decryption_key = partial_decryption_key.copy()

    # Create a set of bytes that have already been mapped to characters
    mapped_characters = set(partial_decryption_key.values())

    # Looking only at the first element of the tuples (byte / letter), zip both frequency lists and match bytes to
    # characters.
    for (byte, _), (letter, _) in zip (sorted_bytes_frequency, sorted_characters_frequency):
        # If the byte and letter have not already been mapped
        if byte not in expanded_decryption_key and letter not in mapped_characters:
            # Map the byte to the letter in "expanded_decryption_key"
            expanded_decryption_key[byte] = letter

            # Add the letter to the "mapped_characters" set
            mapped_characters.add(letter)

    # Return the expanded key
    return expanded_decryption_key

# Expand the decryption key using the partial one
expanded_decryption_key = expand_key(bytes(unsorted_bytes), partial_decryption_key, sorted_bytes_frequency, sorted_characters_frequency, "english_sample.txt")

# Print full decryption key
print("")
print(f"Full decryption key: {expanded_decryption_key}")

# Try to decrypt "cipher_sample.bin" again with guess_txt(), passing it "cipher_sample.bin" and the full key.
decrypted_text = guess_txt(bytes(unsorted_bytes), expanded_decryption_key)

# Print a blank line followed by the decrypted text using the expanded decryption key.
print("")
print(f"Fully decrypted text (cipher_sample.bin): {decrypted_text}")


# --- QUESTION 14 ---
# Please repeat the test using the decryption key on the “test.bin” file and deduce
# as many words as possible in plain text rom.

# Get the content of the "test.bin" file and save it to "testbin_unsorted_bytes", ignoring the frequency list.
_ , testbin_unsorted_bytes = frq_cpr("test.bin")

# Try to decrypt test.bin with guess_txt(), passing it "test.bin" and the full key.
decrypted_text = guess_txt(bytes(testbin_unsorted_bytes), expanded_decryption_key)

# Print a blank line followed by the decrypted text using the expanded decryption key.
print("")
print(f"Fully decrypted text (test.bin): {decrypted_text}")

# The output is:
#
#Fully decrypted text: $ello there$ $ hope you are having a wonderful day.
#$ wanted to take a moment to express my gratitude for your presence here.
#$t is truly a pleasure to assist you with any questions or tasks you may have.
#Whether it is providing information, helping you find solutions, or simply engaging in a friendly conversation, $$m here to make your experience enjoyable and stress-free.
#Feel free to reach out to me anytime, and $$ll be more than glad to lend a helping hand. Take care and have a fantastic day ahead$

# We can probably assume that the final text is:
#
#Hello there! I hope you are having a wonderful day.
#I wanted to take a moment to express my gratitude for your presence here.
#It is truly a pleasure to assist you with any questions or tasks you may have.
#Whether it is providing information, helping you find solutions, or simply engaging in a friendly conversation, I'm here to make your experience enjoyable and stress-free.
#Feel free to reach out to me anytime, and $$ll be more than glad to lend a helping hand. Take care and have a fantastic day ahead!