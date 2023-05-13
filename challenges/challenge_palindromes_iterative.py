def is_palindrome_iterative(word):
    if (not word or len(word) == 0):
        return False
    reverse_word = ""
    word_size = len(word)
    for i in range(1, word_size + 1):
        reverse_word += word[word_size - i]
    return reverse_word == word
