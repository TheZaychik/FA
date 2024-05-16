package com.example.spravkaapp;

import android.content.Intent;
import android.text.Editable;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import com.google.android.material.textfield.TextInputLayout;

public class CreateRecord extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create_record);

    }

    public void saveHandler(View view){
        EditText editText = findViewById(R.id.editTextDate);
        TextInputLayout textInputLayout = findViewById(R.id.textInputLayout);
        String text = textInputLayout.getEditText().getText().toString();
        String date = editText.getText().toString();
        Records rec = new Records(date, text);
        Single.getInstance().recs.add(rec);

        Intent i;
        i = new Intent(this, MainActivity.class);
        startActivity(i);

    }
}