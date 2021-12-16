package com.example.clicer;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    TextView mainText;
    Button mainBtn,mainBtnDec;
    ImageButton mainBtnDel;
    private long score = 0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mainText = (TextView) findViewById(R.id.mainTxt);
        mainBtn = (Button) findViewById(R.id.main_btn);
        View.OnClickListener clickListener = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (score >= 0 && score <= 1) {
                    score++;
                    String s = "Кнопка нажата " + score + " раз";
                    mainText.setText(s.toCharArray(), 0, s.length());
                } else if (score > 1 && score <= 4) {
                    score++;
                    String s = "Кнопка нажата " + score + " раза";
                    mainText.setText(s.toCharArray(), 0, s.length());
                } else if (score > 4 && score <= 20) {
                    score++;
                    String s = "Кнопка нажата " + score + " раз";
                    mainText.setText(s.toCharArray(), 0, s.length());
                } else if (score > 20 && score <= 24) {
                    score++;
                    String s = "Кнопка нажата " + score + " раза";
                    mainText.setText(s.toCharArray(), 0, s.length());
                } else if (score > 24 && score <= 31) {
                    score++;
                    String s = "Кнопка нажата " + score + " раз";
                    mainText.setText(s.toCharArray(), 0, s.length());
                }
            }
        };
        mainBtn.setOnClickListener(clickListener);
        mainBtnDec = (Button) findViewById(R.id.main_btn_dec);
        View.OnClickListener clickListenerForDec = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (score >= 1 && score <= 2) {
                    score--;
                    String s = "Кнопка нажата " + score + " раз";
                    mainText.setText(s.toCharArray(), 0, s.length());
                } else if (score > 2 && score <= 5) {
                    score--;
                    String s = "Кнопка нажата " + score + " раза";
                    mainText.setText(s.toCharArray(), 0, s.length());
                } else if (score > 5 && score <= 22) {
                    score--;
                    String s = "Кнопка нажата " + score + " раз";
                    mainText.setText(s.toCharArray(), 0, s.length());
                } else if (score > 22 && score <= 25) {
                    score--;
                    String s = "Кнопка нажата " + score + " раза";
                    mainText.setText(s.toCharArray(), 0, s.length());
                } else if (score > 22 && score <= 32) {
                    score--;
                    String s = "Кнопка нажата " + score + " раз";
                    mainText.setText(s.toCharArray(), 0, s.length());
                } else {
                    String s = "Уменьшать больше некуда";
                    mainText.setText(s.toCharArray(), 0, s.length());
                }
            }
        };

        mainBtnDec.setOnClickListener(clickListenerForDec);
        mainBtnDel = (ImageButton) findViewById(R.id.main_btn_del);
        View.OnClickListener clickListenerForDel = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                score=0;
                    String s = "Кнопка нажата 0 раз";
                    mainText.setText(s.toCharArray(), 0, s.length());
            }
        };
        mainBtnDel.setOnClickListener(clickListenerForDel);
    }
}