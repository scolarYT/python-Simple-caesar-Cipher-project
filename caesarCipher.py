def encoding(string,shift):
    new_string = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                #return chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
                new_string += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            if char.isupper():
                new_string += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            new_string += char
    return new_string
string = input("type the sentence you want to encode :")
shift = int(input("give the shift for the encoding :"))

print(encoding(string,shift))



