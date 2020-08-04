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


def optimized_zigzag(s: str, k: int) -> str:
    """Here I present a slighlty more optimized way of generating the zigzag 
    pattern. The key insight here is that we can generate each line directly,
    and that there is a pattern to the spaces and characters in a line. Every
    line starts with a number of spaces (`space_0`), followed by a character,
    then another set of spaces (`space_1`). This happens in repetition for the
    length of the string.

    For example: In line 0, we start with 0 spaces, a letter, then 5 spaces, then
    a letter, then 0 spaces. For line 1, we start with 1 space, a letter, then 3
    spaces.
    t     a     g
     h   s z   a

    So a generalized line looks like this:
    (" " * space_0) + letter + (" " * space_1) + letter ...

    You might also notice that each line starts with that line index's spaces.
    Line 0 starts with 0 spaces, line 1 starts with 1 space, and so on. Each
    line operates on a "window", that is 2 * (k - 1). We know that `space_0` is
    the line index, and we can compute `space_1` by subtracting space_0 from the
    window.

    This algorithm takes O(n * k) time, where n is the length of the input
    string. If we print the results directly, it's O(1) space. If we save the
    results, it's O(nk) space.
    """
    res = [""] * k
    window = (2 * k) - 2

    for i in range(k):
        # The iterator in the current string for the current line
        it = 0

        # The number of spaces to append to the string, that we will alternate
        # through.
        spaces = [i, window - i]

        # The index defining which number of spaces to append to the string
        which_space = 0

        while it < len(s):
            # Add the number of spaecs we've computed
            res[i] += " " * spaces[which_space]

            # Add the character from the string
            it += spaces[which_space]

            # Move the string iterator forward by the number of spaces
            res[i] += s[it]

            # Toggle which space count we're using
            which_space = (which_space + 1) % len(spaces)
    return res


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


def test_optimized_zigzag():
    s = "thisisazigzag"
    expected = [
        "t     a     g",
        " h   s z   a ",
        "  i i   i z  ",
        "   s     g   ",
    ]
    ans = zigzag(s, 4)
    assert ans == expected
    assert ans == expected
