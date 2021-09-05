package com.example.tactbot;

import android.bluetooth.BluetoothDevice;
import android.content.Context;
import android.text.Layout;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.util.ArrayList;

//This class is used with listview to shoe the name and address of each unpaired/discoverable devices
public class DeviceListAdapter extends ArrayAdapter<BluetoothDevice> {
    private LayoutInflater layoutInflater;
    private ArrayList<BluetoothDevice> devices;
    private int sourceID;

    public DeviceListAdapter(Context context, int constResID, ArrayList<BluetoothDevice> constDevices){
        super(context, constResID, constDevices);
        this.devices = constDevices;
        layoutInflater = (LayoutInflater)context.getSystemService(context.LAYOUT_INFLATER_SERVICE);
        sourceID = constResID;
    }

    public View getView(int position, View convertView, ViewGroup parent){
        convertView = layoutInflater.inflate(sourceID, null);
        BluetoothDevice device = devices.get(position);

        if(device != null){
            TextView devName = (TextView)convertView.findViewById(R.id.textViewDevName);
            TextView devAddress = (TextView)convertView.findViewById(R.id.textViewDevAddress);

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
