package com.example.lab5_5;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.widget.Toast;

public class MessageReceiver extends BroadcastReceiver {

    public MessageReceiver() {
    }

    @Override
    public void onReceive(Context context, Intent intent) {
        Toast.makeText(context, "Входящее сообщение: " +
                        intent.getStringExtra("com.example.broadcast.Message"),
                Toast.LENGTH_LONG).show();

    }

}