#!/usr/bin/python3
"""Test file for LIFO cache"""

LIFOCache = __import__('2-lifo_cache').LIFOCache

lifo = LIFOCache()

lifo.print_cache()
lifo.put('A', 'Hello')
lifo.put('B', 'Everyone')
lifo.put('C', 'Python is fun')
lifo.put('D', 'Read the Zen of Python LOL, and get started')
lifo.print_cache()
lifo.put('E', 'Just do it everyday')
lifo.print_cache()
lifo.put('B', 'Solve problems')
lifo.print_cache()
