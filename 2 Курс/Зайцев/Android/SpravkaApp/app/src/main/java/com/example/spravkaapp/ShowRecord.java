package com.example.spravkaapp;

import android.content.Intent;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import com.google.android.material.textfield.TextInputLayout;

public class ShowRecord extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_show_record);
        Bundle arguments = getIntent().getExtras();
        TextView textView = findViewById(R.id.textView);
        TextInputLayout textInputLayout = findViewById(R.id.textInputLayout);
        Records rec = Single.getInstance().recs.get(arguments.getInt("pos"));
        textView.setText(rec.date);
        textInputLayout.getEditText().setText(rec.text);
    }

    public void del_btn(View view){
        Bundle arguments = getIntent().getExtras();
        Single.getInstance().recs.remove(arguments.getInt("pos"));
        Intent i;
        i = new Intent(this, MainActivity.class);
        startActivity(i);

    }

    public void back_btn(View view){
        Bundle arguments = getIntent().getExtras();
        TextView textView = findViewById(R.id.textView);
        TextInputLayout textInputLayout = findViewById(R.id.textInputLayout);
        String text = textInputLayout.getEditText().getText().toString();
        String date = textView.getText().toString();
        Records rec = new Records(date, text);
        Single.getInstance().recs.set(arguments.getInt("pos"), rec);
        Intent i;
        i = new Intent(this, MainActivity.class);
        startActivity(i);
    }
}