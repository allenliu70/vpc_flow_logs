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

    which will read flow logs from the **sample_flow_logs.log** file in the same folder by defaul.

3. To process / analyze other flow logs, just provide the file name as an argument to the program.

    **python process_default_format.py <my_flow_logs.log>**

### Testing Conducted:

1. Initial testing was done with the sample flow logs provided in the technical assessment decription. 

2. I gathered additional version2 / default format flow log samples from AWS site https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-records-examples.html (saved locally as 'more_v2_sample_logs.log') and used it for testing purpose.

3. I wrote a synthetic flow log generator that randomize attributes in the flow logs and generate 10000 records.
   This is currently implemented for v2 / default format. To run it, type the following command:

    **python generate_flow_logs.py**

   The generated synthetic flow logs are written into **'v2_synthetic_flow_logs.log'** in the local folder.


### Addition Notes:
1. In addition to the flow logs file, this program also reads from 2 additoinal files for purposes described as follows:
      
    - **lookup_table.csv** -- this csv file provides a lookup table to tag mappings from dstport-protocol combination.
    - **protocol-numbers.csv** -- this csv was downloaded from IANA website providing the mappings between protocol numbers and protocol names.
    - **available_fields.py** -- this captures the available flow logs fiedls from AWS VPC documentation site. I initially included version 2 only. I can further expand it to include fields of higher versions.

2. Once further testings are conducted and the program's robustness is confirmed, I can go ahead and enhance this program to support higher version and custom formats.


