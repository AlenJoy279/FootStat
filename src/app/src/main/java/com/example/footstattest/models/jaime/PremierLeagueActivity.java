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


public class PremierLeagueActivity extends AppCompatActivity {
    List<Standing> dataList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_premier_league);
        Context context;

        TextView txt = (TextView) findViewById(R.id.textView5);


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
}