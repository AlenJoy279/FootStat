package com.example.footstattest.models.jaime;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.example.footstattest.R;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Hashtable;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class TeamRankings extends AppCompatActivity {
    List<Standing> dataList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_team_rankings);


        TextView txt = (TextView) findViewById(R.id.textView3);

        // Retrofit Builder
        Retrofit retrofit = new Retrofit.Builder().baseUrl(APIBig3.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        // instance for interface
        APIBig3 APIBig3 = retrofit.create(APIBig3.class);

        Call<MainResponse>call = APIBig3.getData3();

        call.enqueue(new Callback<MainResponse>() {
            @Override
            public void onResponse(Call<MainResponse> call, Response<MainResponse> response) {
                MainResponse mainResponse = response.body();

                //PutDataIntoRecyclerView(Arrays.asList(mainResponse.getStandings()));


                dataList = new ArrayList(Arrays.asList(mainResponse.getStandings()));

                dataList = mainResponse.getStandings();

                int elo;

                Hashtable<String, Double> rankings = new Hashtable<>();


                for (int i = 0; i < dataList.get(0).getTable().size(); i++) {
                    elo = EloCalculator.calculateElo(dataList.get(0).getTable().get(i).getTeam().getName()
                            , dataList.get(0).getTable().get(i).getWon(),
                            dataList.get(0).getTable().get(i).getLost(),
                            dataList.get(0).getTable().get(i).getDraw(),
                            dataList.get(0).getTable().get(i).getGoalDifference(),
                            dataList.get(0).getTable().get(i).getPlayedGames());

                    rankings = EloCalculator.add_to_rankings(dataList.get(0).getTable().get(i).getTeam().getName(), elo);

                    //txt.append("Rankings : " + rankings);

                    // String team, int wins, int losses, int draws, int goalDifference, int playedGames
                  /*  txt.append("ELO : "+ EloCalculator.calculateElo(dataList.get(0).getTable().get(i).getTeam().getName()
                            , dataList.get(0).getTable().get(i).getWon(),
                            dataList.get(0).getTable().get(i).getLost(),
                            dataList.get(0).getTable().get(i).getDraw(),
                            dataList.get(0).getTable().get(i).getGoalDifference(),
                            dataList.get(0).getTable().get(i).getPlayedGames()
                             ) + "\n"); */
                   // txt.append("NAME : " + dataList.get(0).getTable().get(i).getTeam().getName() + "\n");
                    //txt.append("POSITION : " + dataList.get(0).getTable().get(i).getPosition() + "\n");
                }


                //rankings = EloCalculator.sortValue(rankings);
                for (String name: rankings.keySet()) {
                    String key = name.toString();
                    Double value =   rankings.get(name);
                    txt.append("Team: " + key + "\nELO: " + value + "\n\n");
                }
            }

            @Override
            public void onFailure(Call<MainResponse> call, Throwable t) {
            }
        });
    }
    public void openBundesliga() {
        Intent intent = new Intent(this, BundesligaActivity.class);
        startActivity(intent);
    }
    public void openLaLiga() {
        Intent intent = new Intent(this, LaLigaActivity.class);
        startActivity(intent);
    }

    public void openPremierLeague() {
        Intent intent = new Intent(this, PremierLeagueActivity.class);
        startActivity(intent);
    }

    public void openRankings() {
        Intent intent = new Intent(this, TeamRankings.class);
        startActivity(intent);
    }

}