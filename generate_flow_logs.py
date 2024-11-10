import random
import time
import csv
from typing import List

def get_iana_protocol_numbers() -> List:
    # Initialize an empty dictionary to store the mapping
    protocol_numbers = []

    try:
        print('Retrieving IANA protocol numbers.')
        # Open the CSV file containing the protocol numbers and names
        with open('protocol-numbers.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            
            # Skip the header row if there is one
            next(csv_reader)
            
            # Iterate over each row in the CSV file, assuming the first column is the protocol number
            protocol_numbers = [int(row[0]) for row in csv_reader if row[0].isdigit()]
                
    except FileNotFoundError:
        print("The file was not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    else:
        print('Sucessfully read IANA protocol numbers from the saved csv file.')
    finally:
        print("Finished file operation.")
    
    return protocol_numbers

def get_pre_selected_ports() -> List:
    # Initialize an empty dictionary to store the mapping
    pre_select_ports = []

    try:
        print('Retrieving IANA protocol numbers.')
        # Open the CSV file containing the protocol numbers and names
        with open('lookup_table.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            
            # Skip the header row if there is one
            next(csv_reader)
            
            # Iterate over each row in the CSV file, assuming the first column is the protocol number
            pre_select_ports = [int(row[0]) for row in csv_reader if row[0].isdigit()]
                
    except FileNotFoundError:
        print("The file was not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    else:
        print('Sucessfully read IANA protocol numbers from the saved csv file.')
    finally:
        print("Finished file operation.")
    
    return pre_select_ports
    pass

# since the range (1, 65535) for ports results in mostly untagged entries, I made an assumption here
# that we may be more interseted in small set of pre-selecte ports
# pre_selected_ports = [25, 68, 23, 31, 443, 22, 3389, 0, 110, 993, 143] # taken from the sample tag mappings lookup table.
pre_selected_ports = get_pre_selected_ports()

# print(get_iana_protocol_numbers())
iana_protocol_numbers = get_iana_protocol_numbers()

    

def generate_flow_log_entry():
    version = 2
    account_id = "123456789012"
    eni_id = f"eni-{random.randint(1000, 9999):04x}"
    srcaddr = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
    dstaddr = f"203.0.{random.randint(0, 255)}.{random.randint(0, 255)}"
    srcport = random.randint(1024, 65535)
    # dstport = random.randint(1, 65535)
    dstport = random.choice(pre_selected_ports)
    protocol = random.choice(iana_protocol_numbers) 
    packets = random.randint(1, 100)
    bytes = packets * random.randint(40, 1500)
    start = int(time.time())
    end = start + random.randint(1, 60)
    action = random.choice(["ACCEPT", "REJECT"])
    log_status = "OK"
    
    return f"{version} {account_id} {eni_id} {srcaddr} {dstaddr} {srcport} {dstport} {protocol} {packets} {bytes} {start} {end} {action} {log_status}"

# Generate a large number of flow log entries
with open('v2_synthetic_flow_logs.log', 'w') as file:
    for _ in range(10000):  # Adjust the number as needed
        file.write(generate_flow_log_entry() + "\n")

print("Synthetic flow logs generated.")
