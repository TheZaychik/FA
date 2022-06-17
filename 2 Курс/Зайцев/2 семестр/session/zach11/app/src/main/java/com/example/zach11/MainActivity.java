package com.example.zach11;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView textView = findViewById(R.id.textView);
        TextView textView2 = findViewById(R.id.textView2);
        Button button = findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Runnable runnable = new Runnable() {
                    @Override
                    public void run() {
                        int counter = 0;
                        while (counter < 50){
                            counter += 1;
                            int finalCounter = counter;
                            textView.post(new Runnable() {
                                public void run() {
                                    textView.setText((finalCounter + ""));
                                }
                            });
                            try {
                                Thread.sleep(1000);
                            } catch (Exception e){
                                e.getMessage();
                            }

                        }
                    }
                };
                Thread thread = new Thread(runnable);
                thread.start();
            }
        });
        Button button2 = findViewById(R.id.button2);
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Runnable runnable = new Runnable() {
                    @Override
                    public void run() {
                        int counter = 0;
                        while (counter < 50){
                            counter += 1;
                            int finalCounter = counter;
                            textView2.post(new Runnable() {
                                public void run() {
                                    textView2.setText((finalCounter + ""));
                                }
                            });
                            try {
                                Thread.sleep(3000);
                            } catch (Exception e){
                                e.getMessage();
                            }

                        }
                    }
                };
                Thread thread = new Thread(runnable);
                thread.start();
            }
        });
    }
}