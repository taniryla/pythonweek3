words_set = {"Alpha", "Bravo", "Charlie"}
"""
numbers_set = {1, 2, 3, 4, 4}
numbers_set = {1, 2, 3, 4, [5, 6]}
numbers_set = {1, 2, 3, 4, (5, 6)}
print(numbers_set)

abcd = ""
for word in words_set:
    abcd += word
print(abcd)
if "Alpha" in words_set:
    print("Alpha is in set")
else:
    print("Alpha not in set")
"""
words_set.add("Delta")
print(words_set)
words_set.discard("Bravo")
print(words_set)