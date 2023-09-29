"""
Exercise 9 - Negative Slicing

Question: Complete the script so that it prints out a list slice containing the last three items of the list letters .

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
Expected output:

['h', 'i', 'j'] 
"""

def get_last_three(_list:list)->list:
    try:
        return _list[-3:]
    except Exception:
        print("IndexError: List provided has less than 3 items.")


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(get_last_three(letters))

