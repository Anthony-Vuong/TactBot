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


public class PilotMode extends AppCompatActivity implements JoyStick.JoystickListener {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        JoyStick js = new JoyStick(this);
        setContentView(js);




    }

    @Override
    public void onJoystickMoved(float xPercent, float yPercent, int id) {
        Log.d("Main Method", "X percent: " + xPercent + " Y percent: " + yPercent);


    }
}