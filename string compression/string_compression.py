# String compression Algorithm.
# This is simply a method of counting/telling how many certain characters are inside a string

def compress(s):
    dict = {}
    output = ''

    for i in s:
        if i not in dict:
            dict[i] = 1

        else:
            dict[i] += 1
        
    for i in dict:
        output += ((i + str(dict[i])))
        print(i, ':', dict[i])

    print(output)

# Testing'

compress('AAABBCCCDD')
compress('AAaaBBbCCCCCcDFRDFD')
