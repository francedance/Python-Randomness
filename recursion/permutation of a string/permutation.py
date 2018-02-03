def permute(s):
    
    out = []
    
    if len(s) == 1:
        out = [s]
    
    else:
        # for every letter in string
        for i,let in enumerate(s):
            # For every permutation resulting from Step 2 and 3
            
            for perm in permute(s[:i] + s[i+1:]):
                out += [let+perm]
    
    return out

print('Permutation of \'abc\' is : ', len(permute('abc')))
print(permute('abc'))
print('Permutation of \'permute\' is : ', len(permute('permute')))
print(permute('permute')) ## Very large list..