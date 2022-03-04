package com.example.footstattest.models;

import androidx.room.Entity;

import java.util.HashMap;
import java.util.Map;


public class Season {
    private Integer id;
    private String startDate;
    private String endDate;
    private Object currentMatchday;
    private Winner winner;
    public Integer getId() {
        return id;
    }
    public void setId(Integer id) {
        this.id = id;
    }
    public String getStartDate() {
        return startDate;
    }
    public void setStartDate(String startDate) {
        this.startDate = startDate;
    }
    public String getEndDate() {
        return endDate;
    }
    public void setEndDate(String endDate) {
        this.endDate = endDate;
    }
    public Object getCurrentMatchday() {
        return currentMatchday;
    }
    public void setCurrentMatchday(Object currentMatchday) {
        this.currentMatchday = currentMatchday;
    }
    public Winner getWinner() {
        return winner;
    }
    public void setWinner(Winner winner) {
        this.winner = winner;
    }

    @Override
    public String toString() {
        return "Season{" +
                "id=" + id +
                ", startDate='" + startDate + '\'' +
                ", endDate='" + endDate + '\'' +
                ", currentMatchday=" + currentMatchday +
                ", winner=" + winner +
                '}';
    }

}