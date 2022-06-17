package com.example.lab5_2;

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

        Intent Ac1 =new Intent(this, MainActivity2.class);
        PendingIntent Ac1Pen  =
                PendingIntent.getActivity(this,0,Ac1,0);
        Intent Ac2 =new Intent(this, MainActivity3.class);
        PendingIntent Ac2Pen  =
                PendingIntent.getActivity(this,0,Ac2,0);

        NotificationCompat.Builder builder1 =
                new NotificationCompat.Builder(this)
                            .setSmallIcon(R.mipmap.ic_launcher)
                            .setContentTitle("Уведомление")
                            .setContentText("Это текст уведомления")
                            .setContentIntent(Ac1Pen);

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