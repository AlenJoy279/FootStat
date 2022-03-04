package com.example.footstattest;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.example.footstattest.data.LeagueRepository;
import com.example.footstattest.data.Repository;
import com.example.footstattest.models.League;
import com.example.footstattest.models.LeagueViewModel;
import com.example.footstattest.util.LeagueWinnerConverter;


public class MainActivity extends AppCompatActivity {

    private LeagueViewModel leagueViewModel;
    private TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        textView = findViewById(R.id.textView);

//        Repository allLeagues = Repository.createLeagues();
//        Log.d("LeagueRepo","onCreate: " + allLeagues.getLeagueList().get(0).getEmblemUrl());


        leagueViewModel = new ViewModelProvider.AndroidViewModelFactory(
                MainActivity.this.getApplication()).create(LeagueViewModel.class);

        leagueViewModel.getAllLeagues().observe(this, leagues -> {

            StringBuilder builder = new StringBuilder();

            for (League league:leagues) {
                builder.append(" - ").append(league.getName()).append(" ")
                        .append(league.getCode()).append(" ").append(league.getEmblemUrl()).append("\n");

                Log.d("MainAct", "onCreate: " + league.getName());
                Log.d("MainAct", "onCreate: " + league.getCode());
            }
            textView.setText(builder);
        });

        startActivity(new Intent(MainActivity.this, LoginActivity.class));







    }
}