package com.example.footstattest.models.jaime;


import android.os.Bundle;
import android.util.Log;
import android.widget.ListView;

import androidx.appcompat.app.AppCompatActivity;

import com.example.footstattest.R;
import com.example.footstattest.models.TeamListAdapter;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class LaLigaActivity extends AppCompatActivity {

    public static final String TAG = "LaLiga";
    List<Standing> LaLigadataList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_liga);
        Log.d(TAG, "onCreate: Started");

        ListView liga = (ListView) findViewById(R.id.liga_list);

        

        ArrayList<Table> tableList = new ArrayList<>();


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


                LaLigadataList = new ArrayList(Arrays.asList(mainResponse.getStandings()));

                LaLigadataList = mainResponse.getStandings();



                for (int i = 0; i < LaLigadataList.get(0).getTable().size(); i++) {

                    Table printFormat = new Table();
                    printFormat.setName(LaLigadataList.get(0).getTable().get(i).getTeam().getName());
                    printFormat.setPosition(LaLigadataList.get(0).getTable().get(i).getPosition());
                    printFormat.setWon(LaLigadataList.get(0).getTable().get(i).getWon());
                    printFormat.setDraw(LaLigadataList.get(0).getTable().get(i).getDraw());
                    printFormat.setLost(LaLigadataList.get(0).getTable().get(i).getLost());
                    Log.d(TAG, "onResponse: " + printFormat.getName());
                    tableList.add(printFormat);


                }
                Log.d(TAG, "onResponse: " + tableList.size());


                TeamListAdapter adapterA = new TeamListAdapter(LaLigaActivity.this, R.layout.league_row, tableList);
                liga.setAdapter(adapterA);


            }

            @Override
            public void onFailure(Call<MainResponse> call, Throwable t) {
            }
        });


    }


}