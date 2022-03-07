package com.example.footstattest.models.jaime;

import java.util.ArrayList;

public class EloScore {

    private String name;
    private double score;


    public EloScore(String name, double score) {
        this.name = name;
        this.score = score;
    }

    public EloScore() {
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getScore() {
        return score;
    }

    public void setScore(double score) {
        this.score = score;
    }

}
