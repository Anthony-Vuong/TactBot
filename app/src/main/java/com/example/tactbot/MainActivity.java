package com.example.tactbot;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MAIN PAGE ACTIVITY";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

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
            }
        });

        //Backward Button
        Button backward = (Button)findViewById(R.id.btnBackward);
        backward.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.i(TAG, "Backward button logging");
                Toast.makeText(getApplicationContext(), "BACKWARD!", Toast.LENGTH_SHORT).show();
            }
        });

        //Left Button
        Button left = (Button)findViewById(R.id.btnLeft);
        left.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.i(TAG, "Left button logging");
                Toast.makeText(getApplicationContext(), "LEFT!", Toast.LENGTH_SHORT).show();
            }
        });

        //Right Button
        Button right = (Button)findViewById(R.id.btnRight);
        right.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.i(TAG, "Right button logging");
                Toast.makeText(getApplicationContext(), "RIGHT!", Toast.LENGTH_SHORT).show();
            }
        });

        //Connectivity Button - leads to Connectivity page
        Button button1 = (Button) findViewById(R.id.btnConnectivity);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(view.getContext(), Connectivity.class);
                view.getContext().startActivity(intent);}
        });
    }
}