words = ["eat", "tea", "tan", "ate", "nat", "bat", "tab", "ran"]
words = ["racecar", "racecar", "silent", "listen", "heart", "earth"]

output = []

def anagram_search(words):
    anagram_list = [words[0]]

    for i in range(1, len(words)):
        if(sorted(words[i]) == sorted(words[0])):
            anagram_list.append(words[i])

    return anagram_list

def group_anagrams(words):
    while len(words) > 0:
        current_anagram_set = anagram_search(words)
        output.append(current_anagram_set)
        words = [i for i in words if i not in current_anagram_set]

    return output

print(group_anagrams(words))
