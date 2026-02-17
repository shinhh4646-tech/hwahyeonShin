import collections

# a) Frequency Dictionary 
def firstUniqChar_freq_dict(s: str) -> int:
    if not s:
        return -1
    count_map = collections.Counter(s)
    
    for index, char in enumerate(s):
        if count_map[char] == 1:
            return index

# b) Ordered dictionary

def firstUniqChar_ordered(s: str) -> int:
    if not s:
        return -1
    info_map = {}
  
    for i, char in enumerate(s):
        if char not in info_map:
            info_map[char] = [1, i] 
        else:
            info_map[char][0] += 1
   
    for char in info_map:
        count, index = info_map[char]
        if count == 1:
            return index
            
    return -1