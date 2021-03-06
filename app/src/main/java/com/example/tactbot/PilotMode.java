package com.example.tactbot;

import android.os.Bundle;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.nio.charset.Charset;

public class PilotMode extends AppCompatActivity {

    private static final String TAG = "PILOT MODE ACTIVITY";
    //Bluetooth Connection Service - Bluetooth Util Class
    BluetoothUtil bluetoothUtil;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pilot_mode);

        //Stop Button
        Button stop = (Button)findViewById(R.id.btnStop);
        stop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.i(TAG, "Stop button logging");
                Toast.makeText(getApplicationContext(), "STOP!", Toast.LENGTH_SHORT).show();
            }
        });

        //Forward Button
        Button forward = (Button)findViewById(R.id.btnForward);
        forward.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.i(TAG, "Forward button logging");
                Toast.makeText(getApplicationContext(), "FORWARD!", Toast.LENGTH_SHORT).show();
                String forward = new String("1");
                byte[] bytes = forward.getBytes(Charset.defaultCharset());
                bluetoothUtil.write(bytes);
            }
        });

        //Backward Button
        Button backward = (Button)findViewById(R.id.btnBackward);
        backward.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.i(TAG, "Backward button logging");
                Toast.makeText(getApplicationContext(), "BACKWARD!", Toast.LENGTH_SHORT).show();
                String backward = new String("2");
                byte[] bytes = backward.getBytes(Charset.defaultCharset());
                bluetoothUtil.write(bytes);
            }
        });

        //Left Button
        Button left = (Button)findViewById(R.id.btnLeft);
        left.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.i(TAG, "Left button logging");
                Toast.makeText(getApplicationContext(), "LEFT!", Toast.LENGTH_SHORT).show();
                String left = new String("3");
                byte[] bytes = left.getBytes(Charset.defaultCharset());
                bluetoothUtil.write(bytes);
            }
        });

        //Right Button
        Button right = (Button)findViewById(R.id.btnRight);
        right.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.i(TAG, "Right button logging");
                Toast.makeText(getApplicationContext(), "RIGHT!", Toast.LENGTH_SHORT).show();
                String right = new String("4");
                byte[] bytes = right.getBytes(Charset.defaultCharset());
                bluetoothUtil.write(bytes);
            }
        });
    }
}