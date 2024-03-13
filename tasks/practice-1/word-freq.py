''' Write a function that takes a list of
words as input and returns a dictionary where keys are unique words
and values are their frequencies in the list.'''

word_freq = {}
def frequency(r_list):
    for word in r_list:
        if word in word_freq:
            word_freq[word] += 1
        
        else:
            word_freq.update({word:1})  
    
    print(word_freq) 

user_input = input("Enter word separated with comma:\n")
ulist = user_input.split(',')
frequency(ulist)
