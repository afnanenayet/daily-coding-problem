#pragma once

#include "pch.hpp"

// A coordinate class that allows for coordinates with arbitrary dimensionality
//
// A coordinate represents a point in `D` dimensional space
template <typename T, unsigned int Dims> class Coordinate {
  public:
    Coordinate() = default;
    T &operator[](std::size_t idx) { return coords[idx]; }
    const T &operator[](std::size_t idx) const { return coords[idx]; }
    const T &at(std::size_t idx) const { return coords.at(idx); }

    // The backing store for the points in a coordinate
    std::array<T, Dims> coords;
};
