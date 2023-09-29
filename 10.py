# Exercise 10 - Sequence Item Picking

# Question: Complete the script so that it prints out a list slice containing letters a, c, e, g, and i. 

# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: 

# ['a', 'c', 'e', 'g', 'i'] 

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

def get_even_index_items(_list:list)-> list:
    return [chr for i,chr in enumerate(_list) if i % 2 == 0]

print(get_even_index_items(letters))

