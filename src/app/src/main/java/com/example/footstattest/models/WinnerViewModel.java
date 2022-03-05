package com.example.footstattest.models;

import android.app.Application;

import androidx.annotation.NonNull;
import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;

import com.example.footstattest.data.ConvertedWinnerRepository;
import com.example.footstattest.util.LeagueWinnerConverter;

import java.util.List;

public class WinnerViewModel extends AndroidViewModel {

    public static ConvertedWinnerRepository repository;
    public final LiveData<List<ConvertedWinner>> allWinners;

    public WinnerViewModel(@NonNull Application application) {
        super(application);
        repository = new ConvertedWinnerRepository(application);
        allWinners = repository.getAllWinners();
    }

    public LiveData<List<ConvertedWinner>> getAllWinners() {
        return allWinners;
    }

    public static void insert(ConvertedWinner winner) {

    }
}
