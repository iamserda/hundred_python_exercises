"""
Exercise 8 - Negative Indexing

Question: Complete the script so that it prints out the letter i  using negative indexing.

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
Expected output: 

i 
"""
def get_item_at(_list:list, index:int):
    try:
        return _list[index]
    except Exception as err:
        print(err)
        pass

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(get_item_at(index=-2, _list=letters))
