package com.example.footstattest.models.jaime;


import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.example.footstattest.R;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class LaLigaActivity extends AppCompatActivity {
    List<Standing> LaLigadataList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_la_liga);


        TextView txt = (TextView) findViewById(R.id.textView2);

        // Retrofit Builder
        Retrofit retrofit = new Retrofit.Builder().baseUrl(APICallLaLiga.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        // instance for interface
        APICallLaLiga APICallLaLiga = retrofit.create(APICallLaLiga.class);

        Call<MainResponse>call = APICallLaLiga.getData2();

        call.enqueue(new Callback<MainResponse>() {
            @Override
            public void onResponse(Call<MainResponse> call, Response<MainResponse> response) {
                MainResponse mainResponse = response.body();

                //PutDataIntoRecyclerView(Arrays.asList(mainResponse.getStandings()));

                LaLigadataList = new ArrayList(Arrays.asList(mainResponse.getStandings()));

                LaLigadataList = mainResponse.getStandings();

                for (int i = 0; i < LaLigadataList.get(0).getTable().size(); i++) {
                    txt.append("NAME : " + LaLigadataList.get(0).getTable().get(i).getTeam().getName() + "\n");
                    txt.append("POSITION : " + LaLigadataList.get(0).getTable().get(i).getPosition() + "\n");
                    txt.append("WINS : " + LaLigadataList.get(0).getTable().get(i).getWon() + "\n\n");
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