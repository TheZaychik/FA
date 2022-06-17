package com.example.zach12;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final Button btnStart = findViewById(R.id.button);


        final int[] schet = {0};
        btnStart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //final int[] per = {0};
                Runnable runnable = new Runnable() {
                    public void run() {
                        long endTime = System.currentTimeMillis()
                                + 20 * 1000;

                        while (System.currentTimeMillis() < endTime) {
                            synchronized (this) {
                                try {
                                    wait(endTime -
                                            System.currentTimeMillis());
                                } catch (Exception e) {
                                }
                            }
                        }
                        //Сложынй для обработки процесс
                        schet[0]++; //Увелечение показателя счетчика

                          handler.sendEmptyMessage(0);
                    }
                };
                Thread thread = new Thread(runnable);
                thread.start();
            }
            Handler handler = new Handler(){
                @Override
                public void handleMessage(Message msg) {
                    TextView infoTextView =
                            (TextView) findViewById(R.id.textView);
                    infoTextView.setText("Этот счетчик изменяется в фоновом потоке и передается на интерфейс: " + schet[0]);
                } //Посредник между фоновым и главным потоком
            };
        });
    }
}