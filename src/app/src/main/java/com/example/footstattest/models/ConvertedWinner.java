package com.example.footstattest.models;

import android.graphics.drawable.Drawable;

import androidx.room.Entity;
import androidx.room.Ignore;
import androidx.room.PrimaryKey;

import java.io.InputStream;
import java.net.URL;

@Entity(tableName = "league_winner_table")
public class ConvertedWinner extends Winner{


    private String leagueName;
    private String seasonEndDate;
    @Ignore
    private Drawable crest;


    public ConvertedWinner( Integer id, String name, String shortName, String crestUrl, String leagueName, String seasonEndDate) {
        super(id, name, shortName, crestUrl);
        this.leagueName = leagueName;
        this.seasonEndDate = seasonEndDate;
        this.crest = LoadImageFromWebOperations(crestUrl);
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

    public Drawable getCrest() {
        return crest;
    }

    public void setCrest(Drawable crest) {
        this.crest = crest;
    }

    // Code to get crest icon from url.
    // Source: https://stackoverflow.com/questions/6407324/how-to-display-image-from-url-on-android

    public static Drawable LoadImageFromWebOperations(String url) {
        try {
            InputStream is = (InputStream) new URL(url).getContent();
            Drawable d = Drawable.createFromStream(is, "svg images");
            return d;
        } catch (Exception e) {
            return null;
        }
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
