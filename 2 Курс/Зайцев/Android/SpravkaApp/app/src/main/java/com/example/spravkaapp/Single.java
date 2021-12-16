package com.example.spravkaapp;

import java.util.ArrayList;

public class Single {

    private static final Single INSTANCE = new Single();
    ArrayList<Records> recs;
    private Single() {
        recs = new ArrayList<>();
    }

    public static Single getInstance() {
        return INSTANCE;
    }
}
