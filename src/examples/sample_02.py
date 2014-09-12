##
# The MIT License (MIT)
#
# Copyright (c) 2014 Stefan Wendler
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
##

__author__ = 'Stefan Wendler, sw@kaltpost.de'

"""
Very simple example showing how to use the SmartPlug API query week schedule.

"""

# import plug API
from ediplug.smartplug import SmartPlug

# create plug object for plug with IP 172.16.100.75, login admin and password 1234
p = SmartPlug("172.16.100.75", ('admin', '1234'))

# helper to map numerical days to named days
days = { 0 : "Sunday", 1 : "Monday", 2 : "Tuesday", 3 : "Wednesday",
         4 : "Thursday", 5 : "Friday", 6 : "Saturday"}

# request schedule from plug, display information for each day
for day in p.schedule:

    # only if this day has a schedule, print it
    if len(day["sched"]) > 0:

        # print day information
        print("Schedules for: %s (%s)" % (days[day["day"]], day["state"]))

        # print scheduled hours
        for sched in day["sched"]:
            print(" * %02d:%02d - %02d:%02d" % (sched[0][0], sched[0][1], sched[1][0], sched[1][1]))