package com.example.tactbot;

import androidx.appcompat.app.AppCompatActivity;

import android.bluetooth.BluetoothAdapter;
import android.content.Intent;
import android.view.View;
import android.os.Bundle;
import android.widget.Switch;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    BluetoothAdapter bluetoothAdapter;
    Switch sw1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        sw1 = (Switch)findViewById(R.id.enSwitch);
    }

    public void enableBluetooth(View v)
    {
        if (sw1.isChecked()) {
            if(bluetoothAdapter == null){
                Toast.makeText(getApplicationContext(), "Bluetooth is not supported.", Toast.LENGTH_SHORT).show();
            }
            else{
                if(!bluetoothAdapter.isEnabled()){
                    Intent i = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
                    startActivityForResult(i, 1);
                }
            }
        }
        else {
            if(!bluetoothAdapter.isEnabled()){ }
            else{
                bluetoothAdapter.disable();
            }
        }
    }


}