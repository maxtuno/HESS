cmake_minimum_required(VERSION 3.17)
project(hess C)

set(CMAKE_C_STANDARD 99)

include_directories(include /opt/anaconda3/include/python3.7m)
add_executable(hess src/libhess.c)