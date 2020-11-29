package com.example.tactbot;

import android.app.ProgressDialog;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothServerSocket;
import android.bluetooth.BluetoothSocket;
import android.content.Context;
import android.util.Log;

import java.io.IOException;
import java.util.UUID;

public class BluetoothConnection {
    private static final String TAG = "BluetoothConnection";
    private static final String appName = "tactBotApp";
    private static final UUID myUUIDInsecure =
            UUID.fromString("8ce255c0-200a-11e0-ac64-0800200c9a66");
    private final BluetoothAdapter bleAdapter;
    private AcceptThread insecureAcceptThread;
    private ConnectThread connectThread;
    private BluetoothDevice bluetoothDevice;
    private UUID devUUID;
    ProgressDialog progressDialog;
    Context myContext;

    public BluetoothConnection(Context context){
        myContext = context;
        bleAdapter = BluetoothAdapter.getDefaultAdapter();
    }

    private class AcceptThread extends Thread{
        private BluetoothServerSocket serverSocket;
        public AcceptThread(){
            BluetoothServerSocket temp = null;

            try {
                temp = bleAdapter.listenUsingInsecureRfcommWithServiceRecord(appName, myUUIDInsecure);
                Log.d(TAG, "Accept Thread: Setting up server with: " + myUUIDInsecure);
            } catch (IOException e) {
                e.printStackTrace();
            }

            serverSocket = temp;
        }

        public void run(){
            Log.d(TAG, "RUN: Accept thread processing");
            BluetoothSocket skt = null;
            try {
                Log.d(TAG, "RUN: RFCOM server socket start.");
                skt = serverSocket.accept();
                Log.d(TAG, "RUN: RFCOM server socket accepted.");
            } catch (IOException e) {
                e.printStackTrace();
            }

            if(skt != null){
                connected(skt, myDev);
            }
            Log.d(TAG, "End of Accept thread.");
        }

        public void cancel(){
            Log.d(TAG, "cancel: Cancelling Accept thread.");
            try{
                serverSocket.close();
            }catch (IOException E){
                Log.e(TAG, "cancel: Closing Accept thread failed.");
            }
        }
    }

    private class ConnectThread extends Thread{
        private BluetoothSocket bleSkt;
        public ConnectThread(BluetoothDevice dev, UUID uuid){
            Log.d(TAG, "ConnectThread: start");
            bluetoothDevice = dev;
            devUUID = uuid;
        }

        public void run(){
            BluetoothSocket temp = null;
            Log.i(TAG, "Run ConnectThread");

            try {
                Log.d(TAG, "ConnectThread: Creating RFCOMM Socket");
                temp = bluetoothDevice.createInsecureRfcommSocketToServiceRecord(devUUID);
            } catch (IOException e) {
                Log.d(TAG, "ConnectThread: Creating RFCOMM Socket failed");
                e.printStackTrace();
            }
            bleSkt = temp;
            bleAdapter.cancelDiscovery();

            try {
                Log.d(TAG, "ConnectThread: Trying to connect");
                bleSkt.connect();
            } catch (IOException e) {
                try {
                    bleSkt.close();
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                }
                Log.d(TAG, "ConnectThread: Trying to connect failed");
                e.printStackTrace();
            }

            connected(bleSkt, bluetoothDevice);
        }

        public void cancel(){
            try {
                bleSkt.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public synchronized void start(){
        Log.d(TAG, "START");
        if(connectThread != null){
            connectThread.cancel();
            connectThread = null;
        }
        if(insecureAcceptThread == null){
            insecureAcceptThread = new AcceptThread();
            insecureAcceptThread.start();
        }
    }

    public void startClient(BluetoothDevice device, UUID uuid){
        Log.d(TAG, "START client");

        progressDialog = ProgressDialog.show(myContext, "Connecting bluetooth", "Please wait...", true);

        connectThread = new ConnectThread(device, uuid);
        connectThread.start();
    }
}
