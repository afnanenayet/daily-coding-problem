/*
 * Find the maximum of two numbers without using any if-else statements,
 * branching, or direct comparisons.
 *
 * I did this in C++ so I could get fixed-width integers instead of the big int
 * stuff that python does.
 */

#include <stdint.h>

// The factor we shift down by to determine whether an integer is negative
const int32_t SHIFT_DOWN = 31;

/*
 * Find the maximum of `a` and `b` without using any branching comparisons
 */
constexpr int32_t maximum(int32_t a, int32_t b) {
  // We take the difference between a and b. If a is greater than b, then the
  // difference will be positive. Otherwise, it will be negative.
  int32_t diff = a - b;

  // We can check to see if a number is negative by checking the leftmost bit.
  // If b is greater than a, then this variable will be 1. Otherwise it will be
  // 0.
  int32_t b_greater = (diff >> SHIFT_DOWN) & 1;

  // If a is greater than b, then this will simplify to `a - 0`, which is a. If
  // b is greater than a, then this is a - (a - b), which is a - a + b, which is
  // b.
  return a - (b_greater * diff);
}

/*
 * Note that this is tested at compile time. To test this, simply compile the
 */
int main() {
  static_assert(maximum(0, 1) == 1);
  static_assert(maximum(10, 100) == 100);
  return 0;
}
