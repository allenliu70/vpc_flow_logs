import csv
import pprint

mappings = {}

with open('lookup_table.csv') as lookup_table_csv:
    csv_reader = csv.reader(lookup_table_csv)
    for port, protocol, tag in csv_reader:
        if port.isdigit():
            port = int(port)
            print(port, protocol, tag)
            mappings[(port, protocol)] = tag


pprint.pprint(mappings)


    