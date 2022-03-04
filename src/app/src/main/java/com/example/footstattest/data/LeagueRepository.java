package com.example.footstattest.data;

import android.app.Application;

import androidx.lifecycle.LiveData;

import com.example.footstattest.models.League;
import com.example.footstattest.util.LeagueRoomDatabase;

import java.util.List;

public class LeagueRepository {
    
    private LeagueDao leagueDao;
    private LiveData<List<League>> allLeagues;
    
    public LeagueRepository(Application application) {
        LeagueRoomDatabase db = LeagueRoomDatabase.getDatabase(application);
        leagueDao = db.leagueDao();
        
        allLeagues = leagueDao.getAllLeagues();
    }

    public LiveData<List<League>> getAllLeagues() {
        return allLeagues;
    }
    public void insert(League league) {
        LeagueRoomDatabase.databaseWriteExecutor.execute(() -> {
            leagueDao.insert(league);
        });
    }
}
