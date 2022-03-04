package com.example.footstattest.models.jaime;

import java.util.ArrayList;
import java.util.List;

public class MainResponse{
    private List<Standing> standings = new ArrayList<Standing>();
    public List<Standing> getStandings() {
        return standings;
    }
    public void setStandings(List<Standing> standings) {
        this.standings = standings;
    }
}
