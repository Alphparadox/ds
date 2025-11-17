import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("Client: Connected to RPC Server.\n")

print("--- 1. Palindrome ---")
s = "madam"
print(f"Client: Calling palindrome('{s}')")
result = proxy.palindrome(s)
print(f"Server returned: {result}\n")

print("--- 2. Leap Year ---")
year = 2024
print(f"Client: Calling leap_year({year})")
result = proxy.leap_year(year)
print(f"Server returned: {result}\n")

print("--- 3. GCD ---")
a, b = 48, 18
print(f"Client: Calling gcd({a}, {b})")
result = proxy.gcd(a, b)
print(f"Server returned: {result}\n")

print("--- 4. Square Root ---")
n = 64
print(f"Client: Calling sqrt({n})")
result = proxy.sqrt(n)
print(f"Server returned: {result}")

n_neg = -10
print(f"Client: Calling sqrt({n_neg})")
try:
    result = proxy.sqrt(n_neg)
    print(f"Server returned: {result}\n")
except xmlrpc.client.Fault as err:
    print(f"Server returned an error: {err.faultString}\n")

print("--- 5. Swap ---")
x, y = 10, 20
print(f"Client: Calling swap({x}, {y})")
swapped_x, swapped_y = proxy.swap(x, y)
print(f"Server returned: a = {swapped_x}, b = {swapped_y}\n")

print("--- 6. Array Stats ---")
my_array = [10, 20, 30, 40, 50]
print(f"Client: Calling array_stats({my_array})")
stats = proxy.array_stats(my_array)
print(f"Server returned: Min: {stats['min']}, Max: {stats['max']}, Avg: {stats['average']}\n")

print("--- 7. Compare Strings ---")
s1, s2 = "apple", "banana"
print(f"Client: Calling compare_str('{s1}', '{s2}')")
result = proxy.compare_str(s1, s2)
print(f"Server returned: {result}\n")

print("--- 8. Substring ---")
sub, main_str = "world", "hello world"
print(f"Client: Calling substring('{sub}', '{main_str}')")
result = proxy.substring(sub, main_str)
print(f"Server returned: {result}\n")

print("--- 9. Concatenate ---")
s1, s2 = "hello", " world"
print(f"Client: Calling concat('{s1}', '{s2}')")
result = proxy.concat(s1, s2)
print(f"Server returned: '{result}'\n")

print("--- 10. Reverse List ---")
my_list = [1, 2, 3, 4, 5]
print(f"Client: Calling reverse({my_list})")
result = proxy.reverse(my_list)
print(f"Server returned: {result}\n")