package com.example.newapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;


public class MainActivity extends AppCompatActivity implements View.OnClickListener, AdapterView.OnItemClickListener {
    public TextView mainTextView;
    public EditText mainEditText;
    ListView mainListView;
    ArrayAdapter mArrayAdapter;
    ArrayList mNameList = new ArrayList();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mainTextView = findViewById(R.id.main_textview);
        mainTextView.setText("Привет textview!");
        Button mainButton,mainButton_1;
        mainButton = findViewById(R.id.main_button);
        mainButton.setOnClickListener(this);

        mainEditText = (EditText) findViewById(R.id.main_edittext);

        mainListView = findViewById(R.id.main_listview);
        mArrayAdapter = new ArrayAdapter(this,
                android.R.layout.simple_list_item_1,
                mNameList);
        mainListView.setAdapter(mArrayAdapter);

        mainListView.setOnItemClickListener(this);

        mainButton_1 = findViewById(R.id.main_button_1);
        mainButton_1.setOnClickListener(this);
        mainButton_1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Set<String> s = new LinkedHashSet<>(mNameList);
                mNameList.clear();
                mNameList.addAll(s);
                Collections.sort(mNameList);
                mArrayAdapter.notifyDataSetChanged();
            }
        });
    }

    @Override
    public void onClick(View view) {
        mainTextView.setText("Button pressed!");
        mainTextView.setText(mainEditText.getText().toString() + " добавлен в TextView!");
        mNameList.add(mainEditText.getText().toString());
        mArrayAdapter.notifyDataSetChanged();
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
        Log.d("omg android", i + ": " + mNameList.get(i));
        mainTextView.setText(mNameList.get(i).toString()
                + " is learning Android development!");
        mNameList.remove(i);
        mArrayAdapter.notifyDataSetChanged();
    }
}