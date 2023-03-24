def is_palindrome_iterative(word):
    if word == '':
        return False

    low_index = 0
    high_index = len(word) - 1

    while low_index < high_index:
        if word[low_index] == word[high_index]:
            low_index += 1
            high_index -= 1
        else:
            return False
    return True
