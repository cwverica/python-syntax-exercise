def print_upper_words(words, must_start_with={'e'}):
    """Prints every word in the list that starts with given starting
    letters in upper case. Returns nothing

    -words: list of words to be printed
    -must_start_with (optional): letters must be lowercase a set of
        letters to check starting letter of each word against.
        (default = 'e')"""

    for word in words:
        if word[0].lower() in must_start_with:
            print(word.upper())



print_upper_words(["Everyone", "else", "loves", "elephants", "ExCepT", "you"])
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "y"})

