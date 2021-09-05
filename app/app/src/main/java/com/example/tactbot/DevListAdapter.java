package com.example.tactbot;

import android.bluetooth.BluetoothDevice;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import java.util.ArrayList;

public class DevListAdapter extends ArrayAdapter<BluetoothDevice> {

    private LayoutInflater mLayoutInflater;
    private ArrayList<BluetoothDevice> mDevices;
    private int mViewSourceId;

    public DevListAdapter(Context context, int resource, ArrayList<BluetoothDevice> devices) {
        super(context, resource, devices);
        this.mDevices = devices;
        mLayoutInflater = (LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        mViewSourceId = resource;
    }

    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
        convertView = mLayoutInflater.inflate(mViewSourceId, null);
        BluetoothDevice device = mDevices.get(position);

        if(device != null){
            TextView devName = (TextView) convertView.findViewById(R.id.dev_name);
            TextView devAddress = (TextView) convertView.findViewById(R.id.dev_address);

            if(devName != null){
                devName.setText(device.getName());
            }
            if(devAddress != null){
                devAddress.setText(device.getAddress());
            }

        }
        return convertView;
    }
}
