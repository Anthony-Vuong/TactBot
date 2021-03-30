package com.example.tactbot;

import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.ListView;

import java.util.ArrayList;

public class Connectivity extends AppCompatActivity implements AdapterView.OnItemClickListener {
    //Connectivity TAG
    private final static String TAG = "CONNECTIVITY ACTIVITY";

    //Bluetooth Adapter - fundamental bluetooth tasks, local to device
    BluetoothAdapter bluetoothAdapter;

    //Arraylist to hold discovered devices
    public ArrayList<BluetoothDevice> btDevices = new ArrayList<>();

    //DeviceListAdapter to help display device name/address in listview
    public DeviceListAdapter deviceListAdapter;

    //ListView to display devices
    ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_connectivity);

        //Set to local bluetooth adapter
        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        //List view of devices, id from xml file
        listView = (ListView)findViewById(R.id.DeviceList);
        listView.setOnItemClickListener(Connectivity.this);

        //Array of bluetooth devices
        btDevices = new ArrayList<>();

        //On/off button - bluetooth on/off
        Button onOff = (Button)findViewById(R.id.btnOnOff);
        onOff.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                toggleBT();
            }
        });

        Button discover = (Button)findViewById(R.id.btnDiscover);
        discover.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                toggleDiscovery();
            }
        });

        Button devices = (Button)findViewById(R.id.btnDevices);
        devices.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                listDevices();
            }
        });

        IntentFilter pairIntent = new IntentFilter(BluetoothDevice.ACTION_BOND_STATE_CHANGED);
        registerReceiver(mBroadcastReceiver4, pairIntent);
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

    /////////////////////////////////// BROADCAST RECEIVER3 /////////////////////////////////////////////////

    private final BroadcastReceiver mBroadcastReceiver3 = new BroadcastReceiver() {
        public void onReceive(Context context, Intent intent) {
            final String action = intent.getAction();
            if (action.equals(BluetoothDevice.ACTION_FOUND)) {
                //Retrieves bluetooth device previously added from intent
                BluetoothDevice dev = intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE);
                //Add device to array list
                btDevices.add(dev);
                Log.d(TAG, "Device list adding: " + dev.getName() + " " + dev.getAddress());

                deviceListAdapter = new DeviceListAdapter(context, R.layout.activity_device_list_adapter, btDevices);
                listView.setAdapter(deviceListAdapter);


            }
        }
    };

    /////////////////////////////////// BROADCAST RECEIVER3 /////////////////////////////////////////////////

    /////////////////////////////////// BROADCAST RECEIVER4 /////////////////////////////////////////////////

    private final BroadcastReceiver mBroadcastReceiver4 = new BroadcastReceiver() {
        public void onReceive(Context context, Intent intent) {
            final String action = intent.getAction();
            if (action.equals(BluetoothDevice.ACTION_BOND_STATE_CHANGED)) {
                BluetoothDevice copyDev = intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE);

                if(copyDev.getBondState() == BluetoothDevice.BOND_BONDED){
                    Log.d(TAG, "BOND: BONDED");
                }
                if(copyDev.getBondState() == BluetoothDevice.BOND_BONDING){
                    Log.d(TAG, "BOND: BONDING");
                }
                if(copyDev.getBondState() == BluetoothDevice.BOND_NONE){
                    Log.d(TAG, "BOND: NONE");
                }

            }
        }
    };

    /////////////////////////////////// BROADCAST RECEIVER4 /////////////////////////////////////////////////


    @Override
    protected void onDestroy() {
        super.onDestroy();
        if(mBroadcastReceiver1 != null){
            Log.d(TAG, "Destroying mBroadcastReceiver1");

            unregisterReceiver(mBroadcastReceiver1);
        }
        if(mBroadcastReceiver2 != null){
            Log.d(TAG, "Destroying mBroadcastReceiver2");

            unregisterReceiver(mBroadcastReceiver2);
        }
        if(mBroadcastReceiver3 != null){
            Log.d(TAG, "Destroying mBroadcastReceiver3");

            unregisterReceiver(mBroadcastReceiver3);
        }

        if(mBroadcastReceiver4 != null){
            Log.d(TAG, "Destroying mBroadcastReceiver4");

            unregisterReceiver(mBroadcastReceiver4);
        }

    };


    public void toggleBT(){
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

    public void listDevices(){
        Log.d(TAG, "listDevices: Listing discovered devices ");
        if(bluetoothAdapter.isDiscovering()){
            Log.d(TAG, "listDevices:isDiscovering: Cancel Discovery");
            bluetoothAdapter.cancelDiscovery();

            //For Android Version above 6, include these permissions
            checkBTpermissions();

            Log.d(TAG, "listDevices:isDiscovering: StartDiscovery");
            bluetoothAdapter.startDiscovery();

            IntentFilter deviceIntent = new IntentFilter(BluetoothDevice.ACTION_FOUND);
            registerReceiver(mBroadcastReceiver3, deviceIntent);
        }
        if(!bluetoothAdapter.isDiscovering()){
            Log.d(TAG, "listDevices:isNotDiscovering: StartDiscovery");

            checkBTpermissions();
            bluetoothAdapter.startDiscovery();
            IntentFilter deviceIntent = new IntentFilter(BluetoothDevice.ACTION_FOUND);
            registerReceiver(mBroadcastReceiver3, deviceIntent);
        }
    }

    private void checkBTpermissions(){

        if(Build.VERSION.SDK_INT > Build.VERSION_CODES.LOLLIPOP){
            //Checks the app if the permission is granted
            int permissionCheck = this.checkSelfPermission("Manifest.permission.ACCESS_COARSE_LOCATION");
            permissionCheck += this.checkSelfPermission("Manifest.permission.ACCESS_FINE_LOCATION");
            if(permissionCheck != 0){
                //Requests approval for permissions passed in as string
                this.requestPermissions(new String[]{Manifest.permission.ACCESS_COARSE_LOCATION, Manifest.permission.ACCESS_FINE_LOCATION}, 1001);
            }
        }
    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        bluetoothAdapter.cancelDiscovery();

        String devName = btDevices.get(position).getName();
        String devAddress= btDevices.get(position).getAddress();

        if(Build.VERSION.SDK_INT > Build.VERSION_CODES.JELLY_BEAN_MR2){
            btDevices.get(position).createBond();
        }

    }
}