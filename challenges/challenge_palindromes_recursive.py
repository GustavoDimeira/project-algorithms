def recursive_inversor(word, low_index, high_index):
    if (low_index == high_index):
        return word[low_index]
    return recursive_inversor(word, low_index+1, high_index) + word[low_index]


def is_palindrome_recursive(word, low_index, high_index):
    if (not word or len(word) == 0):
        return False
    return (recursive_inversor(word, low_index, high_index) == word)
