def uni_char_(s):
    if len(set(s)) == len(s):
         return 'The String is UNIQUE!'
    else:
        return 'The String is NOT UNIQUE!'


# Testing
print(uni_char('abcde'))
print(uni_char('aabcd'))
