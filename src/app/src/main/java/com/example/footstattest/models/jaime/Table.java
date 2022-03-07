package com.example.footstattest.models.jaime;

public class Table {
    private Integer position;
    private Team team;
    private Integer playedGames;
    private Integer won;
    private Integer draw;
    private Integer lost;
    private Integer points;
    private Integer goalsFor;
    private Integer goalsAgainst;
    private Integer goalDifference;
    private String name;

    // Constructor
    public Table(Integer position, Team team, Integer playedGames, Integer won, Integer draw, Integer lost, Integer points, Integer goalsFor, Integer goalsAgainst, Integer goalDifference){
        this.position = position;
        this.team = team;
        this.playedGames = playedGames;
        this.won = won;
        this.draw = draw;
        this.lost = lost;
        this.points = points;
        this.goalsFor = goalsFor;
        this.goalsAgainst = goalsAgainst;
        this.goalDifference = goalDifference;
    }

    public Table(Integer position, Team team, Integer won, Integer draw, Integer lost) {
    }

    public Table(Integer position, Integer won, Integer draw, Integer lost) {
        this.position = position;
        this.won = won;
        this.draw = draw;
        this.lost = lost;
    }

    public Table(Integer position, Integer won, Integer draw, Integer lost, String name) {
        this.position = position;
        this.won = won;
        this.draw = draw;
        this.lost = lost;
        this.name = name;
    }

    public Table() {

    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    // Getters and Setters
    public Integer getPosition() {
        return position;
    }
    public void setPosition(Integer position) {
        this.position = position;
    }

    public Team getTeam() {
        return team;
    }
    public void setTeam(Team team) {
        this.team = team;
    }

    public Integer getPlayedGames() {
        return playedGames;
    }
    public void setPlayedGames(Integer playedGames) {
        this.playedGames = playedGames;
    }

    public Integer getWon() {
        return won;
    }
    public void setWon(Integer won) {
        this.won = won;
    }

    public Integer getDraw() {
        return draw;
    }
    public void setDraw(Integer draw) {
        this.draw = draw;
    }

    public Integer getLost() {
        return lost;
    }
    public void setLost(Integer lost) {
        this.lost = lost;
    }

    public Integer getPoints() {
        return points;
    }
    public void setPoints(Integer points) {
        this.points = points;
    }

    public Integer getGoalsFor() {
        return goalsFor;
    }
    public void setGoalsFor(Integer goalsFor) {
        this.goalsFor = goalsFor;
    }

    public Integer getGoalsAgainst() {
        return goalsAgainst;
    }
    public void setGoalsAgainst(Integer goalsAgainst) {
        this.goalsAgainst = goalsAgainst;
    }

    public Integer getGoalDifference() {
        return goalDifference;
    }
    public void setGoalDifference(Integer goalDifference) {
        this.goalDifference = goalDifference;
    }
}
