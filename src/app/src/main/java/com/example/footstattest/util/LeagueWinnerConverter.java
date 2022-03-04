package com.example.footstattest.util;

import android.util.Log;

import com.example.footstattest.data.Repository;
import com.example.footstattest.models.ConvertedWinner;

import java.util.ArrayList;

public class LeagueWinnerConverter {


    private ArrayList<ConvertedWinner> winnerList = new ArrayList<>();

    public LeagueWinnerConverter() {
    }

    public LeagueWinnerConverter(ArrayList<ConvertedWinner> winnerList) {
        this.winnerList = winnerList;
    }

    public static LeagueWinnerConverter createWinners() {

        // Create league set for conversion into ConvertedWinner for easy database creation
        Repository allLeagues = Repository.createLeagues();

        LeagueWinnerConverter latest = new LeagueWinnerConverter();

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < allLeagues.getLeagueList().get(i).getSeasons().size(); j ++) {

            ConvertedWinner winner = new ConvertedWinner(allLeagues.getLeagueList().get(i).getSeasons().get(j).getWinner().getId(),
                    allLeagues.getLeagueList().get(i).getSeasons().get(j).getWinner().getName(),
                    allLeagues.getLeagueList().get(i).getSeasons().get(j).getWinner().getShortName(),
                    allLeagues.getLeagueList().get(i).getSeasons().get(j).getWinner().getCrestUrl(),
                    allLeagues.getLeagueList().get(i).getName(),
                    allLeagues.getLeagueList().get(i).getSeasons().get(j).getEndDate());


            latest.getWinnerList().add(winner);
            }


        }

        return latest;

    }

    public ArrayList<ConvertedWinner> getWinnerList() {
        return winnerList;
    }

    public void setWinnerList(ArrayList<ConvertedWinner> winnerList) {
        this.winnerList = winnerList;
    }
}
