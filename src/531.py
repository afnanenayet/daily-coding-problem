"""
531, Microsoft, Easy


Using a read7() method that returns 7 characters from a file, implement
readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns
“Hello w”, “orld” and then “”.
"""

import math


def read_7(_x):
    pass


class Reader(object):
    """A reader that uses `read7()`

    We use a class so we can keep track of state
    """

    def __init__(self, file):
        # Any remaining characters that we haven't used yet
        self.overflow = ""
        self.file = file
        pass

    def read_n(self, n: int) -> str:
        """Read `n` characters from a file. We are going to use the minimum 
        number of calls to `read7()`, and save the overflowing chars.

        param n: The number of characters to read from the file
        returns: n characters from the file
        """
        num_calls = math.ceil((n - len(self.overflow)) / 7.0)
        read_buffer = ""

        for _ in range(num_calls):
            read_buffer += read_7(self.file)

        ret = self.overflow + read_buffer[:n - len(self.overflow)]
        self.overflow = read_buffer[n - len(self.overflow):]
        return ret
