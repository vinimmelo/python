def is_balanced(parenthesis) -> str:
    positions = [False for x in parenthesis]
    for x in range(len(positions)):
        if parenthesis[x] == '(':
            for y in range(len(positions) -1, 0, -1):
                there_is_my_other_half = parenthesis[y] == ')' and not positions[y] and not positions[x]
                if there_is_my_other_half:
                    positions[y], positions[x] = True, True
    print(positions)
    return 'false' if False in positions else 'true'


input1 = '(())()()'
input2 = '((()))'
input3 = ')))((('

print(is_balanced(input1))
print(is_balanced(input2))
print(is_balanced(input3))
