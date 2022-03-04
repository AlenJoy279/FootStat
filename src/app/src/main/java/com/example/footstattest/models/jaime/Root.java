package com.example.footstattest.models.jaime;

import java.util.ArrayList;
import java.util.List;

public class Root {
    private Filters filters;
    private Competition competition;
    private Season season;
    private List<Standing> standings = new ArrayList<Standing>();

    //Constructor
    public Root(Filters filters, Competition competition, Season season, List<Standing> standings){
        this.filters = filters;
        this.competition = competition;
        this.season = season;
        this.standings = standings;
    }


    // Getters and Setters
    public Filters getFilters() {
        return filters;
    }
    public void setFilters(Filters filters) {
        this.filters = filters;
    }

    public Competition getCompetition() {
        return competition;
    }
    public void setCompetition(Competition competition) {
        this.competition = competition;
    }

    public Season getSeason() {
        return season;
    }
    public void setSeason(Season season) {
        this.season = season;
    }

    public List<Standing> getStandings() {
        return standings;
    }
    public void setStandings(List<Standing> standings) {
        this.standings = standings;
    }
}
