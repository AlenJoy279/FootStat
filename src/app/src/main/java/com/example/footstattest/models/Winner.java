package com.example.footstattest.models;

import androidx.room.Ignore;
import androidx.room.PrimaryKey;

import java.util.HashMap;
import java.util.Map;
public class Winner {

    @PrimaryKey(autoGenerate = true)
    private Integer id;

    private String name;
    private String shortName;

    @Ignore
    private String tla;
    private String crestUrl;

    public Integer getId() {
        return id;
    }

    public Winner(Integer id, String name, String shortName, String crestUrl) {
        this.id = id;
        this.name = name;
        this.shortName = shortName;
        this.crestUrl = crestUrl;
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
    public String getShortName() {
        return shortName;
    }
    public void setShortName(String shortName) {
        this.shortName = shortName;
    }
    public String getTla() {
        return tla;
    }
    public void setTla(String tla) {
        this.tla = tla;
    }
    public String getCrestUrl() {
        return crestUrl;
    }
    public void setCrestUrl(String crestUrl) {
        this.crestUrl = crestUrl;
    }

    @Override
    public String toString() {
        return "Winner{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", shortName='" + shortName + '\'' +
                ", tla='" + tla + '\'' +
                ", crestUrl='" + crestUrl + '\'' +
                '}';
    }
}