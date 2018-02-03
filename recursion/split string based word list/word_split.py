## This is very weird practice but it simplt splits a string based on passed in word list

def word_split(phrase,list_of_words, output = None):
    if output is None:
        output = []
    
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            word_split(phrase[len(word):], list_of_words, output)
    return output
    pass      

print(word_split('HelloIamJae',['Hell','IamJae']))
print(word_split('BatmanisCool',['Bat','man','is','Cool']))