def anagram(s1,s2):
    
    # replace whitespaces then lower
    # it is imported to convert all strings to lowercase since when sorted, 'a' and 'A' is different!
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    # If two strings are anagrams of each other,then their sorted values should be exactly same!
    return sorted(s1) == sorted(s2)

# testing

print('Man Bat vs. Batman?:', anagram('Man Bat','Batman'))
print('aa vs. bb?:', anagram('aa','bb'))
