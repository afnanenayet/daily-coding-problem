#include "coordinate.hpp"
#include "pch.hpp"
#include <array>

namespace p581 {
struct Rectangle {
    // The coordinate representing the top left corner of the rectangle
    Coordinate<unsigned int, 2> top_left;

    // The horizontal width of the rectangle
    unsigned int width;

    // The vertical height of the rectangle
    unsigned int height;
};

// Find the area of the intersection area between two rectangles
//
// We can do this by finding the minimum bounds for the top left and bottom
// right coordinates in the rectangle
unsigned int intersect_area(const Rectangle &a, const Rectangle &b) {
    // First, we calculate the top left corner of the new intersected area. We
    // try to find the bottom-right-most coordinates from the top left
    // coordinates of the two rectangles.
    Coordinate<unsigned int, 2> isect_top_left(
        {std::max(a.top_left[0], b.top_left[0]),
         std::max(a.top_left[1], b.top_left[1])});
    // We calculate the bottom right coordinates for each rectangle using the
    // height and the width
    Coordinate<unsigned int, 2> a_bottom_right{a.top_left[0] + a.width,
                                               a.top_left[1] + a.height};
    Coordinate<unsigned int, 2> b_bottom_right{b.top_left[0] + b.width,
                                               b.top_left[1] + b.height};
    // Calculate the bottom right corner of the rectangle representing the
    // intersection. We find the top-left-most coordinates from the bottom right
    // coordinates of the two rectangles.
    Coordinate<unsigned int, 2> isect_bottom_right = {
        std::min(a_bottom_right[0], b_bottom_right[0]),
        std::min(a_bottom_right[1], b_bottom_right[1])};

    // If the height or width is negative, that means the rectangles don't
    // overlap, and the resulting overlapping area will be 0
    // NOTE: be very careful to use `int` here and not `unsigned int` to avoid
    // overflow errors
    auto isect_width =
        std::max<int>(0, isect_bottom_right[0] - isect_top_left[0]);
    auto isect_height =
        std::max<int>(0, isect_bottom_right[1] - isect_top_left[1]);
    return isect_width * isect_height;
}

TEST_CASE("non-overlapping", "[581]") {
    REQUIRE(intersect_area(Rectangle{{0, 0}, 0, 0}, Rectangle{{0, 0}, 0, 0}) ==
            0);
    REQUIRE(intersect_area(Rectangle{{0, 0}, 1, 1},
                           Rectangle{{1000, 1000}, 5, 5}) == 0);
}

TEST_CASE("overlapping", "[581]") {
    REQUIRE(intersect_area(Rectangle{{0, 0}, 1, 1}, Rectangle{{0, 0}, 1, 1}) ==
            1);
    REQUIRE(intersect_area(Rectangle{{0, 0}, 1, 1},
                           Rectangle{{0, 0}, 100, 100}) == 1);
    REQUIRE(intersect_area(Rectangle{{0, 0}, 100, 100},
                           Rectangle{{99, 99}, 100, 100}) == 1);
}
}; // namespace p581
