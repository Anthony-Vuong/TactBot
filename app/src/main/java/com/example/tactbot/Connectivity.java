package com.example.tactbot;

import androidx.appcompat.app.AppCompatActivity;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

public class Connectivity extends AppCompatActivity {
    //Connectivity TAG
    private final static String TAG = "CONNECTIVITY ACTIVITY";

    //Bluetooth Adapter - fundamental bluetooth tasks, local to device
    BluetoothAdapter bluetoothAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_connectivity);

        //Set to local bluetooth adapter
        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        //On/off button - bluetooth on/off
        Button onOff = (Button)findViewById(R.id.btnOnOff);
        onOff.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                onOffBT();
            }
        });

        //On/off button - bluetooth on/off
        Button discover = (Button)findViewById(R.id.btnDiscover);
        discover.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                toggleDiscovery();
            }
        });
    }


    /////////////////////////////////// BROADCAST RECEIVER1 /////////////////////////////////////////////////

    private final BroadcastReceiver mBroadcastReceiver1 = new BroadcastReceiver() {
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if (action.equals(BluetoothAdapter.ACTION_STATE_CHANGED)) {
                final int state = intent.getIntExtra(BluetoothAdapter.EXTRA_STATE, bluetoothAdapter.ERROR);

                switch(state){
                    case BluetoothAdapter.STATE_OFF:
                        Log.d(TAG, "BT: OFF");
                        break;
                    case BluetoothAdapter.STATE_TURNING_OFF:
                        Log.d(TAG, "BT: TURNING OFF");
                        break;
                    case BluetoothAdapter.STATE_ON:
                        Log.d(TAG, "BT: ON");
                        break;
                    case BluetoothAdapter.STATE_TURNING_ON:
                        Log.d(TAG, "BT: TURNING ON");
                        break;
                    default:

                }
            }
        }
    };

    /////////////////////////////////// BROADCAST RECEIVER1 /////////////////////////////////////////////////



    /////////////////////////////////// BROADCAST RECEIVER2 /////////////////////////////////////////////////

    private final BroadcastReceiver mBroadcastReceiver2 = new BroadcastReceiver() {
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if (action.equals(BluetoothAdapter.ACTION_SCAN_MODE_CHANGED)) {
                final int mode = intent.getIntExtra(BluetoothAdapter.EXTRA_SCAN_MODE, bluetoothAdapter.ERROR);

                switch(mode){
                    case BluetoothAdapter.SCAN_MODE_CONNECTABLE_DISCOVERABLE:
                        Log.d(TAG, "MODE: DISCOVERABILITY ENABLED");
                        break;
                    case BluetoothAdapter.SCAN_MODE_CONNECTABLE:
                        Log.d(TAG, "MODE: DISCOVERABILITY DISABLED. ABLE TO RECEIVE CONNECTIONS");
                        break;
                    case BluetoothAdapter.SCAN_MODE_NONE:
                        Log.d(TAG, "MODE: DISCOVERABILITY DISABLED. NOT ABLE TO RECEIVE CONNECTIONS");
                        break;
                    case BluetoothAdapter.STATE_CONNECTING:
                        Log.d(TAG, "MODE: CONNECTING");
                        break;
                    case BluetoothAdapter.STATE_CONNECTED:
                        Log.d(TAG, "MODE: CONNECTED");
                        break;
                }
            }
        }
    };

    /////////////////////////////////// BROADCAST RECEIVER2 /////////////////////////////////////////////////


    @Override
    protected void onDestroy() {
        Log.d(TAG, "Destroying mBroadcastReceiver1");
        super.onDestroy();
        unregisterReceiver(mBroadcastReceiver1);
        unregisterReceiver(mBroadcastReceiver2);

    };


    public void onOffBT(){
        if(bluetoothAdapter == null){
            Log.d(TAG, "Device has no bluetooth capabilities.");
        }
        else {
            if (!bluetoothAdapter.isEnabled()) {
                Log.d(TAG, "Bluetooth is not enabled...ENABLING");

                //Intent - the glue that ties activities together, communication b/w app components
                Intent enableBTintent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
                //Launches a new activity
                startActivity(enableBTintent);
                //IntentFilter
                IntentFilter BTintent = new IntentFilter(BluetoothAdapter.ACTION_STATE_CHANGED);
                //RegisterReceiver
                registerReceiver(mBroadcastReceiver1, BTintent);

            } else {
                Log.d(TAG, "Bluetooth is enabled...DISABLING");

                bluetoothAdapter.disable();
                IntentFilter BTintent = new IntentFilter(BluetoothAdapter.ACTION_STATE_CHANGED);
                registerReceiver(mBroadcastReceiver1, BTintent);
            }
        }

    };

    public void toggleDiscovery() {
        Log.d(TAG, "Discovery: 60 sec window for discoverable devices");

        //Intent - the glue that ties activities together, communication b/w app components
        Intent discoverDevIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_DISCOVERABLE);
        //60 second window
        discoverDevIntent.putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, 60);
        //Launches a new activity
        startActivity(discoverDevIntent);
        //IntentFilter
        IntentFilter discoverIntent = new IntentFilter(BluetoothAdapter.ACTION_SCAN_MODE_CHANGED);
        //RegisterReceiver
        registerReceiver(mBroadcastReceiver2, discoverIntent);
    };
}