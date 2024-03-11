user_input = input()
palindrome = {}
input_list = user_input.split()  
def find_palindromes(in_list):
    for word in in_list:
        word_r = word[::-1] 
        if word == word_r:
            word_len = len(word)
            
            if word_len in palindrome:
                palindrome[word_len].append(word)
            else:
                palindrome[word_len] = [word]  

    print(palindrome)

find_palindromes(input_list)
