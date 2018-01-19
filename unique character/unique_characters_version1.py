def uni_char(s):
    
   for i in range(len(s)):
       start = s[i]
       
       if start in s[i+1:]:
           return 'The String is NOT UNIQUE!'
       else:
           return 'The String is UNIQUE!'
    


   



# Testing
print(uni_char('abcde'))
print(uni_char('aabcd'))

