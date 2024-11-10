import csv
from pprint import pprint

from available_fields import fields
default_fields = [f[0] for f in fields]

def get_iana_protocol_mapping() -> dict:
    # Initialize an empty dictionary to store the mapping
    protocol_mapping = {}

    try:
        print('Retrieving IANA protocol numbers.')
        # Open the CSV file containing the protocol numbers and names
        with open('protocol-numbers.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            
            # Skip the header row if there is one
            next(csv_reader)
            
            # Iterate over each row in the CSV file
            for row in csv_reader:
                # Assuming the first column is the protocol number and the second column is the protocol name
                if row[0].isdigit():
                    protocol_number = int(row[0])
                    protocol_name = row[1]
                    protocol_mapping[protocol_number] = protocol_name
    except FileNotFoundError:
        print("The file was not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    else:
        print('Sucessfully read IANA protocol numbers from the saved csv file.')
    finally:
        print("Finished file operation.")
    
    return protocol_mapping


def get_tag_mappings() -> dict:
    tag_mappings = {}

    try:
        print('Retrieving tag mappings from the lookup table csv.')
        with open('lookup_table.csv') as lookup_table_csv:
            csv_reader = csv.reader(lookup_table_csv)
            for port, protocol, tag in csv_reader:
                if port.isdigit():
                    port = int(port)
                    tag_mappings[(port, protocol)] = tag
    except FileNotFoundError:
        print("The file was not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    else:
        print('Sucessfully read tag mappings from the csv file.')
    finally:
        print("Finished file operation.")

    return tag_mappings

from typing import List, Dict
def get_counts() -> List[Dict]:
    tag_counts = {}
    port_prot_counts = {}

    protocol_mapping = get_iana_protocol_mapping()
    tag_mappings = get_tag_mappings()

    try:
        print('Reading flow logs and compute tag counts and port/prot combo counts.')
        with open('sample_flow_logs.log') as logfile:
            for line in logfile:
                line = line.strip(' \n')
                if line:
                    dstport, protocol = None, None
                    for fname, fval in zip(default_fields, line.split()):
                        if fname == 'dstport':
                            dstport = int(fval)
                        elif fname == 'protocol':
                            protocol = protocol_mapping[int(fval)].lower()

                    pp_combo = (dstport, protocol)
                    tag = tag_mappings[pp_combo] if pp_combo in tag_mappings else 'Untagged'

                    tag_counts[tag] = tag_counts[tag] + 1 if tag in tag_counts else 1
                    port_prot_counts[pp_combo] = port_prot_counts[pp_combo] + 1 if pp_combo in port_prot_counts else 1
    except FileNotFoundError:
        print("The file was not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    else:
        print('Sucessfully read flow logs and computed counts.')
    finally:
        print("Finished file operation.")

    print('Finished computing tag counts and port/prot combo counts.')
    return [tag_counts, port_prot_counts]


def output_counts_to_file(tag_counts: Dict, port_prot_counts: Dict) -> None:
    try:
        with open('output.txt', mode='w') as outfile:
            print('Writing Tag Counts to output.txt')
            outfile.write('Tag Counts:\n')
            outfile.write('Tag,Count\n')
            for tag, count in tag_counts.items():
                outfile.write(f'{tag},{count}\n')

            print('Writing Port/Protocol Combination Counts to output.txt')
            outfile.write('\nPort/Protocol Combination Counts:\n')
            outfile.write('Port,Protocol,Count\n')
            for (port, protocol), count in port_prot_counts.items():
                outfile.write(f'{port},{protocol},{count}\n')
    except FileNotFoundError:
        print("The file was not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    else:
        print('Sucessfully wrote counts to output.txt file.')
    finally:
        print("Finished file operation.")


if __name__ == "__main__":

    tag_counts, port_prot_counts = get_counts()
    
    print('\nTag Counts:')
    pprint(tag_counts)

    print('\nPort/Protocol Combination Counts:')
    pprint(port_prot_counts)

    output_counts_to_file(tag_counts=tag_counts, port_prot_counts=port_prot_counts)
    print('Done. Please open output.txt to check the results.')
