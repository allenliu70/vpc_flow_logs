import random
import time

def generate_flow_log_entry():
    version = 2
    account_id = "123456789012"
    eni_id = f"eni-{random.randint(1000, 9999):04x}"
    srcaddr = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
    dstaddr = f"203.0.{random.randint(0, 255)}.{random.randint(0, 255)}"
    srcport = random.randint(1024, 65535)
    dstport = random.randint(1, 65535)
    protocol = 6  # TCP
    packets = random.randint(1, 100)
    bytes = packets * random.randint(40, 1500)
    start = int(time.time())
    end = start + random.randint(1, 60)
    action = random.choice(["ACCEPT", "REJECT"])
    log_status = "OK"
    
    return f"{version} {account_id} {eni_id} {srcaddr} {dstaddr} {srcport} {dstport} {protocol} {packets} {bytes} {start} {end} {action} {log_status}"

# Generate a large number of flow log entries
with open('synthetic_flow_logs.log', 'w') as file:
    for _ in range(10000):  # Adjust the number as needed
        file.write(generate_flow_log_entry() + "\n")

print("Synthetic flow logs generated.")
