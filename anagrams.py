def groupanagrams(strs):
    anagrams = {}
    
    for s in strs:
        sorted_s = ''.join(sorted(s))

        if sorted_s not in anagrams:
            anagrams[sorted_s] = []

        anagrams[sorted_s].append(s)
    return list(anagrams.values())

# مثال : 

input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = groupanagrams(input_strs)

print(output)
