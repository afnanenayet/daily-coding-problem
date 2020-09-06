include(CheckCXXCompilerFlag)

cmake_minimum_required(VERSION 3.18)
project(DCP VERSION 1.0
    DESCRIPTION "My solutions for the daily coding problem"
    LANGUAGES CXX)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if (CMAKE_CXX_COMPILER_ID STREQUAL "Clang" AND CMAKE_GENERATOR STREQUAL "Ninja")
    set(CMAKE_C_FLAGS "-fcolor-diagnostics ${CMAKE_C_FLAGS}")
    set(CMAKE_CXX_FLAGS "-fcolor-diagnostics ${CMAKE_CXX_FLAGS}")
endif()

# Enable address sanitizer in debug builds
set(SanitizeFlag "-fsanitize=address")
set(NoOmitFramePointerFlag "-fno-omit-frame-pointer")

check_cxx_compiler_flag("-fno-omit-frame-pointer" NoOmitFramePointer)
check_cxx_compiler_flag("-fsanitize=address" SanitizeAddress)

if (NoOmitFramePointer AND SanitizeAddress)
    string(APPEND CMAKE_CXX_FLAGS_DEBUG  " ${SanitizeFlag} ${NoOmitFramePointerFlag}")
    string(APPEND CMAKE_LINKER_FLAGS_DEBUG  " ${SanitizeFlag} ${NoOmitFramePointerFlag}")
endif()

find_package(Catch2 REQUIRED)
find_package(fmt REQUIRED)

add_executable(dcp 
    src/main.cpp
    src/579.cpp
    src/580.cpp
    src/581.cpp
    src/582.cpp
    src/583.cpp
    src/584.cpp
    src/585.cpp
    src/586.cpp
    )
target_link_libraries(dcp Catch2::Catch2)
target_link_libraries(dcp fmt::fmt)
target_compile_features(dcp PUBLIC cxx_std_17)
target_include_directories(dcp PUBLIC ${PROJECT_SOURCE_DIR}/include)
target_precompile_headers(dcp PRIVATE ${PROJECT_SOURCE_DIR}/include/pch.hpp)

# We can't use precompiled headers for the main directory beacuse of the catch2
# macro that creates the main testing harness
set_source_files_properties(${PROJECT_SOURCE_DIR}/src/main.cpp PROPERTIES SKIP_PRECOMPILE_HEADERS ON)
