package com.example.footstattest;

import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.footstattest.models.ConvertedWinner;
import com.example.footstattest.models.LeagueViewModel;
import com.example.footstattest.models.WinnerViewModel;
import com.example.footstattest.util.LeagueWinnerConverter;
import com.example.footstattest.util.RecyclerViewAdapter;

import java.util.List;


public class MainActivity extends AppCompatActivity {

    private LeagueViewModel leagueViewModel;
    private WinnerViewModel winnerViewModel;
    private RecyclerView recyclerView;
    private RecyclerViewAdapter recyclerViewAdapter;
    private TextView textView;
    private LiveData<List<ConvertedWinner>> winnerList;


    LeagueWinnerConverter winners = LeagueWinnerConverter.createWinners();




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.recycler_view);
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));



//        Repository allLeagues = Repository.createLeagues();
//        Log.d("LeagueRepo","onCreate: " + allLeagues.getLeagueList().get(0).getEmblemUrl());



        winnerViewModel = new ViewModelProvider.AndroidViewModelFactory(this.getApplication()).create(WinnerViewModel.class);

        winnerViewModel.getAllWinners().observe(this, winners -> {

            recyclerViewAdapter = new RecyclerViewAdapter(winners, this);

            recyclerView.setAdapter(recyclerViewAdapter);


        });








    }
}