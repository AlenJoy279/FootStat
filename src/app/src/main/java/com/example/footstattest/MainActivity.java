package com.example.footstattest;

import android.os.Bundle;
import android.widget.ListView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.example.footstattest.models.League;
import com.example.footstattest.models.LeagueViewModel;

import java.util.ArrayList;


public class MainActivity extends AppCompatActivity {

    private LeagueViewModel leagueViewModel;
    private TextView textView;
    private ListView listView;
    private ArrayList<String> leagueString;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        textView = findViewById(R.id.textView0);



//        Repository allLeagues = Repository.createLeagues();
//        Log.d("LeagueRepo","onCreate: " + allLeagues.getLeagueList().get(0).getEmblemUrl());


        leagueViewModel = new ViewModelProvider.AndroidViewModelFactory(
                MainActivity.this.getApplication()).create(LeagueViewModel.class);

        leagueViewModel.getAllLeagues().observe(this, leagues -> {

            StringBuilder builder = new StringBuilder();

            for (League league:leagues) {
                builder.append(" - Name: ").append(league.getName()).append("Code: ")
                        .append(league.getCode()).append(" EmblemUrl: ").append(league.getEmblemUrl()).append(league.getId()).append("\n\n");

            }
            textView.setText(builder);
        });




    }
}