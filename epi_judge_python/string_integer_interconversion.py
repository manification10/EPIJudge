from test_framework import generic_test
from test_framework.test_failure import TestFailure



def int_to_string(x: int) -> str:
    if x == 0:
        return '0'
    is_negative = False
    if x < 0:
        x = -x
        is_negative = True
    s= []
    while x:
        s.append(chr(ord('0')+x%10))
        x //= 10
    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s: str) -> int:
    formedInt = 0
    is_negative = False
    i = 0
    if s[0] == '-':
        is_negative = True
        i = 1
    elif s[0] == '+':
        i = 1

    while i < len(s):
        formedInt = formedInt*10 + ord(s[i]) - ord('0')
        i+=1

    if is_negative:
        formedInt = -formedInt
    return formedInt







def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
