package com.example.lab5_1;

import android.app.Service;
import android.content.Intent;
import android.os.Binder;
import android.os.IBinder;

public class MyService extends Service {


    public void onCreate(){
        super.onCreate();
        System.out.println("onCreate");
    }

    public int onStartCommand(Intent intent, int flags, int startId){
        System.out.println("onStartCommand");
        someTask();
        return super.onStartCommand(intent,flags,startId);
    }

    public IBinder onBind(Intent intent){
        System.out.println("onBind");
        return new Binder();
    }

    @Override
    public void onRebind(Intent intent) {
        super.onRebind(intent);
        System.out.println("onRebind");
    }

    public boolean onUnbind(Intent intent){
        System.out.println("onUnbind");
        return true;
    }

    public void onDestroy(){
        super.onDestroy();
        System.out.println("onDestroy");
    }

    void someTask(){

    }
}
