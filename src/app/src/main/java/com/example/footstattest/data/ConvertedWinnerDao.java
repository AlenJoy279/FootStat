package com.example.footstattest.data;


import androidx.lifecycle.LiveData;
import androidx.room.Dao;
import androidx.room.Insert;
import androidx.room.OnConflictStrategy;
import androidx.room.Query;

import com.example.footstattest.models.ConvertedWinner;

import java.util.List;

@Dao
public interface ConvertedWinnerDao {

    // CRUD Ops
    @Insert(onConflict = OnConflictStrategy.IGNORE)
    void insert(ConvertedWinner winner);

    @Query("DELETE FROM league_winner_table")
    void deleteAll();

    @Query("SELECT * FROM league_winner_table ORDER BY leagueName ASC")
    LiveData<List<ConvertedWinner>> getAllWinners();

}
