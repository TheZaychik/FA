package com.example.zach13;

import androidx.appcompat.app.AppCompatActivity;

import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import java.util.concurrent.TimeUnit;

public class MainActivity extends AppCompatActivity {

    private TextView mInfoTextView;
    private Button mStartButton;
    int counter = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mInfoTextView = findViewById(R.id.info_text);
        mStartButton = findViewById(R.id.start_button);
    }

    public void onClick(View view) {
        counter = 0;
        TimeTask timTask = new TimeTask();
        timTask.execute();
    }

    class TimeTask extends AsyncTask<Void, Void, Void> {

        @Override
        protected void onPreExecute() {
            super.onPreExecute();
            mInfoTextView.setText("Отсчёт пошёл");
            mStartButton.setVisibility(View.INVISIBLE);
        }

        @Override
        protected Void doInBackground(Void... voids) {
            try {
                TimeUnit.SECONDS.sleep(5);
                for (int i = 0; i < 10; i++) {
                    counter = counter + 100000;
                }
            }
            catch (InterruptedException e) {
                e.printStackTrace();
            }

            return null;
        }

        @Override
        protected void onPostExecute(Void aVoid) {
            super.onPostExecute(aVoid);
            mStartButton.setVisibility(View.VISIBLE);
            mInfoTextView.setText("Насчитало: " + counter);

        }
    }
}