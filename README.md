# TactBot🤖
Wireless robot project that uses bluetooth from Android device to communicate with a RPI4. The RPI4 will interface
with an RC Car through the GPIO PWM Signals. Commands will be sent through Android bluetooth protocol. To access the manifest, 
main activity, and design file use the following path: App-Src-Main

Author: Anthony Vuong, Pedro Muñoz-Rodriguez

Development Status:
                  
                     App: In Development 🟡
                  
                   Rover: In Development 🟡
                  
                  Turret: On Hold 🔴
    
    
                  Updated: 06 - 18 - 2021


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

  - [x] Avoid burning the RPI4
  - [x] Run for 1 hour >
  - [x] Powerbank provides enough supply to RPI4  
  
  💡 Future testing - running scripts with multiple peripherals
  
✔️04/13/2021: More helpful links to interfacing RPI with Traxxas RC Car: 

   L1(Itemis): [link](https://blogs.itemis.com/en/how-to-set-up-a-robocar-platform-with-a-remote-control-unit)
   L2(Instructables): [link](https://www.instructables.com/Raspberry-Pi-Remote-Controlled-Car-1/)
   
   RPI4 UUID: Which one? "4E90-7B95", "21466080-2A52-48fb-8f2c-32f4f424694c", "0355-D7B0", "1542b7d9-e011-4ca2-9c6d-80d5af3b811c"

✔️04/15/2021: The following link will help in a huge in milestone on the project. Thank you Electrofun! Here is link:  [link](https://www.youtube.com/watch?v=NddZnd95cyE)

✔️05/24/2021: New route taken to control RPI4 through Android App and Bluetooth: Android App -> Bluetooth -> HC06 -> RPI4; SUCCESS with new approach - Able to send messages from App to RPI4!

✔️05/31/2021: Switching App Acitivites problems. Will develop all controls on one activity for now. Creating serial script to command rover.

✔️06/03/2021: App updates: Adding rover controls to connectivity page. Activity life cycle research needed for multi activity app.

✔️06/18/2021: Created documentation for code - not completely updated.

✔️06/21/2021: Created driver file for rover.

✔️06/23/2021: Tested Bluetooth signal with RPI4 PWM with success - getting rid of timeout for serial port. Git repo on RPI4 created. Project meeting on 6/22.

✔️07/01/2021: Hardware connections for RPI4 and Traxxas Stampede RC Car  [link](https://projects.digilentinc.com/surrogatetv/internet-controlled-rc-car-with-hd-video-using-raspberry-pi-4b728c)




