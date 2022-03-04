package com.example.footstattest.util;

import android.content.Context;
import android.util.Log;

import androidx.annotation.NonNull;
import androidx.room.AutoMigration;
import androidx.room.Database;
import androidx.room.Room;
import androidx.room.RoomDatabase;
import androidx.sqlite.db.SupportSQLiteDatabase;

import com.example.footstattest.data.ConvertedWinnerDao;
import com.example.footstattest.data.LeagueDao;
import com.example.footstattest.data.Repository;
import com.example.footstattest.models.ConvertedWinner;
import com.example.footstattest.models.League;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@Database(version = 1, entities = {League.class, ConvertedWinner.class}, exportSchema = false)
public abstract class LeagueRoomDatabase extends RoomDatabase {

    // Creating a thread pool of executors to perform database operations
    // Doing this keeps the main thread free to handle user interaction and other main activities
    // This will prevent users experiencing perceivable slowdown on most devices

    public abstract LeagueDao leagueDao();
    public abstract ConvertedWinnerDao winnerDao();
    public static final int THREADS = 4;

    public static volatile LeagueRoomDatabase INSTANCE;
    public static final ExecutorService databaseWriteExecutor =
            Executors.newFixedThreadPool(THREADS);



    public static LeagueRoomDatabase getDatabase(final Context context) {

        if (INSTANCE == null) {
            synchronized (LeagueRoomDatabase.class) {
                if (INSTANCE == null) {

                    INSTANCE = Room.databaseBuilder(context.getApplicationContext(),
                    LeagueRoomDatabase.class, "league_database")
                            .addCallback(sRoomDatabaseCallback).build();

                    // Once the database is built, this callback executes the below function
                }
            }
        }

        return INSTANCE;
    }

    public static RoomDatabase.Callback sRoomDatabaseCallback =
            new RoomDatabase.Callback() {
                @Override
                public void onCreate(@NonNull SupportSQLiteDatabase db) {
                    super.onCreate(db);
                    Repository allLeagues = Repository.createLeagues();
                    LeagueWinnerConverter  winners = LeagueWinnerConverter.createWinners();

                    // Executors are sent to write data without using the main thread

                    databaseWriteExecutor.execute(() -> {
                        LeagueDao leagueDao = INSTANCE.leagueDao();
                        ConvertedWinnerDao winnerDao = INSTANCE.winnerDao();

                        leagueDao.deleteAll();

                        for (int i = 0; i < allLeagues.getLeagueList().size(); i++)
                            leagueDao.insert(allLeagues.getLeagueList().get(i));

                        for (ConvertedWinner winner: winners.getWinnerList())
                            winnerDao.insert(winner);


                    });
                }
            };




}
