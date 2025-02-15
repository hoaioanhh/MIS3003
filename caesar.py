def caesar(text, k):
    result  = ""
    for char in text:
        if char.isalpha(): 
            if char.isupper():
                shift=65
            else:
                shift=97
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char  
    return result

k = 21
text = "Nguyen Thi Hoai Oanh"
mahoa = caesar(text, k)

print("ma hoa caesar:", mahoa)

