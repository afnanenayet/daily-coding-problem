cmake_minimum_required(VERSION 3.18)
project(DCP VERSION 1.0
    DESCRIPTION "My solutions for the daily coding problem"
    LANGUAGES CXX)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(Catch2 REQUIRED)

file(GLOB_RECURSE SRC_FILES ${PROJECT_SOURCE_DIR}/src/*.cpp)
add_executable(dcp 
    src/main.cpp
)
target_include_directories(dcp PUBLIC ${PROJECT_SOURCE_DIR}/include)
target_precompile_headers(dcp PRIVATE ${PROJECT_SOURCE_DIR}/include/pch.hpp)
target_link_libraries(dcp Catch2::Catch2)
target_compile_features(dcp PUBLIC cxx_std_17)
include(CTest)