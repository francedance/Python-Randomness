def anagram(s1,s2):
    
    # replace whitespaces then lower
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    # edge case check, if lengths of two strings not equal, it is not anagram!
    if len(s1) != len(s2):
        return False

    # creating a count dictionary to count on letter
    count = {}

    # counting letter in s1
    for letter in s1:
        # if a letter already exists inside count dictionay, just increment that letter by 1
        if letter in count:
            count[letter] += 1
        # if a letter is not in dictionary, just create new dictionary for that letter and add 1
        else:
            count[letter] = 1
    
    # same methods for s2, but instead we will be decrementing values. If anagram, the amount of letters in s1 and s2 should be same. 
    # Therefore, letter counts in s2 will cancel out letter counts in s1 to 0. 
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    # Checking if our dictionary is ended up 0 or not, 0 = anagran else = not anagram
    for k in count:
        if count[k] != 0:
            return False
    
    return True

# testing

print('Man Bat vs. Batman?:', anagram('Man Bat','Batman'))
print('aa vs. bb?:', anagram('aa','bb'))
