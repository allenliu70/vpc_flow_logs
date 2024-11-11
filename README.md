# vpc_flow_logs
This program will process VPC flow logs and output stats into a file.

### Intro.
I approch this problem by focusing on the simpler and easier scope first, i.e. version 2 only and the default format. Once the solution for that simpler scope is established and validated, I then use it as the base to build the more advanced sotlution for the broader problem, i.e. the support for the higher versions and custom formats. In general, I appreciate and follow the KISS principle (Keep it simple, stupid) for software design/developmen as well as security.

### Updates (Nov. 10, 2024):
1. Support for higher versions (>2) and custom format are now implemented.

2. These addition capabilities are implemented as a separate python program, named **'process_custom_format.py'**. Details will be provided below in **How to run it*** section.

### Initial Release Notes (Nov. 9, 2024):
1. Currently, it supports just version 2 (as I just got the technical assessment email today) but I can further extend it to support higher versions 
as well. 

2. By the same token, it supports only the default log format currently. But I can further enhance it to make it more flexible and support custom format next.

3. No non-default lbraries or packages.

### How to run it:

1. Clone my repo: **https://github.com/allenliu70/vpc_flow_logs.git**

2. After cloning, cd into vpc_flow_logs. Depending on whether default or custom formatted flow logs you want to processed, follow one of the following 2 sessions.
    
3. Process **default format** flow logs:

    3.1 Command:
    ```console
    python process_default_format.py
    ```
    which will read flow logs from the **test/sample_flow_logs.log** file in the same folder by default.

    3.2 To process / analyze other flow logs, just provide the file name as an argument to the program.

```console
        python process_default_format.py <my_flow_logs.log>

```
    3.3 Outputs:
        -- Tag counts and port/protocol combination counts are written to the same file.
        -- **'output.txt'** is the output file (hardcoded), located at the program local folder (not the 'test' subfolder).


4. Process **custom format** flow logs:

    4.1 Command:
```console
        python process_custom_format.py <your_custom_format_filename> <your_flow_logs_filename> [--output_filename]
```
        (e.g. python process_custom_format.py test/sample_custom_format.config test/tcp_flag_sequence.log)

    4.2 Arguments:
        -- The first 2 (positional) arguments are mandatory.
                
                <your_custom_format_filename>:
                    - This file must contain 1 uncommented line to specify your custom format.
                    - Commented and empty lines are ignore. The 1st uncommented and non-empty line will be treated as the specified custom format.
                    - The fields specified in this line must be valid AWS flow log field which Amazon publshed on their website.
                    - Otherwise, the program will print an error and exit.

                <your_flow_logs_filename>:
                    - This file should contain the flow logs you want to process and its contents should match the custom format you've provided.
                    - By default, results are written to 'output_custom_format.txt' at program local folder. (Not the 'test' subfoler)

        -- The 3rd argument is optional, default: 'output_custom_fmt.txt'.
                If you specify the output filename, the tag counts and port/portocol counts will be written there.

    4.3 Outputs:
        -- Tag counts and port/protocol combination counts are written to the same file.
        -- By default, **'output_custom_fmt.txt'** is the output file.
        -- If user has provided an output filename to the program, the user-specified output file path will be created and updated with the results.

### Testing Conducted:

1. Initial testing was done with the sample flow logs provided in the technical assessment decription. 

2. I gathered additional version2 / default format flow log samples from AWS site https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-records-examples.html (saved locally as 'more_v2_sample_logs.log') and used it for testing purpose.

3. I wrote a **synthetic flow log generator** that randomize attributes in the flow logs and generate 10000 records.
   This is currently implemented for v2 / default format. To run it, type the following command:

```console
    cd test
    python generate_flow_logs.py
```

   The generated synthetic flow logs are written into **'v2_synthetic_flow_logs.log'** in the test subfolder.
   ps. A word on dstport randomization: 
         - since the range (1, 65535) for ports results in mostly untagged entries, I made an assumption here that we may be more interseted in small set of pre-selecte ports.
         - By defaul, I read pre_selected_ports from lookup_table.csv, which is the example tag mappings provide for this technical assessment. It currently contains these port numbers: [25, 68, 23, 31, 443, 22, 3389, 0, 110, 993, 143].
         - To change the list of dstports you want in the generated synthetic flow logs, just replace/update/edit the lookup_tabe.csv file.


### Addition Notes:
1. In addition to the flow logs file, this program also reads from 2 additoinal files for purposes described as follows:
      
    - **lookup_table.csv** -- this csv file provides a lookup table to tag mappings from dstport-protocol combination.
    - **protocol-numbers.csv** -- this csv was downloaded from IANA website providing the mappings between protocol numbers and protocol names.
    - **available_fields.py** -- this captures the available flow logs fiedls from AWS VPC documentation site. I initially included version 2 only. I can further expand it to include fields of higher versions.

2. Once further testings are conducted and the program's robustness is confirmed, I can go ahead and enhance this program to support higher version and custom formats.

3. Please note: if the fields custom format do not match the flow logs data, the program could error out.

4. Since I re-used main compoments from the implementation for the default format for the more advanced solution for the custom format, there is an opportunity to refactor the code and move the common components into, say, a utils file or folder. I can do that as a further enhancement.