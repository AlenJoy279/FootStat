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

public class BundesligaActivity extends AppCompatActivity {
    List<Standing> dataList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bundesliga);

        TextView txt = (TextView) findViewById(R.id.textView);

        // Retrofit Builder
        Retrofit retrofit = new Retrofit.Builder().baseUrl(APICallBundesliga.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        // instance for interface
        APICallBundesliga APICallBundesliga = retrofit.create(APICallBundesliga.class);

        Call<MainResponse>call = APICallBundesliga.getData1();

        call.enqueue(new Callback<MainResponse>() {
            @Override
            public void onResponse(Call<MainResponse> call, Response<MainResponse> response) {

                MainResponse mainResponse = response.body();

                //PutDataIntoRecyclerView(Arrays.asList(mainResponse.getStandings()));


                dataList = new ArrayList(Arrays.asList(mainResponse.getStandings()));

                dataList = mainResponse.getStandings();

                txt.append("Stage = " + dataList.get(0).getStage() + "\n");
                for (int i = 0; i < dataList.get(0).getTable().size(); i++) {
                    txt.append("NAME : " + dataList.get(0).getTable().get(i).getTeam().getName() + "\n");
                    txt.append("POSITION : " + dataList.get(0).getTable().get(i).getPosition() + "\n");
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