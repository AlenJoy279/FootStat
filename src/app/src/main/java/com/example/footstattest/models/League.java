package com.example.footstattest.models;

import androidx.annotation.NonNull;
import androidx.room.ColumnInfo;
import androidx.room.Entity;
import androidx.room.Ignore;
import androidx.room.PrimaryKey;

import java.util.ArrayList;
import java.util.List;

@Entity(tableName = "league_table")
public class League {
    
    @PrimaryKey(autoGenerate = true)
    @ColumnInfo(name = "id")
    private Integer id;

    @ColumnInfo(name ="league_name")
    private String name;

    @ColumnInfo(name ="league_code")
    private String code;

    @ColumnInfo(name = "emblem_url")
    private String emblemUrl;

    @Ignore
    private CurrentSeason currentSeason;

    @Ignore
    private List<Season> seasons = new ArrayList<Season>();

    @Ignore
    private String lastUpdated;

    public Integer getId() {
        return id;
    }
    public void setId(Integer id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getCode() {
        return code;
    }
    public void setCode(String code) {
        this.code = code;
    }
    public String getEmblemUrl() {
        return emblemUrl;
    }
    public void setEmblemUrl(String emblemUrl) {
        this.emblemUrl = emblemUrl;
    }

    public CurrentSeason getCurrentSeason() {
        return currentSeason;
    }
    public void setCurrentSeason(CurrentSeason currentSeason) {
        this.currentSeason = currentSeason;
    }
    public List<Season> getSeasons() {
        return seasons;
    }
    public void setSeasons(List<Season> seasons) {
        this.seasons = seasons;
    }
    public String getLastUpdated() {
        return lastUpdated;
    }
    public void setLastUpdated(String lastUpdated) {
        this.lastUpdated = lastUpdated;
    }

    public League(@NonNull String name, @NonNull String code, String emblemUrl) {
        this.name = name;
        this.code = code;
        this.emblemUrl = emblemUrl;
    }

    @Override
    public String toString() {

        return "League{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", code='" + code + '\'' +
                ", emblemUrl=" + emblemUrl +
                ", currentSeason=" + currentSeason +
                ", seasons=" + seasons +
                ", lastUpdated='" + lastUpdated + '\'' +
                '}';
    }
}
