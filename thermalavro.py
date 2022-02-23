#!/usr/bin/env python3
from datetime import datetime, timezone
from scd4x import SCD4X
import time
import pulsar
import logging
import sys
import subprocess
import os
import traceback
import math
import base64
import json
from time import gmtime, strftime
import random, string
import time
import psutil
import uuid
from time import sleep
from math import isnan
from subprocess import PIPE, Popen
import socket 
from pulsar.schema import *
from pulsar.schema import AvroSchema

### Schema Object
# https://pulsar.apache.org/docs/en/client-libraries-python/

class thermal(Record):
    uuid = String()
    ipaddress = String()
    cputempf = Integer()
    runtime = Integer()
    host = String()
    hostname = String()
    macaddress = String()
    endtime = String()
    te = String()
    cpu = Float()
    diskusage = String()
    memory = Float()
    rowid = String()
    systemtime = String()
    ts = Integer()
    starttime = String()
    datetimestamp = String()
    temperature = Float()
    humidity = Float()
    co2 =  Float()

# IP Address
def IP_address():
        try:
            s = socket.socket(socket_family, socket.SOCK_DGRAM)
            s.connect(external_IP_and_port)
            answer = s.getsockname()
            s.close()
            return answer[0] if answer else None
        except socket.error:
            return None

# Get MAC address of a local interfaces
def psutil_iface(iface):
    # type: (str) -> Optional[str]
    import psutil
    nics = psutil.net_if_addrs()
    if iface in nics:
        nic = nics[iface]
        for i in nic:
            if i.family == psutil.AF_LINK:
                return i.address
# Random Word
def randomword(length):
 return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()) for i in range(length))

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE, universal_newlines=True)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

external_IP_and_port = ('198.41.0.4', 53)  # a.root-servers.net
socket_family = socket.AF_INET
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name) 
ipaddress = IP_address()

client = pulsar.Client('pulsar://pulsar1:6650')

thermalschema = AvroSchema(thermal)
print("Schema info is: " + thermalschema.schema_info().schema())

producer = client.create_producer(topic='persistent://public/default/pi-thermal-avro' ,schema=thermalschema,properties={"producer-name": "thermal-pyavro-sensor","producer-id": "thermal-avro-sensor" })

try:
    device = SCD4X(quiet=False)
    device.start_periodic_measurement()

    while True:
        currenttime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        starttime = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        start = time.time()

        # Create unique id
        uniqueid = 'thrm_{0}_{1}'.format(randomword(3),strftime("%Y%m%d%H%M%S",gmtime()))
        uuid2 = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())

        # CPU Temp
        f = open("/sys/devices/virtual/thermal/thermal_zone0/temp","r")
        cputemp = str( f.readline() )
        cputemp = cputemp.replace('\n','')
        cputemp = cputemp.strip()
        cputemp = str(round(float(cputemp)) / 1000)
        cputempf = str(round(9.0/5.0 * float(cputemp) + 32))
        f.close()

        usage = psutil.disk_usage("/")
        end = time.time()

        co2, temperature, relative_humidity, timestamp = device.measure()
        dateTimeStamp = datetime.fromtimestamp(timestamp, timezone.utc)
        # date.strftime("%Y/%m/%d %H:%M:%S:%f %Z %z")}
        # CO2:         {co2:.2f}PPM
        # Temperature: {temperature:.4f}c
        # Humidity:    {relative_humidity:.2f}%RH""")

        thermalRec = thermal()
        thermalRec.uuid = uniqueid
        thermalRec.ipaddress = ipaddress
        thermalRec.cputempf = int(cputempf)
        thermalRec.runtime =  int(round(end - start)) 
        thermalRec.host = os.uname()[1]
        thermalRec.hostname = host_name
        thermalRec.macaddress = psutil_iface('wlan0')
        thermalRec.endtime = '{0}'.format( str(end ))
        thermalRec.te = '{0}'.format(str(end-start))
        thermalRec.cpu = psutil.cpu_percent(interval=1)
        thermalRec.diskusage = "{:.1f} MB".format(float(usage.free) / 1024 / 1024)
        thermalRec.memory = psutil.virtual_memory().percent
        thermalRec.rowid = str(uuid2)
        thermalRec.systemtime = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        thermalRec.ts =  int( time.time() )
        thermalRec.starttime = str(starttime)

        thermalRec.datetimestamp = str(dateTimeStamp)
        thermalRec.temperature = round(float(temperature),4)
        thermalRec.humidity = round(float(relative_humidity),2)
        thermalRec.co2 =  round(float(co2),2)

        print(thermalRec)
        producer.send(thermalRec,partition_key=uniqueid)

except KeyboardInterrupt:
    pass

client.close()
