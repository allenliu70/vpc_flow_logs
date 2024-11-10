# vpc_flow_logs
This program will process VPC flow logs and output stats into a file.

### Release Notes:
1. Currently, it supports just version 2 (as I just got the technical assessment email today) but I can further extend it to support higher versions 
as well. 

2. By the same token, it supports only the default log format currently. But I can further enhance it to make it more flexible and support custom format next.

3. No non-default lbraries or packages.

### How to run it:

1. Clone my repo: **https://github.com/allenliu70/vpc_flow_logs.git**

2. After cloning, cd into vpc_flow_logs and type the following python command:

    **python process_default_format.py**

    which will read flow logs from the **sample_flow_logs.log** file in the same folder.

3. To process / analyze other flow logs, just replace the sample_flow_logs.log file. (Later, I can make this an argument to be passed in to the above pythn command).


### Addition Notes:
1. In addition to the flow logs file, this program also reads from 2 additoinal files for purposes described as follows:
      
    - **lookup_table.csv** -- this csv file provides a lookup table to tag mappings from dstport-protocol combination.
    - **protocol-numbers.csv** -- this csv was downloaded from IANA website providing the mappings between protocol numbers and protocol names.
    - **available_fields.py** -- this captures the available flow logs fiedls from AWS VPC documentation site. I initially included version 2 only. I can further expand it to include fields of higher versions.

2. Initial testing was done with the sample flow logs provided in the technical assessment decription. I can search the internet to gather more flow logs samples to conduct more testing.

