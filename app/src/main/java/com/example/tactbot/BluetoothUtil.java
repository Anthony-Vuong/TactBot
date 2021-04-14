package com.example.tactbot;

import android.app.ProgressDialog;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothServerSocket;
import android.bluetooth.BluetoothSocket;
import android.content.Context;
import android.icu.util.Output;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.charset.Charset;
import java.util.UUID;

public class BluetoothUtil {

    private static final String TAG = "Bluetooth Utilities";
    private static final String appName = "TactBot";
    private static final UUID MY_UUID_INSECURE = UUID.fromString("8ce255c0-200a-11e0-ac64-0800200c9a66");
    private final BluetoothAdapter bluetoothAdapter;
    private AcceptThread acceptThread;
    private ConnectThread connectThread;
    private ConnectedThread connectedThread;

    private BluetoothDevice bluetoothDevice;
    private UUID devUUID;
    ProgressDialog mProgressDialog;
    Context context;

    public BluetoothUtil(Context con_context){
        context = con_context;
        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        start();
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
                connected(socket, bluetoothDevice);
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

    private class ConnectedThread extends Thread{
        private final BluetoothSocket bluetoothSocket;
        private final InputStream inputStream;
        private final OutputStream outputStream;

        public ConnectedThread(BluetoothSocket socket){
            bluetoothSocket = socket;
            InputStream inTemp = null;
            OutputStream outTemp = null;

            mProgressDialog.dismiss();

            try {
                inTemp = bluetoothSocket.getInputStream();
                outTemp = bluetoothSocket.getOutputStream();

            } catch (IOException e) {
                e.printStackTrace();
            }


            inputStream = inTemp;
            outputStream = outTemp;
        }

        public void run(){
            byte[] buffer = new byte[1024];

            int bytes;

            while(true){
                try {
                    bytes = inputStream.read(buffer);
                    String message = new String(buffer, 0, bytes);
                } catch (IOException e) {
                    e.printStackTrace();
                    break;
                }

            }
        }

        public void write(byte[] bytes){
            String text = new String(bytes, Charset.defaultCharset());

            try {
                outputStream.write(bytes);
            } catch (IOException e) {
                e.printStackTrace();
            }

        }

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
        mProgressDialog = ProgressDialog.show(context, "Connecting...", "Waiting for connection...", true);

        connectThread = new ConnectThread(device, uuid);
        connectThread.start();

    }

    private void connected(BluetoothSocket socket, BluetoothDevice blueDev){
        connectedThread = new ConnectedThread(socket);
        connectedThread.start();
    }

    public void write(byte[] bytes){
        ConnectedThread connectedThread1;
        connectedThread.write(bytes);

    }


}
