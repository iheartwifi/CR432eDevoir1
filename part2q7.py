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

# Text from the english_sample.txt
text = """Exploring the breathtaking landscapes of the English countryside is truly a remarkable experience.
From the rolling hills covered in vibrant green to the charming little villages nestled along meandering rivers, there is an undeniable sense of tranquility and beauty.
The picturesque scenery, combined with the rich history and culture, creates a perfect blend of old-world charm and modern-day allure.
Whether you choose to stroll through the enchanting gardens, visit historic castles, or indulge in traditional afternoon tea, there is something for everyone to enjoy in this captivating destination."""


# Call the function with the example text
character_frequencies = frq_txt(text)
print(character_frequencies)
