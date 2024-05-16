package com.example.spravkaapp;

public class Records {
    String date;
    String text;

    public Records(String _date, String _text){
        date = _date;
        text = _text;
    }

    @Override
    public String toString() {
        return date;
    }
}
