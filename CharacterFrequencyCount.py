str = "Africa"

#using Dictionary
def char_frequency_dict(s): 
    freq = {} 
    for char in s: 
        if char in freq: freq[char] += 1 
        else: freq[char] = 1 
    return freq 
print(char_frequency_dict(str)) 

#Using dict.get()
def char_frequency_get(s): 
    freq = {} 
    for char in s:
        freq[char] = freq.get(char, 0) + 1 
    return freq

print(char_frequency_get(str))

#Using collections.Counter
from collections import Counter
def char_frequency_counter(s): 
    return dict(Counter(s)) 
frequency_counter = char_frequency_counter(str)
print(frequency_counter)

#Using str.count()
def char_frequency_count(s): 
    freq = {} 
    for char in set(s):
        freq[char] = s.count(char) 
        return freq 
print(char_frequency_count(str))



