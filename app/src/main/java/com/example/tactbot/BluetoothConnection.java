package com.example.tactbot;

import android.bluetooth.BluetoothAdapter;
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



}
