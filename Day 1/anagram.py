# A word or phrase that is made by arranging the letters of another word or phrase in a different order

def isAnagram(str1, str2):
    # sort the both strings and compare them
    str1Chars = sorted(str1)
    str2Chars = sorted(str2)
    str1sort = "".join(str1Chars)
    str2sort = "".join(str2Chars)
    if(str1sort == str2sort):
        return True
    return False

str1 = input()
str2 = input()

print("Given strings are anagram ? : ", isAnagram(str1, str2))