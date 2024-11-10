# Field	Description	Version
('version', 2) # data type: INT_32
('account-id', 2) # data type: STRING
('interface-id', 2) # data type: STRING
('srcaddr', 2) # data type: STRING
('dstaddr', 2) # data type: STRING
('srcport', 2) # data type: INT_32
('dstport', 2) # data type: INT_32
('protocol', 2) # data type: INT_32
('packets', 2) # data type: INT_64
('bytes', 2) # The number of bytes transferred during the flow. Parquet data type: INT_64
('start', 2) # The time, in Unix seconds, when the first packet of the flow was received within the aggregation interval. data type: INT_64
('end', 2) # The time, in Unix seconds, when the last packet of the flow was received within the aggregation interval. data type: INT_64
('action', 2) # The action that is associated with the traffic:
