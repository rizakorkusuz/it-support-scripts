import os

def check_connection(host="8.8.8.8"):
    print(f"Checking connectivity to {host}...\n")
    response = os.system(f"ping -c 1 {host}")
    
    if response == 0:
        print("Network is reachable ✅")
    else:
        print("Network is not reachable ❌")

if __name__ == "__main__":
    check_connection()
