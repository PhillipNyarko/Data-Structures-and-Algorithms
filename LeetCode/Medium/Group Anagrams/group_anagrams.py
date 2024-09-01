words = ["eat","tea","tan","ate","nat","bat"]
output = []

def group_anagrams(words):
    for i in range(len(words)):
        output.append([words[i]])
        print(output)
        for j in range(1, len(words)):
            print("comparing " + output[i][i] + " with " + words[j])
            if(sorted(output[i][i]) == sorted(words[i + j])):
                output[i].append(words[i + j])

    return output

group_anagrams(words)
