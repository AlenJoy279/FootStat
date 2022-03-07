package com.example.footstattest.models;

import android.graphics.drawable.Drawable;

import androidx.room.Entity;
import androidx.room.Ignore;
import androidx.room.PrimaryKey;

import java.io.InputStream;
import java.net.URL;

/* Winner (and almost any other object we need to put in a database) needed to be converted before
 it was possible to add them to the database. This was because SQLite can't parse objects having
 another object as an attribute. This version inherits some props we want from winner + some props
 from league.
 */
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

    // Code to get crest icon from url. Does not support SVG format images
    // Source: https://stackoverflow.com/questions/6407324/how-to-display-image-from-url-on-android

    public static Drawable LoadImageFromWebOperations(String url) {
        try {
            if (!(url.endsWith("svg"))) {
                InputStream is = (InputStream) new URL(url).getContent();
                Drawable d = Drawable.createFromStream(is, "png image");
                return d;
            } else {
                return null;}
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
