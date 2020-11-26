package com.example.tactbot;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Build;
import android.util.Log;
import android.view.View;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Switch;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    BluetoothAdapter bluetoothAdapter;
    private static final String TAG = "MainActivity";
    public DevListAdapter newDevListAdapter;
    public ArrayList<BluetoothDevice> btDevices = new ArrayList<>();
    ListView newDevices;


    private final BroadcastReceiver receiver2 = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            final String action = intent.getAction();
            if(action.equals(BluetoothAdapter.ACTION_SCAN_MODE_CHANGED)){
                int mode = intent.getIntExtra(BluetoothAdapter.EXTRA_SCAN_MODE, BluetoothAdapter.ERROR);
                switch(mode){
                    case BluetoothAdapter.SCAN_MODE_CONNECTABLE_DISCOVERABLE:
                        Log.d(TAG, "Receiver2: Enabled Discovery");
                        break;
                    case BluetoothAdapter.SCAN_MODE_CONNECTABLE:
                        Log.d(TAG, "Receiver2: Enabled Discovery And Can Receive Connections");
                        break;
                    case BluetoothAdapter.SCAN_MODE_NONE:
                        Log.d(TAG, "Receiver2: Enabled Discovery And Can not Receive Connections");
                        break;
                    case BluetoothAdapter.STATE_CONNECTING:
                        Log.d(TAG, "Receiver2: Process of connecting");
                        break;
                    case BluetoothAdapter.STATE_CONNECTED:
                        Log.d(TAG, "Receiver2: Connected");
                        break;
                }
            }
        }
    };



    private final BroadcastReceiver receiver1 = new BroadcastReceiver() {
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if (action.equals(bluetoothAdapter.ACTION_STATE_CHANGED)) {
                final int stat = intent.getIntExtra(BluetoothAdapter.EXTRA_STATE, bluetoothAdapter.ERROR);
                switch(stat){
                    case BluetoothAdapter.STATE_OFF:
                        Log.d(TAG, "Recieve on: State Off");
                        break;
                    case BluetoothAdapter.STATE_TURNING_OFF:
                        Log.d(TAG, "Reciever: State Turning Off");
                        break;
                    case BluetoothAdapter.STATE_ON:
                        Log.d(TAG, "Reciever: State On");
                        break;
                    case BluetoothAdapter.STATE_TURNING_ON:
                        Log.d(TAG, "Reciever: State Turning On");
                        break;
                }
            }
        }
    };
    private BroadcastReceiver receiver3 = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            final String action = intent.getAction();
            Log.d(TAG, "onReceive: ACTION FOUND");
            if(action.equals(BluetoothDevice.ACTION_FOUND)){
                BluetoothDevice dev = intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE);
                btDevices.add(dev);
                Log.d(TAG, "onReceive: " + dev.getName() + " " + dev.getAddress());
                newDevListAdapter = new DevListAdapter(context, R.layout.dev_adapter_view, btDevices);
                newDevices.setAdapter(newDevListAdapter);
            }
        }
    };

    @Override
    protected void onDestroy() {
        Log.d(TAG, "onDestroy");
        super.onDestroy();
        // Don't forget to unregister the ACTION_FOUND receiver.
        unregisterReceiver(receiver1);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Switch ctrlBLE = (Switch)findViewById(R.id.enSwitch);
        Button discoveryEnableDisable = (Button) findViewById(R.id.enDiscovery);
        newDevices = (ListView) findViewById(R.id.deviceListView);
        btDevices = new ArrayList<>();

        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        ctrlBLE.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d(TAG, "onClick");

                controlBluetooth();
            }
        });
    }

    public void controlBluetooth() {
        if (bluetoothAdapter == null) {
            Log.d(TAG, "Bluetooth is not available. ");
        } else if (bluetoothAdapter.isEnabled()) {
            Log.d(TAG, "Disabling BLE");

            bluetoothAdapter.disable();
            IntentFilter intentBLE = new IntentFilter(BluetoothAdapter.ACTION_STATE_CHANGED);
            registerReceiver(receiver1, intentBLE);
        } else {
            Log.d(TAG, "Enabling BLE");

            Intent intentEnableBLE = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
            startActivity(intentEnableBLE);

            IntentFilter intentBLE = new IntentFilter(BluetoothAdapter.ACTION_STATE_CHANGED);
            registerReceiver(receiver1, intentBLE);
        }
    }

    public void discoveryEnableDisable(View v){
            Log.d(TAG, "Called discoveryEnableDisable and awaiting connection for 5 minutes");

            Intent discoverIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_DISCOVERABLE);
            discoverIntent.putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, 300);
            startActivity(discoverIntent);

            IntentFilter intentfilter = new IntentFilter(BluetoothAdapter.ACTION_SCAN_MODE_CHANGED);
            registerReceiver(receiver1, intentfilter);

    }

    @RequiresApi(api = Build.VERSION_CODES.M)
    public void DiscoverDevices(View view) {
        Log.d(TAG, "Discover Button: Looking for unpaired devices");

        if(bluetoothAdapter.isDiscovering()){
            bluetoothAdapter.cancelDiscovery();
            Log.d(TAG, "Discover Button: Discovery Cancelled");

            CheckBTPermissions();

            bluetoothAdapter.startDiscovery();
            IntentFilter discoverDevicesIntent = new IntentFilter(BluetoothDevice.ACTION_FOUND);
            registerReceiver(receiver3, discoverDevicesIntent);
        }
        if(!bluetoothAdapter.isDiscovering()){
            CheckBTPermissions();
            bluetoothAdapter.startDiscovery();
            IntentFilter discoverDevicesIntent = new IntentFilter(BluetoothDevice.ACTION_FOUND);
            registerReceiver(receiver3, discoverDevicesIntent);
        }
    }

    @RequiresApi(api = Build.VERSION_CODES.M)
    private void CheckBTPermissions(){
        if(Build.VERSION.SDK_INT > Build.VERSION_CODES.LOLLIPOP){
            int permissionCheck = this.checkSelfPermission("Manifest.permission.ACCESS_FINE_LOCATION");
            permissionCheck += this.checkSelfPermission("Manifest.permission.ACCESS_COARSE_LOCATION");
            if(permissionCheck != 0){
                this.requestPermissions(new String[]{Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION}, 1001);
            }
        }
        else{
            Log.d(TAG, "check BT: Don't need to check permissions.");
        }

    }
}