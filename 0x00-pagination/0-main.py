#!/usr/bin/python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(page=1, page_size=7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)