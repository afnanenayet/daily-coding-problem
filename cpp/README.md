# C++ solutions

## Synopsis

This contains my C++ solutions to daily coding problem.

## Development

I'm developing with Clang 10 on a Mac, and this isn't tested against any other
targets or compilers. Tests are run with the `Catch2` library.

On Mac I installed Catch2 with Homebrew.

To build this:

```sh
mkdir build && cd build
cmake .. -G Ninja
ninja
```

This project also uses precompiled headers to avoid the overhead of recompiling
catch2 every time we change a file.
