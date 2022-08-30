#### More Sensors

This is a added sensors to the existing Raspberry Pi / Thermal device we had.

#### Topic

persistent://public/default/thermalextsensors-partition-0

#### Run It

````

python3 /opt/demo/cloudsensors.py -t persistent://public/default/thermalextsensors -su pulsar://pulsar1:6650

````

#### Python Record

````
class thermalext(Record):
    uuid = String(required=True)
    ipaddress = String(required=True)
    cputempf = Integer(required=True)
    runtime = Integer(required=True)
    host = String(required=True)
    hostname = String(required=True)
    macaddress = String(required=True)
    endtime = String(required=True)
    te = String(required=True)
    cpu = Float(required=True)
    diskusage = String(required=True)
    memory = Float(required=True)
    rowid = String(required=True)
    systemtime = String(required=True)
    ts = Integer(required=True)
    starttime = String(required=True)
    datetimestamp = String(required=True)
    temperature = Float(required=True)
    humidity = Float(required=True)
    co2 =  Float(required=True)
    totalvocppb = String(required=True)
    equivalentco2ppm = String(required=True)
    pressure = Float(required=True)
    temperatureicp = Float(required=True)
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

## Flink SQL Setup

# Flink table

````
CREATE CATALOG pulsar WITH (
   'type' = 'pulsar',
   'service-url' = 'pulsar://pulsar1:6650',
   'admin-url' = 'http://pulsar1:8080',
   'format' = 'json'
);

USE CATALOG pulsar;

SHOW TABLES;

Flink SQL> DESC thermalextsensors;
+------------------+--------+-------+-----+--------+-----------+
|             name |   type |  null | key | extras | watermark |
+------------------+--------+-------+-----+--------+-----------+
|             uuid | STRING | false |     |        |           |
|        ipaddress | STRING | false |     |        |           |
|         cputempf |    INT | false |     |        |           |
|          runtime |    INT | false |     |        |           |
|             host | STRING | false |     |        |           |
|         hostname | STRING | false |     |        |           |
|       macaddress | STRING | false |     |        |           |
|          endtime | STRING | false |     |        |           |
|               te | STRING | false |     |        |           |
|              cpu |  FLOAT | false |     |        |           |
|        diskusage | STRING | false |     |        |           |
|           memory |  FLOAT | false |     |        |           |
|            rowid | STRING | false |     |        |           |
|       systemtime | STRING | false |     |        |           |
|               ts |    INT | false |     |        |           |
|        starttime | STRING | false |     |        |           |
|    datetimestamp | STRING | false |     |        |           |
|      temperature |  FLOAT | false |     |        |           |
|         humidity |  FLOAT | false |     |        |           |
|              co2 |  FLOAT | false |     |        |           |
|      totalvocppb | STRING | false |     |        |           |
| equivalentco2ppm | STRING | false |     |        |           |
|         pressure |  FLOAT | false |     |        |           |
|   temperatureicp |  FLOAT | false |     |        |           |
+------------------+--------+-------+-----+--------+-----------+
24 rows in set


select datetimestamp, temperature, humidity, co2, totalvocppb, equivalentco2ppm, pressure, temperatureicp
from thermalextsensors

````
