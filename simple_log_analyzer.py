def analyze_log(file_path):
    suspicious_keywords = ["failed", "error", "unauthorized", "denied"]

    try:
        with open(file_path, "r") as file:
            for line in file:
                for keyword in suspicious_keywords:
                    if keyword.lower() in line.lower():
                        print(f"[ALERT] Suspicious entry found: {line.strip()}")
    except FileNotFoundError:
        print("Log file not found.")

if __name__ == "__main__":
    log_file = input("Enter log file path: ")
    analyze_log(log_file)
