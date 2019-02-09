def is_anagram(first, second) -> bool:
    counter_first = {x: first.count(x) for x in first}
    counter_second = {x: second.count(x) for x in second}
    for x in counter_first:
        if counter_first[x] != counter_second[x]:
            return False
    return True


first_word = input()
second_word = input()

result = is_anagram(first_word, second_word)
print(result)
