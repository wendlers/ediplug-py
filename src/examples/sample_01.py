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
Very simple example showing how to use the SmartPlug API to turn the plug ON and OFF.

"""

# import plug API
from ediplug.smartplug import SmartPlug

# create plug object for plug with given IP, login admin and password 1234
p = SmartPlug("192.168.1.117", ('admin', '1234'))

# change state of plug to ON
p.state = "ON"
print("Plug is now: ", p.state)

# change state of plug to OFF
p.state = "OFF"
print("Plug is now: ", p.state)