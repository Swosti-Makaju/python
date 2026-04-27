def remove_word(lst, word):
    result = []
    for item in lst:
        stripped = item.strip()
        if stripped != word:
            result.append(stripped)
    return result

words = [" apple ", "banana", " mango ", "apple"]
print(remove_word(words, "apple"))