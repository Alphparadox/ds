from xmlrpc.server import SimpleXMLRPCServer
import math

def is_palindrome(s):
    return s == s[::-1]

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def gcd(a, b):
    return math.gcd(a, b)

def square_root(n):
    if n < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(n)

def swap(a, b):
    a, b = b, a
    return a, b

def array_stats(arr):
    if not arr:
        return {'min': 0, 'max': 0, 'average': 0}
    
    min_val = min(arr)
    max_val = max(arr)
    avg = sum(arr) / len(arr)
    return {'min': min_val, 'max': max_val, 'average': avg}

def compare_strings(s1, s2):
    if s1 == s2:
        return "Strings are equal."
    elif s1 < s2:
        return f"'{s1}' is lexicographically less than '{s2}'."
    else:
        return f"'{s1}' is lexicographically greater than '{s2}'."

def is_substring(sub, main):
    return sub in main

def concatenate_strings(s1, s2):
    return s1 + s2

def reverse_list(arr):
    return arr[::-1]

try:
    server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
    print("Listening on port 8000...")
    
    server.register_function(is_palindrome, "palindrome")
    server.register_function(is_leap_year, "leap_year")
    server.register_function(gcd, "gcd")
    server.register_function(square_root, "sqrt")
    server.register_function(swap, "swap")
    server.register_function(array_stats, "array_stats")
    server.register_function(compare_strings, "compare_str")
    server.register_function(is_substring, "substring")
    server.register_function(concatenate_strings, "concat")
    server.register_function(reverse_list, "reverse")
    
    server.serve_forever()

except KeyboardInterrupt:
    print("\nServer shutting down.")