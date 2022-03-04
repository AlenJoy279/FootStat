package com.example.footstattest.models.jaime;

import java.util.ArrayList;
import java.util.List;

public class Season {
    private Integer id;
    private String startDate;
    private String endDate;
    private Integer currentMatchday;
    private List<String> availableStages = new ArrayList<String>();

    //Constructor
    Season(Integer id, String startDate, String endDate, Integer currentMatchday, List<String> availableStages){
        this.id = id;
        this.startDate = startDate;
        this.endDate = endDate;
        this.currentMatchday = currentMatchday;
        this.availableStages = availableStages;
    }

    // Getters and Setters
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
    public List<String> getAvailableStages() {
        return availableStages;
    }
    public void setAvailableStages(List<String> availableStages) {
        this.availableStages = availableStages;
    }
}
