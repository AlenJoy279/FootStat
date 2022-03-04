package com.example.footstattest.models;

import android.app.Application;

import androidx.annotation.NonNull;
import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;

import com.example.footstattest.data.LeagueRepository;

import java.util.List;

public class LeagueViewModel extends AndroidViewModel {

    public static LeagueRepository repository;
    public final LiveData<List<League>> allLeagues;

    public LeagueViewModel(@NonNull Application application) {
        super(application);
        repository = new LeagueRepository(application);
        allLeagues = repository.getAllLeagues();


    }

    public LiveData<List<League>> getAllLeagues() {
        return allLeagues;
    }

    public static void insert(League league) {
        repository.insert(league);
    }
}
