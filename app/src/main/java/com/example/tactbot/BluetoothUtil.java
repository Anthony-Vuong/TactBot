package com.example.tactbot;

import android.app.ProgressDialog;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothServerSocket;
import android.bluetooth.BluetoothSocket;
import android.content.Context;

import java.io.IOException;
import java.util.UUID;

public class BluetoothUtil {

    private static final String TAG = "Bluetooth Utilities";
    private static final String appName = "TactBot";
    private static final UUID MY_UUID_INSECURE = UUID.fromString("8ce255c0-200a-11e0-ac64-0800200c9a66");
    private final BluetoothAdapter bluetoothAdapter;
    private AcceptThread acceptThread;
    private ConnectThread connectThread;
    private BluetoothDevice bluetoothDevice;
    private UUID devUUID;
    Context context;

    public BluetoothUtil(Context con_context){
        context = con_context;
        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
    }


    private class AcceptThread extends  Thread{
        private final BluetoothServerSocket serverSocket;

        public AcceptThread(){
            BluetoothServerSocket tmp = null;

            try {
                tmp = bluetoothAdapter.listenUsingRfcommWithServiceRecord(appName, MY_UUID_INSECURE);
            } catch (IOException e) {
                e.printStackTrace();
            }

            serverSocket = tmp;
        }

        public void run(){
            BluetoothSocket socket = null;

            try {
                socket = serverSocket.accept();
            } catch (IOException e) {
                e.printStackTrace();
            }

            if(socket != null){
                connected(socket, dev);
            }
        }

        public void cancel(){
            try {
                serverSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }


    }

    private class ConnectThread extends Thread{
        private BluetoothSocket bluetoothSocket;

        public ConnectThread(BluetoothDevice blueDev, UUID theUUID){
            bluetoothDevice = blueDev;
            devUUID = theUUID;
        }

        //
        public void run(){
            BluetoothSocket tmp = null;

            try {
                tmp = bluetoothDevice.createInsecureRfcommSocketToServiceRecord(devUUID);
            } catch (IOException e) {
                e.printStackTrace();
            }

            bluetoothSocket = tmp;

            bluetoothAdapter.cancelDiscovery();

            try {
                bluetoothSocket.connect();
            } catch (IOException e) {
                try {
                    bluetoothSocket.close();
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                }
                e.printStackTrace();
            }

            connected(bluetoothSocket, bluetoothDevice);
        }

        //
        public void cancel(){
            try {
                bluetoothSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }


    }


    public synchronized  void start(){
        if(connectThread != null){
            connectThread.cancel();
            connectThread = null;
        }
        if(acceptThread != null){
            acceptThread = new AcceptThread();
            acceptThread.start();
        }
    }

    public void startClient(BluetoothDevice device, UUID uuid){
        ProgressDialog mProgressDialog = ProgressDialog.show(context, "Connecting...", "Waiting for connection...", true);

        connectThread = new ConnectThread(device, uuid);
        connectThread.start();

    }


}
