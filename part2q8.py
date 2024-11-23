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
