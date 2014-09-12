EDIPLUG-PY - Pyhton Class for EDIMAX Smart Plug Switch SP-1101W
===============================================================
12.09.2014 Stefan Wendler
sw@kaltpost.de

Simple Python class to access a "EDIMAX Smart Plug Switch SP-1101W". Supports simple switching as well as programming
the schedule of the plug. The class could be used as an API or as command line utility: 


Requirements
------------

* Python 2.7
* The requests library (e.g. use `pip install requests`)


Use as command line utility
---------------------------

General: 

* To specify the hostname or IP addres of the plug us the `-H <host-or-ip>` parameter. 
* To pass along the login for the plug use `-l <login>`.
* To set the password for the login user `-p <password>`

Turn plug on:

    python smartplug.py -H 172.16.100.75 -l admin -p 1234 -s ON

Turn plug off:

    python smartplug.py -H 172.16.100.75 -l admin -p 1234 -s OFF

Get plug state:

    python smartplug.py -H 172.16.100.75 -l admin -p 1234 -g

Get schedule of the whole week (human readable):

    python smartplug.py -H 172.16.100.75 -l admin -p 1234 -G

Get schedule of the whole week (python array):

    python smartplug.py -H 172.16.100.75 -l admin -p 1234 -P

Set schedule for one day:

    python smartplug.py -H 172.16.100.75 -l admin -p 1234 -S "{'state': u'ON', 'sched': [[[11, 0], [11, 45]]], 'day': 6}"

Set schedule for the whole week:

    python smartplug.py -H 172.16.100.75 -l admin -p 1234 -S "[
        {'state': u'ON', 'sched': [[[1, 0], [1, 1]]], 'day': 0},
        {'state': u'ON', 'sched': [[[2, 0], [2, 2]]], 'day': 1},
        {'state': u'ON', 'sched': [[[3, 0], [3, 3]]], 'day': 2},
        {'state': u'ON', 'sched': [[[4, 0], [4, 4]]], 'day': 3},
        {'state': u'ON', 'sched': [[[5, 0], [5, 5]]], 'day': 4},
        {'state': u'ON', 'sched': [[[6, 0], [6, 6]]], 'day': 5},
        {'state': u'ON', 'sched': [[[7, 0], [7, 7]]], 'day': 6},
    ]"


Use as API
----------

Import: 

    from ediplug.smartplug import SmartPlug
    
Create plug object: 

    p = SmartPlug("172.16.100.75", ('admin', '1234'))

Turn plug off: 

    p.state = "OFF"

Turn plug on:

    p.state = "ON"

Query and print current state of plug:

    print(p.state)

Read and print complete week schedule from plug:

    print(p.schedule.__str__())

Write schedule for on day to plug (Saturday, 11:15 - 11:45):

    p.schedule = {'state': u'ON', 'sched': [[[11, 15], [11, 45]]], 'day': 6}

Note: 0 - Sunday, 6 - Saturday

Write schedule for the whole week:

    p.schedule = [
        {'state': u'ON', 'sched': [[[0, 3], [0, 4]]], 'day': 0},
        {'state': u'ON', 'sched': [[[0, 10], [0, 20]], [[10, 16], [11, 55]], [[15, 19], [15, 32]], [[21, 0], [23, 8]], [[23, 17], [23, 59]]], 'day': 1},
        {'state': u'OFF', 'sched': [[[19, 59], [21, 1]]], 'day': 2},
        {'state': u'OFF', 'sched': [[[20, 59], [21, 12]]], 'day': 3},
        {'state': u'OFF', 'sched': [], 'day': 4},
        {'state': u'OFF', 'sched': [[[0, 0], [0, 30]], [[11, 14], [14, 31]]], 'day': 5},
        {'state': u'ON', 'sched': [[[1, 42], [2, 41]]], 'day': 6}]


Complete examples could be found in the `examples` directory. Don't forget to set your python path properly. E.g. when
running the 1st exmaple from the projects main directory:

    PYTHONPATH=./src
    python ./src/examples/sample_01.py
    

Further Information
-------------------

Some more information on the plug and its XML API is provided on my website:

* [Operating from Python] (http://gpio.kaltpost.de/?p=2112)
* [Scheduling] (http://gpio.kaltpost.de/?p=2224)



