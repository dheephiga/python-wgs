'''Unique Elements: Create a function that takes a list as input and
returns a set containing only the unique elements of the list'''

def to_set(u_list):
    print(set(u_list))

user_input = input("Enter elements separated with comma:\n")
ulist = user_input.split(',')
to_set(ulist)