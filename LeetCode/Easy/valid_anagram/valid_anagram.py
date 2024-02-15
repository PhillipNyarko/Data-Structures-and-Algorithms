def isAnagram(s, t):
# if the two strings are anagrams, when sorted they should be the same
    if sorted(s) == sorted(t): 
        return True
    return False
