cmake_minimum_required(VERSION 4.0)
project(learncpp)

set(CMAKE_CXX_STANDARD 20)

add_executable(learncpp main.cpp
        calculator.txt
        funcs.cpp
        input.cpp
)
