package com.example.guessnumber;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.*;

import java.util.Random;


public class MainActivity extends AppCompatActivity {
    TextView tvInfo;
    EditText etInput;
    Button bControl;
    public int score;
    public boolean win=false;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        tvInfo = (TextView)findViewById(R.id.textView);
        etInput = (EditText)findViewById(R.id.editTextNumber);
        bControl = (Button)findViewById(R.id.button);
        Random r = new Random();
        score = r.nextInt(100-1+1)+1;
    }
    public void onClick(View v) {
        int next;
        if (etInput.getText().toString().isEmpty()){
            tvInfo.setText(getResources().getString(R.string.error_empty));
        }
        else{
        next = Integer.parseInt(etInput.getText().toString());
        if (win == false && next > 0 && next < 101 && next < score) {
            tvInfo.setText(getResources().getString(R.string.behind));
        } else if (win == false && next > 0 && next < 101 && next > score) {
            tvInfo.setText(getResources().getString(R.string.ahead));
        } else if (win == false && next > 0 && next < 101 && next == score) {
            tvInfo.setText(getResources().getString(R.string.hit));
            bControl.setText(getResources().getString(R.string.play_more));
            win = true;
        } else if (win == true && next > 0 && next < 101) {
            Random r = new Random();
            score = r.nextInt(100 - 1 + 1) + 1;
            win = false;
            bControl.setText(getResources().getString(R.string.guess));
            tvInfo.setText(getResources().getString(R.string.try_to_guess));
        } else if ((next < 0 || next > 100)) {
            tvInfo.setText(getResources().getString(R.string.error));
        }
        }
    }

    public void OnClick_exit(View v) {
        moveTaskToBack(true);
        finish();
    }
}