package com.example.tactbot;

import android.app.ProgressDialog;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothServerSocket;
import android.bluetooth.BluetoothSocket;
import android.content.Context;
import android.content.Intent;
import android.icu.util.Output;
import android.util.Log;

import androidx.localbroadcastmanager.content.LocalBroadcastManager;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.charset.Charset;
import java.util.UUID;


public class BluetoothUtil {

    private static final String TAG = "Bluetooth Utilities";
    private static final String appName = "TactBot";
    private static final UUID MY_UUID_INSECURE = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");
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
                Log.d(TAG, "AcceptThread: Setting up Server using: " + MY_UUID_INSECURE);
            } catch (IOException e) {
                Log.e(TAG, "AcceptThread: IOException: " + e.getMessage());
            }

            serverSocket = tmp;
        }

        public void run(){
            Log.d(TAG, "Running AccceptThread");
            BluetoothSocket socket = null;

            try {
                Log.d(TAG, "RFCOM server socket start: AccceptThread");

                socket = serverSocket.accept();

                Log.d(TAG, "RFCOM server socket accepted connection: AccceptThread");

            } catch (IOException e) {
                Log.e(TAG, "AcceptThread: IOException: " + e.getMessage());

            }

            if(socket != null){
                connected(socket, bluetoothDevice);
            }

            Log.i(TAG, "END acceptThread");
        }

        public void cancel(){
            try {
                Log.d(TAG, "Cancelling AccceptThread");

                serverSocket.close();
            } catch (IOException e) {
                Log.e(TAG, "Could not close AcceptThread Socket " + e.getMessage());

            }
        }


    }

    private class ConnectThread extends Thread{
        private BluetoothSocket bluetoothSocket;

        public ConnectThread(BluetoothDevice blueDev, UUID theUUID){
            Log.d(TAG, "Started ConnectThread");
            bluetoothDevice = blueDev;
            devUUID = theUUID;
        }


        public void run(){
            BluetoothSocket tmp = null;
            Log.i(TAG, "Running ConnectThread");
            try {
                Log.d(TAG, "Using UUID to create InsRfCommSkt: ConnectThread " + MY_UUID_INSECURE);
                tmp = bluetoothDevice.createInsecureRfcommSocketToServiceRecord(devUUID);
            } catch (IOException e) {
                Log.e(TAG, "Could not create RFcomm socket: ConnectThread: Run");
            }

            bluetoothSocket = tmp;

            //Discovery slows process down - cancel after a connection has been established
            bluetoothAdapter.cancelDiscovery();

            try {
                bluetoothSocket.connect();
                Log.d(TAG, "SUCCESFUL: ConnectThread: run");
            } catch (IOException e) {
                try {
                    bluetoothSocket.close();
                    Log.d(TAG, "UNSUCCESFUL: SOCKET CLOSED: ConnectThread: run");

                } catch (IOException ioException) {
                    Log.e(TAG, "Could not close socket" + ioException.getMessage());
                }
                Log.d(TAG, "Could not connect to UUID: ConnectThread: run: " + MY_UUID_INSECURE);

            }

            connected(bluetoothSocket, bluetoothDevice);
        }


        public void cancel(){
            try {
                Log.d(TAG, "Cancelling ConnectThread");
                bluetoothSocket.close();
            } catch (IOException e) {
                Log.e(TAG, "Could not close ConnectThread Socket " + e.getMessage());

            }
        }

    }

    private class ConnectedThread extends Thread{
        private final BluetoothSocket bluetoothSocket;
        private final InputStream inputStream;
        private final OutputStream outputStream;

        public ConnectedThread(BluetoothSocket socket){
            Log.d(TAG, "Started CONNECTEDThread");

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
                    Log.d(TAG, "Input stream: " + message);

                    Intent incomingMessageIntent = new Intent("Incoming Message");
                    incomingMessageIntent.putExtra("theMessage", message);
                    LocalBroadcastManager.getInstance(context).sendBroadcast(incomingMessageIntent);

                } catch (IOException e) {
                    Log.e(TAG, "Error reading to input stream");

                    break;
                }
            }
        }

        public void write(byte[] bytes){
            String text = new String(bytes, Charset.defaultCharset());
            Log.d(TAG, "Writing to output stream: write " + text);

            try {
                outputStream.write(bytes);
            } catch (IOException e) {
                Log.e(TAG, "Error writing to output stream");
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
        Log.d(TAG, "start method");
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
        Log.d(TAG, "startClient method");

        mProgressDialog = ProgressDialog.show(context, "Connecting...", "Waiting for connection...", true);

        connectThread = new ConnectThread(device, uuid);
        connectThread.start();

    }

    private void connected(BluetoothSocket socket, BluetoothDevice blueDev){
        Log.d(TAG, "connected method: Starting");
        connectedThread = new ConnectedThread(socket);
        connectedThread.start();
    }

    public void write(byte[] bytes){
        ConnectedThread connectedThread1;
        Log.d(TAG, "write method: Starting");

        connectedThread.write(bytes);

    }


}
