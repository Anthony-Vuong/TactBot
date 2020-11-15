package com.example.tactbot;

import androidx.appcompat.app.AppCompatActivity;

import android.bluetooth.BluetoothAdapter;
import android.content.Intent;
import android.content.IntentFilter;
import android.util.Log;
import android.view.View;
import android.os.Bundle;
import android.widget.Switch;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    BluetoothAdapter bluetoothAdapter;

    // Create a BroadcastReceiver for ACTION_FOUND.
    private final broadCastReceiver receiver = new BroadcastReceiver() {
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if (action.equals(bluetoothAdapter.ACTION_STATE_CHANGED)) {

            }
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Switch ctrlBLE = (Switch)findViewById(R.id.enSwitch);

        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        ctrlBLE.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
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
            bluetoothAdapter.disable();
            IntentFilter intentBLE = new IntentFilter(BluetoothAdapter.ACTION_STATE_CHANGED);
            registerReceiver(broadCastReceiver, intentBLE);
        }
        else{
            Intent intentEnableBLE = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
            startActivity(intentEnableBLE);

            IntentFilter intentBLE = new IntentFilter(BluetoothAdapter.ACTION_STATE_CHANGED);
            registerReceiver(broadCastReceiver, intentBLE);
        }

    }


}