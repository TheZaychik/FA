package com.example.spravkaapp;

import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

import java.io.*;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
//        try {
//            Context context = getBaseContext();
//            FileInputStream fis = context.openFileInput("save.out");
//            ObjectInputStream is = new ObjectInputStream(fis);
//            Single.getInstance().recs = (ArrayList<Records>)is.readObject();
//            is.close();
//            fis.close();
//        } catch (FileNotFoundException e) {
//            e.printStackTrace();
//        } catch (IOException | ClassNotFoundException e) {
//            e.printStackTrace();
//        }
        setContentView(R.layout.activity_main);
        ListView listView = findViewById(R.id.main_list);

        ArrayAdapter<Records> adapter = new ArrayAdapter<>(this,
                android.R.layout.simple_list_item_1, Single.getInstance().recs);
        listView.setAdapter(adapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View v, int position, long id) {
                Intent i = new Intent(MainActivity.this, ShowRecord.class);
                i.putExtra("pos", position);
                startActivity(i);
            }
        });

    }

    public void fabHandler(View view) {

        startActivity(new Intent(this, CreateRecord.class));
    }

    @Override
    protected void onStop() {
        Context context = getBaseContext();
        super.onStop();
        try {
            FileOutputStream fos = context.openFileOutput("save.out", Context.MODE_PRIVATE);
            ObjectOutputStream os = new ObjectOutputStream(fos);
            os.writeObject(Single.getInstance().recs);
            fos.close();
            os.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}