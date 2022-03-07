package com.example.footstattest.models.jaime;

import android.os.Bundle;
import android.widget.TextView;
import java.lang.Double;

import androidx.appcompat.app.AppCompatActivity;

import com.example.footstattest.R;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Hashtable;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class TeamRankings extends AppCompatActivity {
    List<Standing> dataList;
    ArrayList<EloScore> eloArray= new ArrayList<>();
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


                }


                //rankings = EloCalculator.sortValue(rankings);
                for (String name: rankings.keySet()) {

                    EloScore score = new EloScore();
                    score.setName(name.toString());
                    score.setScore(rankings.get(name));
                    eloArray.add(score);

                }

                eloArray.sort(Comparator.comparingDouble(EloScore::getScore));

                for (int i = eloArray.size() - 1; i >= 0; i--)
                    txt.append("Team: " + eloArray.get(i).getName() + "\nELO: " + eloArray.get(i).getScore() + "\n\n");
            }

            @Override
            public void onFailure(Call<MainResponse> call, Throwable t) {
            }
        });
    }


}