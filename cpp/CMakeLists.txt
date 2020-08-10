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
target_link_libraries(dcp Catch2::Catch2)
include(CTest)
target_compile_features(dcp PUBLIC cxx_std_17)
target_include_directories(dcp PUBLIC ${PROJECT_SOURCE_DIR}/include)
target_precompile_headers(dcp PRIVATE ${PROJECT_SOURCE_DIR}/include/pch.hpp)
set_source_files_properties(${PROJECT_SOURCE_DIR}/src/main.cpp PROPERTIES SKIP_PRECOMPILE_HEADERS ON)
