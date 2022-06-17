package com.example.lab5_1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.util.Log;
import android.view.View;


public class MainActivity extends AppCompatActivity {
    Intent intent;
    ServiceConnection sConn;
    boolean bound = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        intent = new Intent(this, MyService.class);

        sConn = new ServiceConnection() {
            @Override
            public void onServiceConnected(ComponentName name, IBinder service) {
                System.out.println("Connected");
                bound = true;
            }

            @Override
            public void onServiceDisconnected(ComponentName name) {
                System.out.println("Unconnected");
                bound = false;
            }
        };
    }

    public void startService(View view){
        startService(intent);
    }

    public void stopService(View view){
        stopService(intent);
    }

    public void ClickBind(View view){
        bindService(intent, sConn,BIND_AUTO_CREATE );
    }

    public void ClickUnbind(View view){
        if (!bound) return;
        unbindService(sConn);
        bound = false;
    }
}