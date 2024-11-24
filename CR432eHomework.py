# Course: CR432E - Cybersecurity with Python
# Title: Homework 1: Cryptographic Attacks
# Student 1: Wan Lan HE (student number #2295821)
# Student 2: Maxime PAQUIN (student number #2249537)

import argparse
import os

# Initialization of global variables
letters_in_alphabet = 26
change_to_index = 1 # To shift starting at index 0 to index 1


# --- QUESTION 1 ---
# Please write an “encrypt” function which takes as input a (plain) text composed of a sequence of ASCII characters
# [a z] and a key and which returns the encrypted text via the Caesar code.


# Function argument_validation(arguments) to test that arguments are all correctly included and valid
def argument_validation(arguments):
    # print(f"Arguments: {arguments}") # For diagnostics purposes

    tests = {"input_test_passed": True,
             "arguments_min1_test_passed": True,
             "arguments_only1_test_passed": True,
             "key_exists_test_passed": True,
             "key_not_multiple_of_26_or_0_test_passed": True,
             "key_without_bruteforce_test_passed": True,
             "bruteforce_test_passed": True
             }

    list_of_errors = []

    # Argument validation
    # Check input
    match arguments.input:
        case None | "":
            list_of_errors.append("Input missing. Specify --input INPUT or -i INPUT. The input must be a string or the path to the input file.")
            tests["input_test_passed"] = False

    # Check encryption flag (need at least one flag, but not both)
    encryption_mode = ""
    match arguments.encrypt, arguments.decrypt, arguments.bruteforce:
        # Case 1 -- both missing
        case (None, None, *rest) | (False, False, *rest) | (False, None, *rest) | (None, False, *rest):
            list_of_errors.append("Encryption flag missing. Specify --encrypt (or -e) to encrypt or --decrypt (or -d) to decrypt.")
            tests["arguments_min1_test_passed"] = False

        # Case 2 -- both included
        case (True, True, *rest):
            list_of_errors.append("Only one encryption flag can be specified. Choose --encrypt (or -e) to encrypt or --decrypt (or -d) to decrypt.")
            tests["arguments_only1_test_passed"] = False

        # Case 3a -- encryption mode, bruteforce enabled
        case (True, False, True):
            encryption_mode = "encryption"
            list_of_errors.append(
                "Bruteforce mode (--bruteforce or -b) cannot be combined with encryption mode (--encrypt or -e).")
            tests["bruteforce_test_passed"] = False

        # Case 3b -- encryption mode, no bruteforce
        case (True, False, False) | (True, False, None):
            encryption_mode = "encryption"

        # Case 4 -- decryption mode
        case (False, True, *rest):
            encryption_mode = "decryption"

    # Check key
    # Case - No key
    if arguments.key in (None, "") and arguments.bruteforce in (None, False):
            list_of_errors.append("Key missing. Specify --key KEY or -k KEY. The key must be an integer.")
            tests["key_exists_test_passed"] = False

    # Case - Key exists
    elif arguments.key is not None:
                # Case - Key is a multiple of 0 or 26
                if abs(arguments.key) % letters_in_alphabet == 0 or abs(arguments.key) == 0:
                    list_of_errors.append("Full rotation. The plaintext and ciphertext are identical. Choose another key.")
                    tests["key_not_multiple_of_26_or_0_test_passed"] = False
                # Case - Key exists and bruteforce is enabled
                if arguments.bruteforce == True:
                    list_of_errors.append("Cannot combine a key with bruteforce mode.")
                    tests["key_without_bruteforce_test_passed"] = False

    all_tests_passed = True

    for test in tests:
        if tests[test] == False:
            all_tests_passed = False

    return all_tests_passed, encryption_mode, list_of_errors


# Function encrypt(plain, key) takes a string of plain text and an integer as a key to return a Caesar cipher
def encrypt(plain, key):
    # Initialization of an empty string
    encrypted = ""

    # Caesar cipher
    for letter in plain:
        # Ensure we only encrypt a-z lowercase letters
        if 'a' <= letter <= 'z':
            # Turning the letter into an ordinal
            letter_to_ordinal = ord(letter)
            letter_to_ordinal_0_25 = ord(letter) - ord('a')

            # Adding the key
            ord_plus_key = (letter_to_ordinal_0_25 + key) % letters_in_alphabet

            # Turning ord_plus_key back into a character
            new_character = chr(ord_plus_key + ord('a'))

            # Adding the new character to a variable
            encrypted += new_character

        # If the character is not a-z lowercase (e.g. "1", "!", "#", "A", "B", etc.)
        else:
            # Append the character without encrypting it
            encrypted += letter

    # Return the Caesar cipher
    return encrypted


# --- QUESTION 2 ---
# Please write a “decrypt” function that takes ciphertext and a key as inputs and returns the plaintext via Caesar code.

def decrypt(ciphertext, key):
    # Initialization of an empty string
    decrypted = ""

    # Decryption of the Caesar cipher
    for letter in ciphertext:

        #Ensure we only decrypt a-z lowercase letters
        if 'a' <= letter <= 'z':

            # Turning the letter into an ordinal
            letter_to_ordinal = ord(letter)
            letter_to_ordinal_0_25 = ord(letter) - ord('a')

            # Subtracting the key
            ord_minus_key = (letter_to_ordinal_0_25 - key) % letters_in_alphabet

            # Turning ord_plus_key back into a character
            new_character = chr(ord_minus_key + ord('a'))

            # Adding the new character to a variable
            decrypted += new_character

        # If the character is not a-z lowercase (e.g. "1", "!", "#", "A", "B", etc.)
        else:
            # Append the character without decrypting it
            decrypted += letter

    # Return the decrypted text
    return decrypted


# --- QUESTION 3 ---
# What is the relationship between encryption and decryption?

# The Caesar cipher from the intro and questions 1 and 2 is an example of symmetric encryption,
# which uses the same key to encrypt and to decrypt. For symmetric encryption, both people need to agree on a key
# in advance of communicating. The sender takes a plaintext, adds the key (for example +2, or shift 2 positions to
# the right), converts their plaintext into ciphertext, then sends this to the receiver. Then, the received takes
# the ciphertext, subtracts the key, and ends up with the original plaintext. For example, using a key of "+3"
# (or "shift 3 positions to the right"), the sender converts "abc" into "def". The receiver would then subtract 3
# to each letter (or shift 3 positions to the left) and get the original text: "abc".


# --- QUESTION 4 ---
# Using the “argparse” module, please create a setting for your script such that it can take a character string as
# input or a file containing text and return a message or an encrypted file as output.

# Function main() using argparse to parse arguments
def output_message(arguments, tests, mode, errors):
    # Initialize empty arrays and variables
    outputs = []
    result = ""
    mode_adjective = ""

    print("")
    # If all tests pass
    if tests:
        print("All tests passed.")
        print("")

        # And if the mode is "encryption"
        if mode == "encryption":
            mode_adjective, result = "encrypted", encrypt(arguments.input, arguments.key)

        # Or if the mode is "decryption" and the bruteforce flag is not set
        elif mode == "decryption" and arguments.bruteforce == False:
            mode_adjective, result = "decrypted", decrypt(arguments.input, arguments.key)

        # Or if the mode is "decryption" and the bruteforce flag is set
        elif mode == "decryption" and arguments.bruteforce:
            outputs.append("Bruteforce results:")
            bruteforce_results = brute_force(arguments.input)
            for key, plaintext in bruteforce_results.items():
                outputs.append(f"Using key \"{key}\": \"{plaintext}\".")
            for output in outputs:
                result += output + "\n"

        # Append the final result to the outputs array
        if arguments.bruteforce is None or arguments.bruteforce == False:
            outputs.append(f"The {mode_adjective} version of \"{arguments.input}\" with key \"{arguments.key}\" is: \"{result}\"")

        # If there is an --output (or -o) argument
        if arguments.output:
            # Write the output to a file
            with open(arguments.output, "w", encoding="utf-8") as output_file:
                output_file.write(result)
                # Append a message to the outputs
                outputs.append("")
                outputs.append(f"Output successfully written to \"{arguments.output}\".")

    # If tests fail
    else:
        outputs.append(f"Error. The following {'test has' if len(errors) < 2 else 'tests have'} failed:")
        for i, error in enumerate(errors, start=1):
            outputs.append(f"{i} - {error}")
        outputs.append("* - Specify --help (or -h) to read the help file.")

    outputs.append("") # Final line break to make it breathe

    # Print all outputs to the console
    for output in outputs:
        print(output)

def main():
    # Based on https://docs.python.org/3/library/argparse.html
    # and https://docs.python.org/3/howto/argparse.html

    # Get arguments and parse them
    parser = argparse.ArgumentParser(description="This script encrypts or decrypts user-provided text based on a user-provided key.",
                                    epilog="Example: '-i \"test\" -e -k 3' should return 'whvw'.")

    # Possible arguments, including their type and help text
    parser.add_argument('-i', '--input', type=str, help="Enter a string or the path to the input file.")
    parser.add_argument('-o', '--output', type=str, help="Optional. Enter the path to the output file.")
    parser.add_argument('-e', '--encrypt', action='store_true', help="Enter the plaintext to encrypt.")
    parser.add_argument('-d', '--decrypt', action='store_true', help="Enter the ciphertext to decrypt.")
    parser.add_argument('-k', '--key', type=int, help="Enter the secret key. The key must be an integer.")
    parser.add_argument('-b', '--bruteforce', action='store_true', help="Optional. Enable bruteforce mode.")

    # Saving the parsed arguments to the "arguments" variable
    arguments = parser.parse_args()

    print("")

    if arguments.input is not None:
        if os.path.isfile(arguments.input):
            with open(arguments.input, 'r', encoding='utf-8') as file:
                print(f"Successfully loaded input file \"{arguments.input}\".")
                arguments.input = file.read()
        else:
            print(f"Using input string \"{arguments.input}\".")

            print("")
            arguments.input = arguments.input.lower()
            print(f"Input converted to lowercase: \"{arguments.input}\".")

    # Validate that all tests passed the encryption mode (mode), and get a list of errors (errors), if any
    tests, mode, errors = argument_validation(arguments)

    # Print results
    output_message(arguments, tests, mode, errors)


# --- QUESTION 5 ---
# Please add to your script a “brute_force” function, which will take an encrypted message as input and return a
# dictionary having the encryption key values as keys and the plaintext values as values (e.g., {k0: plain text0,
# k1: plain _text1, ..., kn: plain_textn})

# Function brute_force(ciphertext) to go through the 26 combinations, add the results to a dictionary, and return the dictionary
def brute_force(ciphertext):
    bruteforce_results = {}
    for key in range(1, letters_in_alphabet):
        decrypted_text = decrypt(ciphertext, key)
        bruteforce_results[key] = decrypted_text
    return bruteforce_results


# --- QUESTION 6 ---
# By testing the “brute_force” function with the intercepted message, please deduce the key value as
# well as the plaintext message.

# When running the script with the '-i "gpkyfe zj r kilcp nfeuviwlc crexlrxv" -d -b' arguments, we get these results:
# Using key "1": "fojxed yi q jhkbo medtuhvkb bqdwkqwu".
# Using key "2": "eniwdc xh p igjan ldcstguja apcvjpvt".
# Using key "3": "dmhvcb wg o hfizm kcbrsftiz zobuious".
# Using key "4": "clguba vf n gehyl jbaqreshy ynathntr".
# Using key "5": "bkftaz ue m fdgxk iazpqdrgx xmzsgmsq".
# Using key "6": "ajeszy td l ecfwj hzyopcqfw wlyrflrp".
# Using key "7": "zidryx sc k dbevi gyxnobpev vkxqekqo".
# Using key "8": "yhcqxw rb j caduh fxwmnaodu ujwpdjpn".
# Using key "9": "xgbpwv qa i bzctg ewvlmznct tivociom".
# Using key "10": "wfaovu pz h aybsf dvuklymbs shunbhnl".
# Using key "11": "veznut oy g zxare cutjkxlar rgtmagmk".
# Using key "12": "udymts nx f ywzqd btsijwkzq qfslzflj".
# Using key "13": "tcxlsr mw e xvypc asrhivjyp perkyeki".
# Using key "14": "sbwkrq lv d wuxob zrqghuixo odqjxdjh".
# Using key "15": "ravjqp ku c vtwna yqpfgthwn ncpiwcig".
# Using key "16": "qzuipo jt b usvmz xpoefsgvm mbohvbhf".
# Using key "17": "python is a truly wonderful language". # <--- The key is 17 and this is the original message.
# Using key "18": "oxsgnm hr z sqtkx vnmcdqetk kzmftzfd".
# Using key "19": "nwrfml gq y rpsjw umlbcpdsj jylesyec".
# Using key "20": "mvqelk fp x qoriv tlkabocri ixkdrxdb".
# Using key "21": "lupdkj eo w pnqhu skjzanbqh hwjcqwca".
# Using key "22": "ktocji dn v ompgt rjiyzmapg gvibpvbz".
# Using key "23": "jsnbih cm u nlofs qihxylzof fuhaouay".
# Using key "24": "irmahg bl t mkner phgwxkyne etgzntzx".
# Using key "25": "hqlzgf ak s ljmdq ogfvwjxmd dsfymsyw".

# The original message is "python is a truly wonderful language" and the key is "17".

# On start, run main()
if __name__ == "__main__":
    # Call main()
    main()