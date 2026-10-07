def fsa(string):
    state = 'q0'

    for char in string:
        if state == 'q0':
            if char == 'a':
                state = 'q1'
            else:
                state = 'q0'

        elif state == 'q1':
            if char == 'b':
                state = 'q2'
            elif char == 'a':
                state = 'q1'
            else:
                state = 'q0'

        elif state == 'q2':
            if char == 'a':
                state = 'q1'
            else:
                state = 'q0'

    return state == 'q2'


strings = ["ab", "aab", "abab", "abc", "baa", "hello"]

for string in strings:
    if fsa(string):
        print(string, "-> Accepted")
    else:
        print(string, "-> Rejected")
