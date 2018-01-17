def rev_word(s):

    words = [] # stores words from string
    length = len(s) # stores length of string passed in
    space = [' '] # list with whitespace in it

    i = 0 # starting index

    while i < length: # while loop to go through whole string 
        if s[i] not in space: # if current index position is not a whitespace

            word_start = i # simply word_starts are 'i' index position

            while i < length and s[i] not in space: # while loop until it hits a whitespace

                i += 1 # move forward in a string

            words.append(s[word_start:i]) # when while loop is done, append word into words[]
        
        i += 1 # increment index by one if current index position is a whitespace

    print(" ".join(reversed(words))) # just print words in words[] in reversed order (reversed() is Python trick!)

# Testing

rev_word('The string reversed of this string')
