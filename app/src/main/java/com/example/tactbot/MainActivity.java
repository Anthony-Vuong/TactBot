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

        //Connectivity Button - leads to Connectivity page
        Button connectivity = (Button) findViewById(R.id.btnConnectivity);
        connectivity.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(MainActivity.this, Connectivity.class));}
        });

        //Pilot Mode Button - leads to Controls Page
        Button pilotMode = (Button) findViewById(R.id.btnPilotMode);
        pilotMode.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(view.getContext(), PilotMode.class);
                view.getContext().startActivity(intent);}
        });
    }
}