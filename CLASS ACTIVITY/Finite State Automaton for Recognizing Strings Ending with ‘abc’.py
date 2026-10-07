def fsa(string):
    state = 'q0'

    for char in string:
        if state == 'q0' and char == 'a':
            state = 'q1'
        elif state == 'q1' and char == 'b':
            state = 'q2'
        elif state == 'q2' and char == 'c':
            state = 'q3'
        else:
            state = 'dead'

    return state == 'q3'


strings = ["abc", "aabc", "ababc", "abcd", "cab", "hello"]

for string in strings:
    if fsa(string):
        print(string, "-> Accepted")
    else:
        print(string, "-> Rejected")
