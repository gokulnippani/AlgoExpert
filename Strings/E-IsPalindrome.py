def isPalindrome(string):
    startIdx,endIdx = 0, len(string)-1
    while startIdx < endIdx:
        if string[startIdx] != string[endIdx]:
            return False 
        startIdx += 1
        endIdx -= 1
    return True

print(isPalindrome("abcdcba"))