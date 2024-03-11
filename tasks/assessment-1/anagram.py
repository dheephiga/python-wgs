raw_data = input()
r_list = raw_data.split(' ')
anagrams = {}


def find_anagrams(raw_list):
    list_copy = raw_list.copy()
    
    for i in raw_list:
        # word_value = raw_list[i]
        word = sorted(list(i))   
        word.reverse()
        word_key = ''.join(word)

        if word_key in anagrams:
            if isinstance(anagrams[word_key], list):
                anagrams[word_key].append(i)
            else:
                anagrams[word_key] = [anagrams[word_key], i]
        else:
            anagrams[word_key] = i
        # print(word)
        # print(word_value)
        # anagrams.update({word:word_value})
    
    print(anagrams)
        
        
find_anagrams(r_list)
# anagrams.update({sorted(r_list[0]):r_list[0]})