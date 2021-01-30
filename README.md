# TactBot🤖
Project to create an Android Studio app that uses bluetooth to communicate with a RPI4. The RPI4 will interface
with an RC Car through the GPIO PWM Signals. Commands will be sent through bluetooth protocol and use of socket
programming. To access the manifest, main activity, and design file use the following path: App-Src-Main

Author: Anthony Vuong, Pedro Muñoz-Rodriguez

⌨️ Current Status: In Development 🟡
    
    Updated: 12 - 18 - 2020


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



