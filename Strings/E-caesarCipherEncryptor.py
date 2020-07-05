def caesarCipherEncryptor(string, key):
    result = []
    for ch in list(string):
        newCh = (ord(ch) - ord('a') + key) % 26 + ord('a')
        result.append(chr(newCh))
    print(result)
    return "".join(result) 

print(caesarCipherEncryptor("xyz", 2))
