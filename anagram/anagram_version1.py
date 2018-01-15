def anagram(s1,s2):
    
    # removing whitespaces
    s1 = s1.replace(' ', '') 
    s2 = s2.replace(' ','')

    # edge checking. If length of both strings are equal, proceed else terminate 
    if len(s1) == len(s2):
        
        # checking if each letter in s1 is in s2
        for letter in s1:
            if letter in s2:
                letter_in_s2 = True
            else:
                letter_in_s2 = False
                       
        # checking if each letter in s2 is in s1
        for letter in s2:
            if letter in s1:
                letter_in_s1 = True
            else:
                letter_in_s1 = False
                
        # if it comes out that each letter in s1 is in s2 and vice versa, it is indeed anagram so return True!         
        if letter_in_s2 == True and letter_in_s1 == True:
            return True
        else:
            return False
    
    else:
        return False

# testing

print('Man Bat vs. Batman?:', anagram('Man Bat','Batman'))
print('aa vs. bb?:', anagram('aa','bb'))
