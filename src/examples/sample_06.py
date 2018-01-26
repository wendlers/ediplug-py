##
# The MIT License (MIT)
#
# Copyright (c) 2018 Stefan Wendler
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
This example shows how to connect the plug to Blynk (http://www.blynk.cc/).

The following is needed to make this example run:

    - BlynkLib for Python installed: 
        - e.g.: pip install blynk-library-python
        - for details go to: https://github.com/vshymanskyy/blynk-library-python
    - Blynk App for your smart phone: 
        - Android: https://play.google.com/store/apps/details?id=cc.blynk
        - iOS: https://itunes.apple.com/us/app/blynk-control-arduino-raspberry/id808760481?ls=1&mt=8
    
Next, in the Blynk App on the phone, create a new project (e.g. for generic board). 
A token will be send to you by email. Copy the token into 'BLYNK_AUTH' below. 
Back in the Blynk App, add a button widget, and assign virtual PIN V0 to it. 

In the code below also fill in the correct values for 'PLUG_IP', 'PLUG_LOGIN' and 'PLUG_PASSWORD'

Now fire up this example, and you should see it go online in the phone app. Switch the
plug with the button in the app.  

An other nice thing is, that you are now also able to reach your plug via the 
Blynk REST API through the WWW doing the following:

    - get the IP of your countries Blynk could server e.g. with ping:

        ping cloud.blynk.cc

      E.g. for europe this returns: 139.59.206.133

    - then make a PUT request with the following URL to turn the plug ON, e.g. using CURL:

        curl -H "Content-Type: application/json" -X PUT -d '["1"]' http://139.59.206.133/BLYNK_TOKEN/pin/V0

      and to turn it OFF:
   
        curl -H "Content-Type: application/json" -X PUT -d '["0"]' http://139.59.206.133/BLYNK_TOKEN/pin/V0
    
This also works nicely with IFTTT when using 'webhook' as action and configuring it like this:

    - URL         : http://139.59.206.133/BLYNK_TOKEN/pin/V0
    - Method      : PUT
    - Content-Type: application/json
    - Body        : ["1"] for ON or ["0"] for OFF

"""

import BlynkLib
import ediplug

BLYNK_AUTH = 'YourAuthToken'

PLUG_IP = '192.168.1.117'
PLUG_LOGIN = 'admin'
PLUG_PASSWORD = '1234'

blynk = BlynkLib.Blynk(BLYNK_AUTH)
plug = ediplug.SmartPlug(PLUG_IP, (PLUG_LOGIN, PLUG_PASSWORD))


@blynk.VIRTUAL_WRITE(0)
def ediplug_write_handler(value):
    """
    Called by Blynk whenever the button state changed.

    :param value:   1 - ON, 0 - OFF
    """
    global plug

    if value == '1':
        plug.state = 'ON'
        print("Turning plug ON")
    else:
        plug.state = 'OFF'
        print("Turning plug OFF")


def blynk_connected():
    """
    On startup sync state from Blynk server to plug.
    """
    global blynk

    print("Updating all values from the server...")
    blynk.sync_all()


blynk.on_connect(blynk_connected)
blynk.run()
