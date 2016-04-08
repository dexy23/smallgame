def count_words(text, words):
    result = 0
    text = text.lower()
    for word in words:
        word = word.lower()
        if word in text:
            result += 1
    return result
