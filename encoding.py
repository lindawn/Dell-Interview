'''
write an algo that returns t/f given words a, b which can be an encoding, secret or translation of each other

a=banana
b=cololo
>> true

'''  



def Solution(a, b):
    mapping = {}

    if ((a is None or b is None) or len(a) != len(b)) : return False

    for i in range(len(a)):
        if a[i] in mapping:
            if mapping[a[i]] != b[i]:
                return False
        else:
            mapping[a[i]] = b[i]
    return True
    
print(Solution(None, 'noodle'))

