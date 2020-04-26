""" Problem #521

(From Paypal)



Given a string and a number of lines k, print the string in zigzag form. In 
zigzag, characters are printed out diagonally from top left to bottom right 
until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

```txt
t     a     g
 h   s z   a
  i i   i z
   s     g
```
"""


def zigzag(s: str, k: int) -> str:
    """The naive method of doing the zigzag is to simply iterate through the
    string one character at a time, and add to the lines as necessary. This is
    O(nk) time and O(nk) space, since each line is going to be as long as the
    size of the input string, and we have to add to each string in every
    iteration of the loop.
    """
    # The result that we're going to return. It's a list of strings, which
    # represents each line of the input, where res[0] is the top line and
    # res[-1] is the bottom line.
    res = [""] * k
    target_line_number = 0
    add = 1

    # Iterate through the string. We can determine which line number a character
    # will be added to by its index in the string.
    for i, char in enumerate(s):
        # We need to "zigzag" which line we're appending to. Once we hit the
        # bottom (0), we change the line number iterator to start moving up.
        # Once we hit the # ceiling (k -1), we change the line number iterator
        # to start moving down, achieving the "zigzag" effect.
        if target_line_number == 0:
            add = 1
        elif target_line_number == k - 1:
            add = -1

        for line_number in range(len(res)):
            if line_number == target_line_number:
                res[line_number] += char
            else:
                res[line_number] += " "
        target_line_number += add
    return res


def test_zigzag():
    s = "thisisazigzag"
    expected = [
        "t     a     g",
        " h   s z   a ",
        "  i i   i z  ",
        "   s     g   ",
    ]
    ans = zigzag(s, 4)
    assert ans == expected
