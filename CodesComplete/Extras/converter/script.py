# Should receive a string and convert into another format.

from collections import Counter


def dictionary_converter(word: str) -> dict:
    counter = Counter(word)
    return counter


def string_converter(word: str) -> str:
    counter = 0
    actual_letter = word[0]
    final_result = ''
    for i in range(len(word)):
        if word[i] == actual_letter:
            counter += 1

        finish_letter = word[i] != actual_letter or i == (len(word) - 1)
        if finish_letter:
            final_result += str(counter)
            final_result += actual_letter
            counter = 1
            actual_letter = word[i]

    return final_result

