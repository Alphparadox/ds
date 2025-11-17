import time
import random
import datetime

class TimeServer:
    def __init__(self):
        # The server is 5 minutes AHEAD of real time for this demo
        self.offset = 300 

    def get_time(self):
        """Returns the server's current high-precision timestamp."""
        return time.time() + self.offset

class Client:
    def __init__(self, server):
        self.server = server
        # The client is 10 minutes BEHIND real time initially
        self.offset = -600 
    
    def get_local_time(self):
        """Returns client's current time with its specific drift."""
        return time.time() + self.offset

    def adjust_clock(self, new_offset):
        """Updates the client's clock offset after synchronization."""
        self.offset = new_offset

    def synchronize(self):
        print(f"[Client] Requesting time from server...")
        
        # 1. Record time request sent (local client time)
        t0_local = self.get_local_time()
        t0_monotonic = time.monotonic() # Use monotonic for accurate RTT measurement

        # Simulate network latency (sending request)
        time.sleep(random.uniform(0.5, 1.5)) 
        
        # 2. Server receives request and sends back its time
        server_time = self.server.get_time()
        
        # Simulate network latency (receiving response)
        time.sleep(random.uniform(0.5, 1.5)) 
        
        # 3. Record time response received
        t1_monotonic = time.monotonic()
        
        # 4. Calculate RTT and new time
        rtt = t1_monotonic - t0_monotonic
        synchronized_time = server_time + (rtt / 2)
        
        # 5. Calculate the new offset for the client clock to match synchronized time
        # (Current actual system time + new_offset = synchronized_time)
        current_actual_time = time.time()
        new_offset = synchronized_time - current_actual_time
        self.adjust_clock(new_offset)

        return rtt, server_time, synchronized_time

# --- Demonstration ---
def format_time(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S.%f')[:-3]

# Initialize
server = TimeServer()
client = Client(server)

print("--- Before Synchronization ---")
print(f"Server Time: {format_time(server.get_time())}")
print(f"Client Time: {format_time(client.get_local_time())}")
print("\n--- Starting Synchronization Process ---")

# Perform sync
rtt, t_server, t_sync = client.synchronize()

print(f"\n[Stats] Round Trip Time (RTT): {rtt:.4f} seconds")
print(f"[Stats] Server timestamp received: {format_time(t_server)}")
print(f"[Stats] Calculated synchronized time (T_server + RTT/2): {format_time(t_sync)}")

print("\n--- After Synchronization ---")
print(f"Server Time: {format_time(server.get_time())}")
print(f"Client Time: {format_time(client.get_local_time())}")

error = abs(server.get_time() - client.get_local_time())
print(f"New difference between Server and Client: {error:.4f} seconds")