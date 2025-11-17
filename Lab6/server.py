import socket
import json
import math
import statistics

# --- 1. Palindrome Check ---
def is_palindrome(s):
    return s == s[::-1]

# --- 2. Leap Year Check ---
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# --- 3. Find GCD ---
def find_gcd(a, b):
    return math.gcd(a, b)

# --- 4. Find Square Root ---
def find_sqrt(n):
    if n < 0:
        return "Error: Cannot calculate square root of a negative number"
    return math.sqrt(n)

# --- 5. Swap two variables ---
def swap_vars(a, b):
    a, b = b, a
    return a, b

# --- 6. Array Stats (Max, Min, Avg) ---
def array_stats(arr):
    if not arr:
        return {"max": None, "min": None, "avg": None}
    return {
        "max": max(arr),
        "min": min(arr),
        "avg": statistics.mean(arr)
    }

# --- 7. Compare two strings ---
def compare_strings(s1, s2):
    if s1 == s2:
        return "Strings are equal"
    elif s1 < s2:
        return f"'{s1}' is lexicographically less than '{s2}'"
    else:
        return f"'{s1}' is lexicographically greater than '{s2}'"

# --- 8. Substring Check ---
def is_substring(main_str, sub_str):
    return sub_str in main_str

# --- 9. Concatenate two strings ---
def concat_strings(s1, s2):
    return s1 + s2

# --- 10. Reverse an array ---
def reverse_array(arr):
    return arr[::-1]

# This dictionary maps the string name (from the client) to the actual function
PROCEDURES = {
    "is_palindrome": is_palindrome,
    "is_leap": is_leap,
    "find_gcd": find_gcd,
    "find_sqrt": find_sqrt,
    "swap_vars": swap_vars,
    "array_stats": array_stats,
    "compare_strings": compare_strings,
    "is_substring": is_substring,
    "concat_strings": concat_strings,
    "reverse_array": reverse_array,
}

def handle_connection(conn, addr):
    print(f"[SERVER] Connected by {addr}")
    try:
        while True:
            data = conn.recv(1024)  # Receive data from client
            if not data:
                break
            
            # 1. Deserialize the request
            request = json.loads(data.decode('utf-8'))
            print(f"[SERVER] Received request: {request}")
            
            proc_name = request['procedure']
            args = request['args']
            
            # 2. Find and call the procedure
            if proc_name in PROCEDURES:
                try:
                    func = PROCEDURES[proc_name]
                    # Use *args to unpack the list of arguments
                    result = func(*args) 
                    response = {'status': 'success', 'result': result}
                except Exception as e:
                    response = {'status': 'error', 'message': str(e)}
            else:
                response = {'status': 'error', 'message': 'Procedure not found'}
                
            # 3. Serialize and send the response
            conn.sendall(json.dumps(response).encode('utf-8'))
            
    except ConnectionResetError:
        print(f"[SERVER] Client {addr} disconnected abruptly.")
    finally:
        print(f"[SERVER] Closing connection with {addr}")
        conn.close()

def main():
    HOST = '192.168.137.1'  # Standard loopback interface (localhost)
    PORT = 65432        # Port to listen on
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[SERVER] Listening for connections on {HOST}:{PORT}...")
        while True:
            conn, addr = s.accept()
            # Start a new thread or process for each connection if you expect many
            # For this lab, handling one at a time is fine.
            handle_connection(conn, addr)

if __name__ == "__main__":
    main()