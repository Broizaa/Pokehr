cmake_minimum_required(VERSION 3.23)
project(poker)

set(CMAKE_CXX_STANDARD 14)

add_executable(poker Carte.cpp Carte.h "aleatoire carte.cpp" test_main.cpp)
