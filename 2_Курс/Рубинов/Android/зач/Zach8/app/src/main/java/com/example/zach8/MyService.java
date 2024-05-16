package com.example.zach8;

import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;
import android.os.Binder;
import android.os.IBinder;

import androidx.core.app.NotificationCompat;

public class MyService extends Service {

    public void onCreate(){
        super.onCreate();
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId){
        Notif1();
        return super.onStartCommand(intent,flags,startId);
    }

    private void Notif1() {

        NotificationCompat.Builder builder1 =
                new NotificationCompat.Builder(this)
                        .setSmallIcon(R.mipmap.ic_launcher)
                        .setContentTitle("Уведомление")
                        .setContentText("Это Уведомление");

        Notification notification1 = builder1.build();

        NotificationManager notificationManager =
                (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
        startForeground(1,notification1);

    }


    public IBinder onBind(Intent intent){

        return new Binder();
    }
    public boolean onUnbind(Intent intent) {
        return true;
    }

    public void onDestroy() {
        super.onDestroy();
    }

}