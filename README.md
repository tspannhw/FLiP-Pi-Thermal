# FLiP-Pi-Thermal

### Example Run

````

root@thermal:/opt/demo# python3 thermal.py                                                                                                                                   
2022-02-22 19:41:44.380 INFO  [3069204864] ClientConnection:182 | [<none> -> pulsar://pulsar1:6650] Create ClientConnection, timeout=10000                                   
2022-02-22 19:41:44.380 INFO  [3069204864] ConnectionPool:96 | Created connection for pulsar://pulsar1:6650                                                                  
2022-02-22 19:41:44.386 INFO  [3036730432] ClientConnection:368 | [192.168.1.204:34966 -> 192.168.1.230:6650] Connected to broker                                            
2022-02-22 19:41:44.390 INFO  [3036730432] HandlerBase:64 | [persistent://public/default/pi-thermal, ] Getting connection from pool                                          
2022-02-22 19:41:44.392 INFO  [3036730432] ClientConnection:182 | [<none> -> pulsar://pulsar1:6650] Create ClientConnection, timeout=10000                                   
2022-02-22 19:41:44.392 INFO  [3036730432] ConnectionPool:96 | Created connection for pulsar://127.0.0.1:6650                                                                
2022-02-22 19:41:44.396 INFO  [3036730432] ClientConnection:370 | [192.168.1.204:34968 -> 192.168.1.230:6650] Connected to broker through proxy. Logical broker: pulsar://127.0.0.1:6650                                                                                                                                                                  
2022-02-22 19:41:44.430 INFO  [3036730432] ProducerImpl:189 | [persistent://public/default/pi-thermal, ] Created producer on broker [192.168.1.204:34968 -> 192.168.1.230:6650] 
SCD4X, Serial: d3efd3efd3ef
{'_required_default': False, '_default': None, '_required': False, 'uuid': 'wthr_uri_20220223004144', 'ipaddress': '192.168.1.204', 'cputempf': 108, 'runtime': 0, 'host': 'thermal', 'hostname': 'thermal', 'macaddress': 'e4:5f:01:7c:3f:34', 'endtime': '1645576904.9345362', 'te': '0.0006937980651855469', 'cpu': 6.5, 'diskusage': '106326.3 MB', 'memory': 8.7, 'rowid': '20220223004144_b9de27fa-fc0b-46a0-8d1f-04664360f3b0', 'systemtime': '02/22/2022 19:41:50', 'ts': 1645576910, 'starttime': '02/22/2022 19:41:44', 'datetimestamp': '2022-02-23 00:41:49.613734+00:00', 'temperature': 28.4543, 'humidity': 28.6, 'co2': 670.0}
{'_required_default': False, '_default': None, '_required': False, 'uuid': 'wthr_qle_20220223004150', 'ipaddress': '192.168.1.204', 'cputempf': 108, 'runtime': 0, 'host': 'thermal', 'hostname': 'thermal', 'macaddress': 'e4:5f:01:7c:3f:34', 'endtime': '1645576910.6230323', 'te': '0.0004811286926269531', 'cpu': 0.0, 'diskusage': '106326.3 MB', 'memory': 8.7, 'rowid': '20220223004150_040bc286-7778-4b87-8f20-abbe3028fe29', 'systemtime': '02/22/2022 19:41:55', 'ts': 1645576915, 'starttime': '02/22/2022 19:41:50', 'datetimestamp': '2022-02-23 00:41:54.384983+00:00', 'temperature': 27.9977, 'humidity': 29.2, 'co2': 683.0}
{'_required_default': False, '_default': None, '_required': False, 'uuid': 'wthr_sgh_20220223004155', 'ipaddress': '192.168.1.204', 'cputempf': 107, 'runtime': 0, 'host': 'thermal', 'hostname': 'thermal', 'macaddress': 'e4:5f:01:7c:3f:34', 'endtime': '1645576915.400389', 'te': '0.0007336139678955078', 'cpu': 0.0, 'diskusage': '106326.3 MB', 'memory': 8.7, 'rowid': '20220223004155_1a7c21b3-3e0b-48c9-8c3c-73e11b538602', 'systemtime': '02/22/2022 19:42:00', 'ts': 1645576920, 'starttime': '02/22/2022 19:41:55', 'datetimestamp': '2022-02-23 00:41:59.164362+00:00', 'temperature': 27.7413, 'humidity': 29.66, 'co2': 682.0}
^C2022-02-22 19:42:02.086 INFO  [3069204864] ClientImpl:495 | Closing Pulsar client with 1 producers and 0 consumers
2022-02-22 19:42:02.086 INFO  [3069204864] ProducerImpl:686 | [persistent://public/default/pi-thermal, standalone-1-2217] Closing producer for topic persistent://public/default/pi-thermal
2022-02-22 19:42:02.092 INFO  [3036730432] ProducerImpl:729 | [persistent://public/default/pi-thermal, standalone-1-2217] Closed producer
2022-02-22 19:42:02.092 INFO  [3036730432] ClientConnection:1548 | [192.168.1.204:34968 -> 192.168.1.230:6650] Connection closed
2022-02-22 19:42:02.092 INFO  [3036730432] ClientConnection:1548 | [192.168.1.204:34966 -> 192.168.1.230:6650] Connection closed
2022-02-22 19:42:02.121 INFO  [3069204864] ProducerImpl:655 | Producer - [persistent://public/default/pi-thermal, standalone-1-2217] , [batching  = off]
2022-02-22 19:42:02.122 INFO  [3069204864] ClientConnection:256 | [192.168.1.204:34966 -> 192.168.1.230:6650] Destroyed connection
2022-02-22 19:42:02.122 INFO  [3069204864] ClientConnection:256 | [192.168.1.204:34968 -> 192.168.1.230:6650] Destroyed connection

````

### References

* https://github.com/tspannhw/minifi-gasthermal.git
