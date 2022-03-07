package com.example.footstattest.data;

import androidx.lifecycle.LiveData;
import androidx.room.Dao;
import androidx.room.Insert;
import androidx.room.OnConflictStrategy;
import androidx.room.Query;

import com.example.footstattest.models.League;

import java.util.ArrayList;
import java.util.List;

@Dao
public interface LeagueDao {

    // This data access object (DAO) enables us to perform our CRUD operations
    @Insert(onConflict = OnConflictStrategy.IGNORE)
    void insert(League league);

    @Query("DELETE FROM league_table")
    void deleteAll();

    @Query("SELECT * FROM league_table ORDER BY league_name ASC")
    LiveData<List<League>> getAllLeagues();
}
