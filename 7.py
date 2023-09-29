# Exercise 7 - Sequence Slicing
# Question: List slicing is important in various data manipulation activities. Let's do a few more exercises on that.
# Please complete the script so that it prints out the first three items of list letters.
# input: letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# output: ['a', 'b', 'c']

def get_first_three_members(_list: list)->list:
    return _list[:3]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(get_first_three_members(letters))


