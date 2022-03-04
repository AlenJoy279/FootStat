package com.example.footstattest.models;

import java.util.HashMap;
import java.util.Map;
public class CurrentSeason {
    private Integer id;
    private String startDate;
    private String endDate;
    private Integer currentMatchday;
    private Object winner;
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
    public Integer getCurrentMatchday() {
        return currentMatchday;
    }
    public void setCurrentMatchday(Integer currentMatchday) {
        this.currentMatchday = currentMatchday;
    }
    public Object getWinner() {
        return winner;
    }
    public void setWinner(Object winner) {
        this.winner = winner;
    }

    @Override
    public String toString() {
        return "CurrentSeason{" +
                "id=" + id +
                ", startDate='" + startDate + '\'' +
                ", endDate='" + endDate + '\'' +
                ", currentMatchday=" + currentMatchday +
                ", winner=" + winner +
                '}';
    }
}