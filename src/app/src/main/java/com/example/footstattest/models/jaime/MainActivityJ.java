package com.example.footstattest.models.jaime;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.example.footstattest.LoginActivity;
import com.example.footstattest.MainActivity;
import com.example.footstattest.R;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


public class MainActivityJ extends AppCompatActivity {
    private Button button;
    List<Standing> dataList;
    private Button button1;
    private Button button2;
    private Button button3;
    private Button button4;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_j);

//        startActivity(new Intent(MainActivityJ.this, LoginActivity.class));
        
        Context context;

        TextView txt = (TextView) findViewById(R.id.textView7);
        button = (Button) findViewById(R.id.button3);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openBundesliga();
            }
        });

        button1 = (Button) findViewById(R.id.button1);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openLaLiga();
            }
        });

        button2 = (Button) findViewById(R.id.button4);
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openRankings();
            }
        });

        button3 = (Button) findViewById(R.id.button2);
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openPremierLeague();
            }
        });
        button3 = (Button) findViewById(R.id.button2);
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openPremierLeague();
            }
        });

        button4 = (Button) findViewById(R.id.button5);
        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openLeagues();
            }
        });

    }

    public void openBundesliga() {
        Intent intent = new Intent(this, BundesligaActivity.class);
        startActivity(intent);
    }
    public void openLaLiga() {
        Intent intent = new Intent(this, LaLigaActivity.class);
        startActivity(intent);
    }
    public void openRankings() {
        Intent intent = new Intent(this, TeamRankings.class);
        startActivity(intent);
    }
    public void openPremierLeague() {
        Intent intent = new Intent(this, PremierLeagueActivity.class);
        startActivity(intent);
    }
    public void openLeagues() {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }
}

