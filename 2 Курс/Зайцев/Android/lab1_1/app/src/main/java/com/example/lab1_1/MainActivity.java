package com.example.lab1_1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    public TextView mainTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // 1. Access the TextView defined in layout XML
        // and then set its text
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mainTextView =  (TextView) findViewById(R.id.main_textview);
        mainTextView .setText("Set in Java!");
    }
}