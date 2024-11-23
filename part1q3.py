#Encryption: Plaintext is combined with a secret key to produce scrambled data (ciphertext).
#Decryption: The ciphertext and the same secret key are used to revert the scrambled data back to the original plaintext.

def decrypt(cipher, key, word_dict):
    ans = ""
    give_point = {}
    max_point = 0
    final_key = None
    final_text = ""

    for c in cipher:
        if c.islower():
            l = ord(c) - ord("a")
            l = (l - key) % 26 + 97
        elif c.isupper():
            l = ord(c) - ord("A")
            l = (l - key) % 26 + 65
        else:
            l = ord(c)
        ans += chr(l)

    print("key =", key)
    print("Decrypted Text:", ans)

    word_array = ans.split()

    for word in word_array:
        if word in word_dict:
            if key in give_point:
                give_point[key] += 1
                if max_point < give_point[key]:
                    max_point = give_point[key]
                    final_key = key
                    final_text = ans
            else:
                give_point[key] = 1

    print("\nDecryption: ")
    print("Final key: ", final_key)
    print("Decrypted message: ")
    print(final_text)

# Example usage
cipher_text = "gpkyfe zj r kilcp nfeuviwlc crexlrxv"  # Example cipher text
key = 2  # Example key for decryption
word_dict = {"There", "is", "a", "secret", "message"}  # Example word dictionary
decrypt(cipher_text, key, word_dict)
