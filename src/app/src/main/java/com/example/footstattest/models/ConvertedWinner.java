package com.example.footstattest.models;

import androidx.room.Entity;
import androidx.room.PrimaryKey;

@Entity(tableName = "league_winner_table")
public class ConvertedWinner extends Winner{


    private String leagueName;
    private String seasonEndDate;


    public ConvertedWinner( Integer id, String name, String shortName, String crestUrl, String leagueName, String seasonEndDate) {
        super(id, name, shortName, crestUrl);
        this.leagueName = leagueName;
        this.seasonEndDate = seasonEndDate;
    }


    public String getLeagueName() {
        return leagueName;
    }

    public void setLeagueName(String leagueName) {
        this.leagueName = leagueName;
    }

    public String getSeasonEndDate() {
        return seasonEndDate;
    }

    public void setSeasonEndDate(String seasonEndDate) {
        this.seasonEndDate = seasonEndDate;
    }

    @Override
    public String toString() {
        return "ConvertedWinner{" +
                "id=" + getId() +
                ", name='" + getName() + '\'' +
                ", shortName='" + getShortName() + '\'' +
                ", crestUrl='" + getCrestUrl() + '\'' +
                "leagueName='" + leagueName + '\'' +
                ", seasonEndDate='" + seasonEndDate + '\'' +
                '}';
    }
}
