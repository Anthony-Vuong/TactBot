# TactBot🤖
Wireless robot project that uses bluetooth from Android device to communicate with a RPI4. The RPI4 will interface
with an RC Car through the GPIO PWM Signals. Commands will be sent through Android bluetooth protocol. To access the manifest, 
main activity, and design file use the following path: App-Src-Main

Author: Anthony Vuong, Pedro Muñoz-Rodriguez

Development Status:
                  
                     App: Testing 🔵
                  
                   Rover: In Development 🟡
                  
                  Turret: On Hold 🔴
    
    
                  Updated: 02 - 02 - 2021


✔️11/15/2020: MainActivity Updated with Broadcast Receiver

✔️11/17/2020: Discoverable feature implemeneted with second broadcast receiver. Initiated with connect button.

✔️11/26/2020: Created list view of discoverable devices. Design changed slightly. Will implement
controls at a later date. In addition, added ME405 Turret control python files and Rover control
python files. Rover feature given motor controls. HAPPY THANKSGIVING!!!

✔️11/27/2020: Device pairing feature implemented.

✔️11/28/2020: Bluetooth server/client socket class implemented using BluetoothServerSocket and BluetoothSocket classes. Not yet complete.

✔️11/29/2020: ConnectThread subclass in BluetoothConnection source file. Ordered V2-8 MEGAPIZEL RPI Camera w/ PAN Tilt HAT and Coral USB Connector

✔️11/30/2020: TurretFeature Motor Control source file updated.

✔️12/01/2020: Updated Rover features with new speed control and motor control functions. BOM Added(see OtherDocuments folder)

✔️12/02/2020: ConnectedThread class created - used after establishing connection. Bluetooth process: acceptThread -> connectThread -> connectedThread

✔️12/03/2020: Small features for RoverFeature motor control changed. Turret feature automation implementations and camera setup planning.

✔️12/05/2020: Updates to turret encoder.py and added 2 buttons/1 edit text widgets in app design. MainActivity completed with core bluetoohconnection structure! Not tested...

✔️12/14/2020: Turret Controller Class created and pi cam integration research conducted.

✔️12/18/2020: More turret features included in python file

✔️01/19/2021: Connecting RPI to Traxxas RC Car

✔️01/28/2021: Testing RPI wih bluetooth app to spin motor. Status: Unsuccesful

✔️01/30/2021: Powering RPI Externally tests. Status: TBD

✔️01/31/2021: Interesting read on Android app connection RPI.  Follow this [link](https://raspberrypi.stackexchange.com/questions/88214/setting-up-a-raspberry-pi-as-an-access-point-the-easy-way/88234#88234)

✔️02/02/2021: RPI Cam Research - Computer Vision?

✔️03/24/2021: Ordered Pixel 2 for development off Amazon, redesignig app for less clutter. All in for next 4 months. Up to date app not yet uploaded here.

✔️03/25/2021: Additional page for PILOT MODE, considering making Joystick, time permitted. Emulator demo coming soon...

✔️03/26/2021: Further app developments.

✔️03/28/2021: Minor app bug fixes encountered and temporary fixes applied. 

✔️03/29/2021: App developments - testing on PIXEL 2 is good!

✔️03/30/2021: App developments - enable/disable bluetooth, discover other bluetooth devices, and pairing. For a virtual device demo follow this [link](https://youtu.be/aG-tTt_GuIU)

✔️04/02/2021: App developments for bluetooth data transfers! Pairing is okay for now...
RPI screen coming Saturday. Will begin testing connections when screen comes in, results pending!

✔️04/04/2021: App developments - Sending/Receiving data code added - classes{accept/connect/connected}

✔️04/05/2021: RPI4 Screen and Keyboard received. Power tests resuming...

✔️04/07/2021: Successfully integrated Elecgrow display to RPI4. 

✔️04/08/2021: Conducting power tests with Metecsmart PowerBank. Goals for power test:

    - [ ] Avoid burning the RPI4
    - [ ] Run for 1 hour >
    - [ ] Powerbank provides enough supply to RPI4  








