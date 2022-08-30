#### More Sensors

#### Topic

persistent://public/default/thermalextsensors-partition-0

#### Run It

````

python3 /opt/demo/cloudsensors.py -t persistent://public/default/thermalextsensors -su pulsar://pulsar1:6650

````

#### JSON Sensor Data

````

{
'uuid': 'thrml_xxj_20220830161901', 'ipaddress': '192.168.1.179', 
'cputempf': 122, 'runtime': 0, 'host': 'thermal', 'hostname': 'thermal', 
'macaddress': 'e4:5f:01:7c:3f:34', 'endtime': '1661876341.3852887', 
'te': '0.0007121562957763672', 'cpu': 11.3, 'diskusage': '104222.5 MB', 
'memory': 9.8, 'rowid': '20220830161901_05a69b73-f2f1-4b5c-8543-aaea0b4dfa4a',
'systemtime': '08/30/2022 12:19:06', 'ts': 1661876346, 'starttime': '08/30/2022 12:19:01', 
'datetimestamp': '2022-08-30 16:19:05.150044+00:00', 
'temperature': 31.5251, 'humidity': 42.71, 'co2': 572.0, 
'totalvocppb': '  0', 'equivalentco2ppm': '65535', 'pressure': 100670.76, 'temperatureicp': 85.0
}

````
