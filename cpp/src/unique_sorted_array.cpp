/*
 * Given an array, return an sorted array containing unique integers in sorted
 * order from the first array.
 */

#include "pch.hpp"

// Given an array of inputs, we sort the array, and then do a linear scan to
// only include unique elements and discard elements that are not unique
//
// @param inputs: A list of numbers
// @returns The effective length of the returned array
template <auto size> size_t unique_sort(std::array<int, size> &inputs) {
    // First, we sort the array in place, this is O(nlogn)
    std::sort(inputs.begin(), inputs.end());

    // The length of the resulting unique array
    size_t result_size{1};

    // Iterate through the array, incrementing the the `result_size` as we find
    // unique elements.
    // We start at 1, knowing that a std::array can't have a size of 0
    for (size_t i = 1; i < inputs.size(); i++) {

        // We add elements by swapping into the last element if the current
        // element in the array we're iterating isn't equal to the last element
        // in the results array
        if (inputs[result_size - 1] != inputs[i]) {
            inputs[result_size] = inputs[i];
            result_size++;
        }
    }
    return result_size;
}

TEST_CASE("single element", "[unique sort]") {
    std::array<int, 1> input{0};
    std::array<int, 1> expected{0};
    REQUIRE(unique_sort(input) == 1);
    REQUIRE(input == expected);
}

TEST_CASE("multiple elements", "[unique sort]") {
    std::array<int, 10> input{5, 5, 4, 4, 3, 3, 2, 2, 1, 1};
    std::array<int, 5> expected{1, 2, 3, 4, 5};
    std::array<int, 5> result_container;
    size_t result_size{unique_sort(input)};
    REQUIRE(result_size == 5);
    std::copy_n(input.begin(), result_size, result_container.begin());
    REQUIRE(result_container == expected);
}
