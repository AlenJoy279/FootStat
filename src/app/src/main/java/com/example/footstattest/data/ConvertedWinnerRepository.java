package com.example.footstattest.data;

import android.app.Application;

import androidx.lifecycle.LiveData;

import com.example.footstattest.models.ConvertedWinner;
import com.example.footstattest.models.League;
import com.example.footstattest.util.LeagueRoomDatabase;

import java.util.List;

public class ConvertedWinnerRepository {

    private ConvertedWinnerDao winnerDao;
    private LiveData<List<ConvertedWinner>> allWinners;

    public ConvertedWinnerRepository(Application application) {
        LeagueRoomDatabase db = LeagueRoomDatabase.getDatabase(application);
        winnerDao = db.winnerDao();

        allWinners = winnerDao.getAllWinners();
    }

    public LiveData<List<ConvertedWinner>> getAllWinners() {
        return allWinners;
    }
    public void insert(ConvertedWinner winner) {
        LeagueRoomDatabase.databaseWriteExecutor.execute(() -> {
            winnerDao.insert(winner);
        });
    }
}
