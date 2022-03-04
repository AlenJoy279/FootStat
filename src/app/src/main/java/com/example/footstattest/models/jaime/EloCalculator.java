package com.example.footstattest.models.jaime;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Hashtable;
import java.util.Map;

public class EloCalculator {
    private static double elo;
    private static Integer rounded_elo;

    //double elo;

    //private ArrayList<String> rankings = new ArrayList<String>();
    static Hashtable<String, Double> rankings = new Hashtable<>();

    public static int calculateElo(String team, int wins, int losses, int draws, double goalDifference, double playedGames){
        elo = (wins * 100) + (draws * 50) + (losses * 0);
       // double loss_ratio = (losses / playedGames) * 100;
        elo = elo + (goalDifference / playedGames) * 10;
        rounded_elo = (int) elo;
        return rounded_elo;
    }

    public static Hashtable<String, Double> add_to_rankings(String team, double elo){
        String otpt = (team + " : " + elo);
        rankings.put(team, elo);
        rankings = sortValue(rankings);
        return rankings;
    }

    public static Hashtable<String, Double> sortValue(Hashtable<String, Double> t){

        //Transfer as List and sort it
        ArrayList<Map.Entry<String, Double>> l = new ArrayList(t.entrySet());
        Collections.sort(l, new Comparator<Map.Entry<String, Double>>(){

            public int compare(Map.Entry<String, Double> o1, Map.Entry<String, Double> o2) {
                return o1.getValue().compareTo(o2.getValue());
            }});
        return t;
    }



}
