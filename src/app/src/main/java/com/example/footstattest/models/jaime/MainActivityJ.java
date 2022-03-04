package com.example.footstattest.models.jaime;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
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


public class MainActivityJ extends AppCompatActivity {
    private Button button;
    List<Standing> dataList;
    private Button button1;
    private Button button2;
    private Button button3;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_j);
        Context context;

        TextView txt = (TextView) findViewById(R.id.textView7);
        button = (Button) findViewById(R.id.button3);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openBundesliga();
            }
        });

        button1 = (Button) findViewById(R.id.button1);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openLaLiga();
            }
        });

        button2 = (Button) findViewById(R.id.button4);
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openRankings();
            }
        });

        button3 = (Button) findViewById(R.id.button2);
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openPremierLeague();
            }
        });


        // Retrofit Builder
        Retrofit retrofit = new Retrofit.Builder().baseUrl(APICall.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        // instance for interface
        APICall APICall = retrofit.create(APICall.class);

        Call<MainResponse>call = APICall.getData();

        call.enqueue(new Callback<MainResponse>() {
            @Override
            public void onResponse(Call<MainResponse> call, Response<MainResponse> response) {
               /* if (response.code() != 200) {
                    txt.setText("Check connection!  " + response.code());
                } */
                MainResponse mainResponse = response.body();

                //PutDataIntoRecyclerView(Arrays.asList(mainResponse.getStandings()));


                dataList = new ArrayList(Arrays.asList(mainResponse.getStandings()));

                dataList = mainResponse.getStandings();
                txt.append(dataList.get(0).getTable().get(0).getTeam().toString());

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
    public void openRankings() {
        Intent intent = new Intent(this, TeamRankings.class);
        startActivity(intent);
    }
    public void openPremierLeague() {
        Intent intent = new Intent(this, PremierLeagueActivity.class);
        startActivity(intent);
    }
}

