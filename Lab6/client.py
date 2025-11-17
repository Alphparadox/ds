import socket
import json

# --- Helper function to make RPC calls ---
def rpc_call(proc_name, args):
    """
    Calls a remote procedure on the server.
    
    Args:
        proc_name (str): The name of the function to call.
        args (list): A list of arguments for the function.
    """
    SERVER_HOST = '192.168.137.1'  # Change this to the Server's IP address
    SERVER_PORT = 65432
    
    # 1. Package the request
    request = {
        'procedure': proc_name,
        'args': args
    }
    
    response = "No response from server"
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # 2. Connect and send the request
            s.connect((SERVER_HOST, SERVER_PORT))
            s.sendall(json.dumps(request).encode('utf-8'))
            
            # 3. Receive and deserialize the response
            data = s.recv(1024)
            response = json.loads(data.decode('utf-8'))
            
    except ConnectionRefusedError:
        return f"[CLIENT] Error: Connection refused. Is the server running at {SERVER_HOST}?"
    except Exception as e:
        return f"[CLIENT] Error: {e}"
        
    return response

# --- Main execution to call all procedures ---
if __name__ == "__main__":
    print("--- 1. Palindrome Check ---")
    print(f"Calling 'is_palindrome' with ['racecar'] -> {rpc_call('is_palindrome', ['racecar'])}")
    print(f"Calling 'is_palindrome' with ['hello'] -> {rpc_call('is_palindrome', ['hello'])}")

    print("\n--- 2. Leap Year Check ---")
    print(f"Calling 'is_leap' with [2024] -> {rpc_call('is_leap', [2024])}")
    print(f"Calling 'is_leap' with [2023] -> {rpc_call('is_leap', [2023])}")

    print("\n--- 3. Find GCD ---")
    print(f"Calling 'find_gcd' with [48, 18] -> {rpc_call('find_gcd', [48, 18])}")

    print("\n--- 4. Find Square Root ---")
    print(f"Calling 'find_sqrt' with [64] -> {rpc_call('find_sqrt', [64])}")
    print(f"Calling 'find_sqrt' with [-10] -> {rpc_call('find_sqrt', [-10])}")

    print("\n--- 5. Swap two variables ---")
    print(f"Calling 'swap_vars' with [10, 20] -> {rpc_call('swap_vars', [10, 20])}")

    print("\n--- 6. Array Stats (Max, Min, Avg) ---")
    my_array = [10, 5, 40, 25, 15]
    print(f"Calling 'array_stats' with [{my_array}] -> {rpc_call('array_stats', [my_array])}")

    print("\n--- 7. Compare two strings ---")
    print(f"Calling 'compare_strings' with ['apple', 'banana'] -> {rpc_call('compare_strings', ['apple', 'banana'])}")
    print(f"Calling 'compare_strings' with ['test', 'test'] -> {rpc_call('compare_strings', ['test', 'test'])}")

    print("\n--- 8. Substring Check ---")
    print(f"Calling 'is_substring' with ['hello world', 'world'] -> {rpc_call('is_substring', ['hello world', 'world'])}")
    print(f"Calling 'is_substring' with ['hello world', 'python'] -> {rpc_call('is_substring', ['hello world', 'python'])}")

    print("\n--- 9. Concatenate two strings ---")
    print(f"Calling 'concat_strings' with ['Hello, ', 'RPC!'] -> {rpc_call('concat_strings', ['Hello, ', 'RPC!'])}")

    print("\n--- 10. Reverse an array ---")
    array_to_reverse = [1, 2, 3, 4, 5]
    print(f"Calling 'reverse_array' with [{array_to_reverse}] -> {rpc_call('reverse_array', [array_to_reverse])}")