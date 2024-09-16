def print_upper_words(list, must_start_with):
    """Print words from a list if it starts with the letters in must_start_with"""

    for i in list:
        for letter in must_start_with:
            if i.startswith(letter):
                print(i.upper())