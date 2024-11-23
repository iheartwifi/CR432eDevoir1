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


