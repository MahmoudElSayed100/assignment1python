def char_frequency(s):
    result = {}
    for char in s:
        if char in result:
            result[char]+=1
        else:
            result[char]=1
    return result

print(char_frequency("Mahmoud El Sayed"))