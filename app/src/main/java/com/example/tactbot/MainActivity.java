package com.example.tactbot;

import androidx.appcompat.app.AppCompatActivity;

import android.bluetooth.BluetoothAdapter;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.util.Log;
import android.view.View;
import android.os.Bundle;
import android.widget.Switch;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    BluetoothAdapter bluetoothAdapter;
    private static final String TAG = "MainActivity";

    private final BroadcastReceiver receiver = new BroadcastReceiver() {
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

    @Override
    protected void onDestroy() {
        Log.d(TAG, "onDestroy");
        super.onDestroy();
        // Don't forget to unregister the ACTION_FOUND receiver.
        unregisterReceiver(receiver);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Switch ctrlBLE = (Switch)findViewById(R.id.enSwitch);

        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        ctrlBLE.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d(TAG, "onClick");

                controlBluetooth();
            }
        });
    }

    public void controlBluetooth()
    {
        if(bluetoothAdapter == null){
            Log.d(TAG, "Bluetooth is not available. ");
        }
        else if(bluetoothAdapter.isEnabled()){
            Log.d(TAG, "Disabling BLE");

            bluetoothAdapter.disable();
            IntentFilter intentBLE = new IntentFilter(BluetoothAdapter.ACTION_STATE_CHANGED);
            registerReceiver(receiver, intentBLE);
        }
        else{
            Log.d(TAG, "Enabling BLE");

            Intent intentEnableBLE = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
            startActivity(intentEnableBLE);

            IntentFilter intentBLE = new IntentFilter(BluetoothAdapter.ACTION_STATE_CHANGED);
            registerReceiver(receiver, intentBLE);
        }

    }


}